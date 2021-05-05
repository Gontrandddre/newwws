from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, AuthenticationFormApp

from .models import Article
from .methods import ParseMode, RequestApiHeadlines, RequestApiEverything
from .constantes import CATEGORIES, LANGUAGES, SORTBY

from datetime import datetime


# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect("newwws_app:index")

    if request.method == "GET":
        form = AuthenticationFormApp()
        return render(request, "registration/login.html", {"form": form})

    if request.method == "POST":
        form = AuthenticationFormApp(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("newwws_app:index")
        else:
            print("User not found")
    else:
        return render(request, "login_error.html", {"form": form})
    

def register(request):

    if request.method == "GET":
        form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if password == password2:
                form.save()
                user = authenticate(email=email, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect("newwws_app:index")
            else:
                # form = CustomUserCreationForm()
                print("passwords not equals")
        else:
            print("Register not valid")

    return render(request, "registration/register.html", {"form": form})


def index(request):

    if request.method == 'POST':
        
        data = ParseMode(request.POST.get('query'))
        input_user = data.cleanInput()
        
        if input_user == "":
            messages.warning(request, 'No key word detected. Please try again')
        
        elif request.POST.get('mode') == None:
            
            data = RequestApiEverything(q=input_user)
            articles = data.articles()

            if articles['totalResults'] == 0:
                messages.warning(request, 'No articles about it, try an other key-word.')
            
            else:
                request.session['query'] = input_user
                request.session['mode'] = request.POST.get('mode')
                return redirect("newwws_app:articles")

        elif request.POST.get('mode') == 'on':

            data = RequestApiHeadlines(q=input_user)
            articles = data.news()

            if articles['totalResults'] == 0:
                messages.warning(request, 'No recent news about it, try an other key-word or change mode.')
        
            else:
                request.session['query'] = input_user
                request.session['mode'] = request.POST.get('mode')
                return redirect("newwws_app:news")
        
        else:
            pass
        
    return render(request, 'newwws_app/index.html', {})


def news(request):

    try:
        data = RequestApiHeadlines(q=request.session['query'])
        value_input = request.session['query']
        
    except KeyError:
        data = RequestApiHeadlines(q="politic")
        value_input = 'politic'

    articles = data.news()
    
    if request.method == 'POST':

        if request.POST.get('save'):
            # data = RequestApiEverything(qintitle=request.POST.get('save'))
            # element = data.articles()
            
            # Article.objects.update_or_create(
            #             defaults={'title': element['articles'][0]['title']},
            #             description = element['articles'][0]['description'],
            #             author = element['articles'][0]['author'],
            #             content = element['articles'][0]['content'],
            #             published_at = element['articles'][0]['publishedAt'],
            #             url = element['articles'][0]['url'],
            #             url_to_image = element['articles'][0]['urlToImage']
            #         )
            
            # article = get_object_or_404(Article, title=request.POST.get('save'))
            # user = get_object_or_404(User, pk=1) # refacto to request.user.id
            # user.article_set.add(article)

            messages.success(request, 'Article saved ! Now available in my-news section.')

        if request.POST.get('search') or request.POST.get('category') or request.POST.get('language'):
            
            if request.POST.get('search') == "":
                q = None
            else:
                q = request.POST.get('search') 
            category = request.POST.get('category')
            language = request.POST.get('language')
            data = RequestApiHeadlines(q=q, category=category, language=language)
            articles = data.news()

            value_input = request.POST.get('search')

            if articles['articles'] == []:
                messages.warning(request, 'Your request get 0 articles')

    return render(request, 'newwws_app/news.html', {
        "articles": articles['articles'],
        "value_input": value_input,
        "CATEGORIES": CATEGORIES,
        "LANGUAGES": LANGUAGES,
    })

def articles(request):

    try:
        data = RequestApiEverything(q=request.session['query'])
        value_input = request.session['query']
        
    except KeyError:
        data = RequestApiEverything(q="politic")
        value_input = 'politic'

    articles = data.articles()

    if request.method == 'POST':

        if request.POST.get('save'):
            # data = RequestApiEverything(qintitle=request.POST.get('save'))
            # element = data.articles()
            
            # Article.objects.update_or_create(
            #             defaults={'title': element['articles'][0]['title']},
            #             description = element['articles'][0]['description'],
            #             author = element['articles'][0]['author'],
            #             content = element['articles'][0]['content'],
            #             published_at = element['articles'][0]['publishedAt'],
            #             url = element['articles'][0]['url'],
            #             url_to_image = element['articles'][0]['urlToImage']
            #         )
            
            # article = get_object_or_404(Article, title=request.POST.get('save'))
            # user = get_object_or_404(User, pk=1) # refacto to request.user.id
            # user.article_set.add(article)

            messages.success(request, 'Article saved ! Now available in my-news section.')
        
        if request.POST.get('search') or request.POST.get('category') or request.POST.get('language'):
            
            q = request.POST.get('search')
            language = request.POST.get('language')

            # premium access
            try: 
                from_param = datetime.strptime(
                    request.POST.get('from_param'),
                    "%Y-%m-%d"
                ).strftime('%Y-%m-%d')
                to = datetime.strptime(
                    request.POST.get('to'),
                    "%Y-%m-%d"
                ).strftime('%Y-%m-%d')
            except TypeError:
                from_param = None
                to = None

            data = RequestApiEverything(q=q, language=language, from_param=from_param, to=to)
            articles = data.articles()

            value_input = request.POST.get('search')

            if articles['articles'] == []:
                    messages.warning(request, 'Your request get 0 article.')

    print(type(articles['articles'][0]['publishedAt']))
    return render(request, 'newwws_app/articles.html', {
        "articles": articles['articles'],
        "value_input": value_input,
        "SORTBY": SORTBY,
        "LANGUAGES": LANGUAGES,
    })

@login_required(login_url="login")
def article(request):
    return render(request, 'newwws_app/article.html', {})

@login_required(login_url="login")
def saved(request):
    return render(request, 'newwws_app/saved.html', {})

@login_required(login_url="login")
def account(request):
    return render(request, 'newwws_app/account.html', {})