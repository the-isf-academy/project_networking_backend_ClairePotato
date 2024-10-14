# views.py

from banjo.urls import route_get, route_post
from .models import Biology
from settings import BASE_URL

# post a new concept 
@route_post(BASE_URL + 'new', args={'concept':str, 'related_keywords': str, 'discussion' : str})
def new_concept(args):
    new_concept = Biology(
        concept = args['concept'],
        related_keywords = args['related_keywords'],
        confused = False,
        archive = False,
        discussion = args['discussion']
    )

    new_concept.save()

    return {'fortune': new_concept.json_response()}

# get all concepts
@route_get(BASE_URL + 'all')
def all_concepts(args):
    concept_list = []

    for concept in Biology.objects.all():
        concept.increase_view()
        concept_list.append(concept.json_response())
    return {'fortunes':concept_list}


# get one concept

# archive one concept
@route_post(BASE_URL + 'change_archive', args={'id':int})
def archive(args):
    if Biology.objects.filter(id=args['id']).exists():
        one_concept = Biology.objects.get(id=args['id']) 
        one_concept.change_archive()
        one_concept.increase_view()
        return {'fortune': one_concept.json_response()}
    else:
        return {'error': 'no riddle exists'}
    
# view all archived concepts

# search for keywords
@route_get(BASE_URL + 'search', args={'keyword':str})
def search(args):
    keyword_list = []
    # add 'or' so that it appends even if the word appears in the discussion?
    for concept in Biology.objects.filter(statement__contains=args['keyword']):
        keyword_list.append(concept.json_response())
        concept.increase_view()
    # add fuzzy wuzzy

    return {'concept':keyword_list}

