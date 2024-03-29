from django.shortcuts import render
from .models import Article
from django.http import JsonResponse

def index(request):

    Article.objects.all().delete()

    # Check if there are any articles in the database
    articles_count = Article.objects.count()
    if articles_count == 0:
        # If no articles exist, create some initial articles
        create_initial_articles()
    
    # Retrieve the latest 24 articles
    articles = Article.objects.order_by('-created_at')[:12]
    return render(request, 'index.html', {'articles': articles})

def load_more_articles(request):
    start_index = int(request.GET.get('start_index', 24))
    end_index = start_index + 12  # Load 3 more rows (12 articles)
    articles = Article.objects.order_by('-created_at')[start_index:end_index]

    data = {
        'articles': [{'title': article.title, 'content': article.content} for article in articles]
    }

    if not articles:
        # If no more articles are available, return an empty response
        return JsonResponse({})

    return JsonResponse(data)

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
        {'title': 'Article 22', 'content': 'Content for article 22'},
        {'title': 'Article 23', 'content': 'Content for article 23'},
        {'title': 'Article 24', 'content': 'Content for article 24'},
        {'title': 'Article 25', 'content': 'Content for article 25'},
        {'title': 'Article 26', 'content': 'Content for article 26'},
        {'title': 'Article 27', 'content': 'Content for article 27'},
        {'title': 'Article 28', 'content': 'Content for article 28'},
        {'title': 'Article 29', 'content': 'Content for article 29'},
        {'title': 'Article 30', 'content': 'Content for article 30'},
        {'title': 'Article 31', 'content': 'Content for article 31'},
        {'title': 'Article 32', 'content': 'Content for article 32'},
        {'title': 'Article 33', 'content': 'Content for article 33'},
        {'title': 'Article 34', 'content': 'Content for article 34'},
        {'title': 'Article 35', 'content': 'Content for article 35'},
        {'title': 'Article 36', 'content': 'Content for article 36'},
        {'title': 'Article 37', 'content': 'Content for article 37'},
        {'title': 'Article 38', 'content': 'Content for article 38'},
        {'title': 'Article 39', 'content': 'Content for article 39'},

    ]
    for data in articles_data:
        Article.objects.create(title=data['title'], content=data['content'])
