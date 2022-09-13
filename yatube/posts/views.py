from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Main page
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    header_text = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'header_text': header_text,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    header_text = 'Записи сообщества '
    context = {
        'group': group,
        'posts': posts,
        'header_text': header_text,
    }

    return render(request, 'posts/group_list.html', context)
