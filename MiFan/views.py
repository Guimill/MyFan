# views.py
from django.shortcuts import render
from .models import Article
from django.http import JsonResponse

def index(request):
    articles = Article.objects.order_by('-created_at')[:24]  # Retrieve latest 24 articles
    return render(request, 'index.html', {'articles': articles})

def load_more_articles(request):
    start_index = int(request.GET.get('start_index', 24))
    end_index = start_index + 24
    articles = Article.objects.order_by('-created_at')[start_index:end_index]
    data = {
        'articles': [{'title': article.title, 'content': article.content} for article in articles]
    }
    return JsonResponse(data)