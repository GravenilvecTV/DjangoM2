from django.shortcuts import render, get_object_or_404
from .models import Article

def show_article(request, numero):
    try:
        # recuperer l'article avec ce numero dans la bdd
        article = get_object_or_404(Article, pk=numero)
        return render(request, "article.html", context={'article': article})
    except:
        return render(request, "article-not-found.html")

def blog_index(request):
    # on recupere tout les articles de blog de la bdd
    all_articles = Article.objects.all()

    return render(request, "index.html", context={'articles': all_articles})