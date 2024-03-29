from django.shortcuts import render
from .models import Article
from django.http import JsonResponse

def index(request):
    # Check if there are any articles in the database
    articles_count = Article.objects.count()
    if articles_count == 3:
        # If no articles exist, create some initial articles
        create_initial_articles()
    
    # Retrieve the latest 24 articles
    articles = Article.objects.order_by('-created_at')[:24]
    print("Total number of articles:", articles_count)  # Add this line for debugging
    return render(request, 'index.html', {'articles': articles})


def create_initial_articles():
    # Create some initial articles
    articles_data = [
        {'title': 'Article 1', 'content': 'Content for article 1'},
        {'title': 'Article 2', 'content': 'Content for article 2'},
        {'title': 'Article 3', 'content': 'Content for article 3'},
        {'title': 'Article 4', 'content': 'Content for article 4'},
        {'title': 'Article 5', 'content': 'Content for article 5'},
        {'title': 'Article 6', 'content': 'Content for article 6'},
        {'title': 'Article 7', 'content': 'Content for article 7'},
        {'title': 'Article 8', 'content': 'Content for article 8'},
        {'title': 'Article 9', 'content': 'Content for article 9'},
        {'title': 'Article 10', 'content': 'Content for article 10'},
        {'title': 'Article 11', 'content': 'Content for article 11'},
        {'title': 'Article 12', 'content': 'Content for article 12'},
        {'title': 'Article 13', 'content': 'Content for article 13'},
        {'title': 'Article 14', 'content': 'Content for article 14'},
        {'title': 'Article 15', 'content': 'Content for article 15'},
        {'title': 'Article 16', 'content': 'Content for article 16'},
        {'title': 'Article 17', 'content': 'Content for article 17'},
        {'title': 'Article 18', 'content': 'Content for article 18'},
        {'title': 'Article 19', 'content': 'Content for article 19'},
        {'title': 'Article 20', 'content': 'Content for article 20'},
        {'title': 'Article 21', 'content': 'Content for article 21'},
        # Add more articles as needed
    ]
    for data in articles_data:
        Article.objects.create(title=data['title'], content=data['content'])

def load_more_articles(request):
    start_index = int(request.GET.get('start_index', 24))
    end_index = start_index + 24  # Load 3 more rows (12 articles)
    articles = Article.objects.order_by('-created_at')[start_index:end_index]
    data = {
        'articles': [{'title': article.title, 'content': article.content} for article in articles]
    }
    return JsonResponse(data)

