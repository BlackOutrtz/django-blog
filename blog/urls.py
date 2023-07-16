from django.urls import path
from blog.views import index, sobre, post, post_mundo, mundo, politica, post_politica, pop_arte, post_pop_arte, economia, post_economia, tecnologia, post_tecnologia, educacao, post_educacao, saude, post_saude, search 

urlpatterns = [
    
    # Pagina inicial
    path('', index, name='index'),
    
    # Pagina dos posts
    path('post/<slug:slug>', post, name='post'),
    
    # Pagina sobre a empresa
    path('sobre/empresa/', sobre, name='sobre'),
    
    # Pagina de busca
    path('search/', search, name='search'),
    
    # Pagina da categoria mundo
    path('categoria/mundo/', mundo, name='mundo'),
    path('categoria/mundo/<slug:slug>', post_mundo, name='postmundo'),
    
    # Pagina da categoria politica
    path('categoria/politica/', politica, name='politica'),
    path('categoria/politica/<slug:slug>', post_politica, name='postpolitica'),
    
    # Pagina da categoria pop&arte
    path('categoria/pop&arte/', pop_arte, name='poparte'),
    path('categoria/pop&arte/<slug:slug>', post_pop_arte, name='postpoparte'),
    
    # Pagina da categoria economia
    path('categoria/economia/', economia, name='economia'),
    path('categoria/economia/<slug:slug>', post_economia, name='posteconomia'),

    # Pagina da categoria tecnologia
    path('categoria/tecnologia/', tecnologia, name='tecnologia'),
    path('categoria/tecnologia/<slug:slug>', post_tecnologia, name='posttecnologia'),

    # Pagina da categoria educacao
    path('categoria/educacao/', educacao, name='educacao'),
    path('categoria/educacao/<slug:slug>', post_educacao, name='posteducacao'),
    
    # Pagina de categoria saude
    path('categoria/saude/', saude, name='saude'),
    path('categoria/saude/<slug:slug>', post_saude, name='postsaude'),
]
