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

    return {'biology': new_concept.json_response()}

# get all concepts ✅
@route_get(BASE_URL + 'all')
def all_concepts(args):
    concept_list = []

    for concept in Biology.objects.all():
        concept.increase_view()
        concept_list.append(concept.json_response())
    return {'biology':concept_list}


# get one concept ✅
@route_get(BASE_URL + 'one', args={'id':int})
def one_concept(args):
    if Biology.objects.filter(id=args['id']).exists():
        one_concept = Biology.objects.get(id=args['id'])
        return {'biology': one_concept.json_response()}
    else:
        return {'error': 'no concept exists'}

# archive one concept ✅
@route_post(BASE_URL + 'archive', args={'id':int})
def archive(args):
    if Biology.objects.filter(id=args['id']).exists():
        one_concept = Biology.objects.get(id=args['id']) 
        one_concept.change_archive()
        one_concept.increase_view()
        return {'biology': one_concept.json_response()}
    else:
        return {'error': 'no concept exists'}
    
# view all archived concepts ✅
@route_get(BASE_URL + 'all_archived')
def all_archived(args):
    archived_list = []

    for concept in Biology.objects.all():
        if concept.archive == True:
            concept.increase_view()
            archived_list.append(concept.json_response())
    return {'biology':archived_list}

# search for keywords ✅
@route_get(BASE_URL + 'search', args={'keyword':str})
def search(args):
    keyword_list = []
    for object in Biology.objects.all():
        if args['keyword'] in object.concept:
            keyword_list.append(object.json_response())
            object.increase_view()
        elif args['keyword'] in object.related_keywords:
            keyword_list.append(object.json_response())
            object.increase_view()
        elif args['keyword'] in object.discussion:
            keyword_list.append(object.json_response())
            object.increase_view()
        else:
            return {'error': 'no concept exists, try another keyword!'}
    
    return {'biology':keyword_list}

# mark a concept as confusing ✅
@route_post(BASE_URL + 'confused', args={'id':int})
def confused(args):
    if Biology.objects.filter(id=args['id']).exists():
        one_concept = Biology.objects.get(id=args['id']) 
        one_concept.mark_as_confused()
        one_concept.increase_view()
        return {'biology': one_concept.json_response()}
    else:
        return {'error': 'no concept exists'}

# get all concepts in order from most to least confusing ✅
@route_get(BASE_URL + 'confused_ranked')
def confused_rank(args):
    concept_list = []
    for concept in Biology.objects.order_by("-confused_percentage"):
        concept.calculate_confused_percentage()
        concept.increase_view()
        concept_list.append(concept.confused_percentage_json_response())
    return {'biology':concept_list}

# add to discussion 
@route_post(BASE_URL + 'add_to_discussion', args={'id':int, 'discussion':str})
def add(args):
    if Biology.objects.filter(id=args['id']).exists():
        concept = Biology.objects.get(id=args['id'])
        concept.add_to_discussion(args['discussion'])
        concept.increase_view()
    return {'biology':concept.json_response()}