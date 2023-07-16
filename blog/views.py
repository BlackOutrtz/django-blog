from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Sobre
from posts_categorias.models import Mundo, Politica, PopArtes, Economia, Tecnologia, Educacao, Saude
from django.db.models import Q

PER_PAGE = 9

def index(request):
    posts = (
        Post
        .objects
        .filter(is_published=True)
        .order_by('-pk')    
    )

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/index.html',
        {
            'page_obj': page_obj,
        }
    )


def category(request, slug):
    posts = (
        Post
        .objects
        .filter(is_published=True, category__slug=slug)
        .order_by('-pk')    
    )

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/index.html',
        {
            'page_obj': page_obj,
        }
    )

def search(request):
    search_value = request.GET.get('search', '').strip()

    posts = (
        Post
        .objects
        .filter(is_published=True)
        .filter(
            Q(title__icontains=search_value) |
            Q(excerpt__icontains=search_value) |
            Q(content__icontains=search_value)
        )[0:PER_PAGE] 
    )

    return render(
        request,
        'blog/index.html',
        {
            'page_obj': posts,
            'search_value': search_value,
        }
    )

def sobre(request):
    sobre = (
        Sobre
        .objects
        .all()
    )

    return render(
        request,
        'blog/sobre.html',
        {
            'sobre': sobre,    
        }
    )




def post(request, slug):
    post = (
        Post
        .objects
        .filter(is_published=True, slug=slug)
        .order_by('-pk')
        .first()    
    )


    return render(
        request,
        'blog/post.html',
        {
            'post': post,
        }
    )

def mundo(request):
    mundo = (
        Mundo
        .objects
        .filter(is_published=True)

    )

    return render(
        request,
        'blog/categorias/mundo.html',
        {
            'mundo': mundo,
        }    
    )

def post_mundo(request, slug):
    post_mundo = (
        Mundo
        .objects
        .filter(is_published=True, slug=slug)
        .order_by('-pk')
        .first()    
    )


    return render(
        request,
        'blog/categorias/postcategorias/post_mundo.html',
        {
            'post_mundo': post_mundo,
        }
    )

def politica(request):
    politica = (
        Politica
        .objects
        .filter(is_published=True)

    )

    return render(
        request,
        'blog/categorias/politica.html',
        {
            'politica': politica,
        }    
    )

def post_politica(request, slug):
    post_politica = (
        Politica
        .objects
        .filter(is_published=True, slug=slug)
        .order_by('-pk')
        .first()    
    )


    return render(
        request,
        'blog/categorias/postcategorias/post_politica.html',
        {
            'post_politica': post_politica,
        }
    )

def pop_arte(request):
    pop_arte = (
        PopArtes
        .objects
        .filter(is_published=True)

    )

    return render(
        request,
        'blog/categorias/pop_arte.html',
        {
            'pop_arte': pop_arte,
        }    
    )

def post_pop_arte(request, slug):
    post_pop_arte = (
        PopArtes
        .objects
        .filter(is_published=True, slug=slug)
        .order_by('-pk')
        .first()    
    )


    return render(
        request,
        'blog/categorias/postcategorias/post_pop_arte.html',
        {
            'post_pop_arte': post_pop_arte,
        }
    )


def economia(request):
    economia = (
        Economia
        .objects
        .filter(is_published=True)

    )

    return render(
        request,
        'blog/categorias/economia.html',
        {
            'economia': economia,
        }    
    )

def post_economia(request, slug):
    post_economia = (
        Economia
        .objects
        .filter(is_published=True, slug=slug)
        .order_by('-pk')
        .first()    
    )


    return render(
        request,
        'blog/categorias/postcategorias/post_economia.html',
        {
            'post_economia': post_economia,
        }
    )


def tecnologia(request):
    tecnologia = (
        Tecnologia
        .objects
        .filter(is_published=True)

    )

    return render(
        request,
        'blog/categorias/tecnologia.html',
        {
            'tecnologia': tecnologia,
        }    
    )

def post_tecnologia(request, slug):
    post_tecnologia = (
        Tecnologia
        .objects
        .filter(is_published=True, slug=slug)
        .order_by('-pk')
        .first()    
    )


    return render(
        request,
        'blog/categorias/postcategorias/post_tecnologia.html',
        {
            'post_tecnologia': post_tecnologia,
        }
    )

def educacao(request):
    educacao = (
        Educacao
        .objects
        .filter(is_published=True)

    )

    return render(
        request,
        'blog/categorias/educacao.html',
        {
            'educacao': educacao,
        }    
    )

def post_educacao(request, slug):
    post_educacao = (
        Educacao
        .objects
        .filter(is_published=True, slug=slug)
        .order_by('-pk')
        .first()    
    )


    return render(
        request,
        'blog/categorias/postcategorias/post_educacao.html',
        {
            'post_educacao': post_educacao,
        }
    )


def saude(request):
    saude = (
        Saude
        .objects
        .filter(is_published=True)

    )

    return render(
        request,
        'blog/categorias/saude.html',
        {
            'saude': saude,
        }    
    )

def post_saude(request, slug):
    post_saude = (
        Saude
        .objects
        .filter(is_published=True, slug=slug)
        .order_by('-pk')
        .first()    
    )


    return render(
        request,
        'blog/categorias/postcategorias/post_saude.html',
        {
            'post_saude': post_saude,
        }
    )


def handler404(request, exception):
    return render(request, 'blog/404.html', status=404)


def handler505(request, exception):
    return render(request, 'blog/505.html', status=505)