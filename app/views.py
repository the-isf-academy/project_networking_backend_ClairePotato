# views.py

from banjo.urls import route_get, route_post
from .models import Biology
from settings import BASE_URL

# post a new concept ✅
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

# get all concepts ✅
@route_get(BASE_URL + 'all')
def all_concepts(args):
    concept_list = []

    for concept in Biology.objects.all():
        concept.increase_view()
        concept_list.append(concept.json_response())
    return {'fortunes':concept_list}


# get one concept ✅
@route_get(BASE_URL + 'one', args={'id':int})
def one_concept(args):
    if Biology.objects.filter(id=args['id']).exists():
        one_concept = Biology.objects.get(id=args['id'])
        return {'riddle': one_concept.json_response()}
    else:
        return {'error': 'no riddle exists'}

# archive one concept ✅
@route_post(BASE_URL + 'archive', args={'id':int})
def archive(args):
    if Biology.objects.filter(id=args['id']).exists():
        one_concept = Biology.objects.get(id=args['id']) 
        one_concept.change_archive()
        one_concept.increase_view()
        return {'fortune': one_concept.json_response()}
    else:
        return {'error': 'no rconcept exists'}
    
# view all archived concepts

# search for keywords
@route_get(BASE_URL + 'search', args={'keyword':str})
def search(args):
    # keyword_list = []
    # add 'or' so that it appends even if the word appears in the discussion?
    for object in Biology.objects.all():
        if args['keyword'] in object.concept:
            # concept.filter(concept__contains=args['keyword']):
            print("hi")
            # keyword_list.append(concept.json_response())
            # concept.increase_view()
        # elif concept in  Biology.objects.filter(related_keywords__contains=args['keyword']):
        #     keyword_list.append(concept.json_response())
        #     concept.increase_view()
        # elif concept in  Biology.objects.filter(discussion__contains=args['keyword']):
        #     keyword_list.append(concept.json_response())
        #     concept.increase_view()
    
    # return {'concept':keyword_list}

