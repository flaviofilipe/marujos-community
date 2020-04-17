from django.shortcuts import render
from blog.models import Post, Category
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q

def getCategorias():

    categorias = Category.objects.order_by('name')
    if categorias.count() > 3:
        col = int(categorias.count()/2)

        if(col % 2 == 1):
            col = col+1

        categorias_col1 = categorias[:col]
        categorias_col2 = categorias[col:]
    else:
        categorias_col1 = categorias
        categorias_col2 = []

    return [categorias_col1, categorias_col2]


def index(request, pk=None):
    title = 'Publicações'

    category = request.GET.get('category')
    template = 'blog/index.html'
    page = request.GET.get('page')
    query = request.GET.get('q')

    if pk:
        template = 'blog/posts/view_post.html'
        posts = get_object_or_404(Post, id=pk)
    elif category:
        posts_list = Post.objects.filter(category__name=category)
        paginator = Paginator(posts_list, 10)  # Show 25 contacts per page
        posts = paginator.get_page(page)
    elif query:
        lookups = Q(title__icontains=query) | Q(text__icontains=query)
        posts = Post.objects.filter(lookups).distinct().order_by('-published_date')
    else:
        posts_list = Post.objects.order_by('-published_date')
        paginator = Paginator(posts_list, 10)  # Show 25 contacts per page
        posts = paginator.get_page(page)

    category_list = getCategorias()
    context = {
        'title': title,
        'posts': posts,
        'categorias_col1': category_list[0],
        'categorias_col2': category_list[1]

    }
    return render(request, template, context)
