from django.http import HttpResponse


#Main page
def index(request):
    return HttpResponse('оБложка')


def group_posts(request, slug):
    return HttpResponse(f'Бложики по по группам. Условие группировки: {slug}')