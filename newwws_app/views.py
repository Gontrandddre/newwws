from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import CustomUserCreationForm, AuthenticationFormApp
from .models import CustomUser, Article, Saved
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
            articles = data.news()

            if articles['totalResults'] == 0:
                messages.warning(request, 'No articles about it, try an other key-word.')
            
            else:
                request.session['query'] = input_user
                request.session['mode'] = request.POST.get('mode')
                return redirect("newwws_app:news")

        elif request.POST.get('mode') == 'on':

            data = RequestApiHeadlines(q=input_user)
            articles = data.daily_news()

            if articles['totalResults'] == 0:
                messages.warning(request, 'No recent news about it, try an other key-word or change mode.')
        
            else:
                request.session['query'] = input_user
                request.session['mode'] = request.POST.get('mode')
                return redirect("newwws_app:daily_news")
        
        else:
            pass
        
    return render(request, 'newwws_app/index.html', {})


def daily_news(request):

    try:
        data = RequestApiHeadlines(q=request.session['query']).daily_news()
        value_input = request.session['query']
        
    except KeyError:
        data = RequestApiHeadlines(q="politic").daily_news()
        value_input = 'politic'

    if request.method == 'POST':

        if request.POST.get('save'):

            # Get current article data
            item = RequestApiHeadlines(q=request.POST.get('save')).daily_news()
            
            # Create or update object Article
            Article.objects.update_or_create(
                        defaults={'title': item['articles'][0]['title']},
                        description = item['articles'][0]['description'],
                        author = item['articles'][0]['author'],
                        content = item['articles'][0]['content'],
                        published_at = item['articles'][0]['publishedAt'],
                        url = item['articles'][0]['url'],
                        url_to_image = item['articles'][0]['urlToImage']
                    )
            
            # Search current User and Article
            current_article = get_object_or_404(Article, title=request.POST.get('save'))
            current_user = get_object_or_404(CustomUser, pk=request.user.id)
            
            # Save or not current article by current user
            alreadySaved = Saved.objects.filter(user=current_user, article=current_article)
            if not alreadySaved.exists():
                saved = Saved.objects.create(
                    user=current_user,
                    article=current_article
                )
                saved.save()
                messages.success(request, 'Article saved ! Now available in my-news section.')
            else:
                messages.info(request, 'You have already saved this article.')
            

        if request.POST.get('search') or request.POST.get('category') or request.POST.get('language'):
            
            # q must be None instead of empty
            if request.POST.get('search') == "":
                q = None
            else:
                q = request.POST.get('search') 

            category = request.POST.get('category')
            language = request.POST.get('language')
            data = RequestApiHeadlines(q=q, category=category, language=language).daily_news()
    
            value_input = request.POST.get('search')

    if data['articles'] == []:
        messages.warning(request, 'Your request get 0 articles')

    return render(request, 'newwws_app/daily_news.html', {
        "articles": data['articles'],
        "value_input": value_input,
        "CATEGORIES": CATEGORIES,
        "LANGUAGES": LANGUAGES,
    })

def news(request):

    try:
        data = RequestApiEverything(q=request.session['query']).news()
        value_input = request.session['query']
        
    except KeyError:
        data = RequestApiEverything(q="politic").news()
        value_input = 'politic'

    if request.method == 'POST':

        if request.POST.get('save'):

            # Get current article data
            item = RequestApiEverything(q=request.POST.get('save')).news()
            
            # Create or update object Article
            Article.objects.update_or_create(
                        defaults={'title': item['articles'][0]['title']},
                        description = item['articles'][0]['description'],
                        author = item['articles'][0]['author'],
                        content = item['articles'][0]['content'],
                        published_at = item['articles'][0]['publishedAt'],
                        url = item['articles'][0]['url'],
                        url_to_image = item['articles'][0]['urlToImage']
                    )
            
            # Search current User and Article
            current_article = get_object_or_404(Article, title=request.POST.get('save'))
            current_user = get_object_or_404(CustomUser, pk=request.user.id)
            
            # Save or not current article by current user
            alreadySaved = Saved.objects.filter(user=current_user, article=current_article)
            if not alreadySaved.exists():
                saved = Saved.objects.create(
                    user=current_user,
                    article=current_article
                )
                saved.save()
                messages.success(request, 'Article saved ! Now available in my-news section.')
            else:
                messages.info(request, 'You have already saved this article.')
        
        if request.POST.get('search') or request.POST.get('category') or request.POST.get('language'):
            
            q = request.POST.get('search')
            language = request.POST.get('language')

            # premium access only
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

            data = RequestApiEverything(q=q, language=language, from_param=from_param, to=to).news()

            value_input = request.POST.get('search')

    if data['articles'] == []:
        messages.warning(request, 'Your request get 0 article.')

    return render(request, 'newwws_app/news.html', {
        "articles": data['articles'],
        "value_input": value_input,
        "SORTBY": SORTBY,
        "LANGUAGES": LANGUAGES,
    })

@login_required(login_url="login")
def saved(request):
    
    data = Saved.objects.filter(user=request.user.id)
    current_user = get_object_or_404(CustomUser, pk=request.user.id)

    if request.method == 'POST':

        if request.POST.get('read'):

            current_article = request.POST.get('current_article')
            read_status = request.POST.get('read')
            update_saved_current_article = data.get(
                                                article=current_article,
                                            )
            update_saved_current_article.read = read_status
            update_saved_current_article.save()
            data = data

            messages.success(request, "Article read.")

        if request.POST.get('delete'):
            
            current_article = request.POST.get('current_article')
            delete_current_article = data.get(
                                                article=current_article,
                                            )
            delete_current_article.delete()
            data = data

            messages.success(request, "Article deleted.")

        # elif request.POST.get('search') or \
        #      request.POST.get('form_param') or \
        #      request.POST.get('to') or \
        #      request.POST.get('read_param') or \

        #     data = data.filter(
        #                 tilte__contains=request.POST.get('search'),
        #                 publiashedAt__time__range=(
        #                     datetime.time(request.POST.get('form_param'),
        #                     datetime.time(request.POST.get('to'))
        #                 ),
        #                 read=request.POST.get('read_param')
        #             )
    
    if data.count() == 0:
        messages.warning(request, "Not article saved.")
    
    else:
        paginator = Paginator(data, 8)
        page = request.GET.get("page")
        list_pages = [*range(1, (paginator.num_pages)+1, 1)]

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

    return render(request, 'newwws_app/saved.html', {
        "articles": data,
        "list_pages": list_pages,
        "current_page": page,
    })

@login_required(login_url="login")
def article(request, id_article):

    data = Saved.objects.get(article=id_article)

    if request.POST.get('read'):

            current_article = request.POST.get('current_article')
            read_status = request.POST.get('read')
            update_saved_current_article = data.get(
                                                article=current_article,
                                            )
            update_saved_current_article.read = read_status
            update_saved_current_article.save()
            data = data

            messages.success(request, "Article read.")
    

    return render(request, 'newwws_app/article.html', {
        "article": data,
    })

@login_required(login_url="login")
def account(request):
    return render(request, 'newwws_app/account.html', {})