from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from ..models import Article, CustomUser, Saved

class StaticPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            email="test@test.test", password="testPassword"
        )
        self.client.login(email="test@test.test", password="testPassword")

    def test_register_page(self):
        response = self.client.get(reverse("newwws_app:register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")
        self.assertEqual(response.resolver_match.func.__name__, "register")
        self.assertIn(
            "Inscription",
            response.content.decode("utf8")
        )

    def test_login_page(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        self.assertEqual(response.resolver_match.func.__name__, "LoginView")
        self.assertIn(
            "Welcome back !",
            response.content.decode("utf8")
        )

    def test_index_page(self):
        response = self.client.get(reverse("newwws_app:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newwws_app/index.html")
        self.assertEqual(response.resolver_match.func.__name__, "index")
        self.assertIn(
            "Welcome To Newwws !",
            response.content.decode("utf8")
        )
    
    def test_logout_page(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/logged_out.html")
        self.assertEqual(response.resolver_match.func.__name__, "LogoutView")
        self.assertIn(
            "See you !",
            response.content.decode("utf8")
        )
    
    def test_daily_news_page(self):
        response = self.client.get(reverse("newwws_app:daily_news"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newwws_app/daily_news.html")
        self.assertEqual(response.resolver_match.func.__name__, "daily_news")
        self.assertIn(
            "Your daily newwws !",
            response.content.decode("utf8")
        )

    def test_news_page(self):
        response = self.client.get(reverse("newwws_app:news"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newwws_app/news.html")
        self.assertEqual(response.resolver_match.func.__name__, "news")
        self.assertIn(
            "Every newwws !",
            response.content.decode("utf8")
        )
    
    def test_my_news_page(self):
        response = self.client.get(reverse("newwws_app:saved"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newwws_app/saved.html")
        self.assertEqual(response.resolver_match.func.__name__, "saved")
        self.assertIn(
            "Your saved articles !",
            response.content.decode("utf8")
        )

    # def test_article_page(self):
    #     article = Article.objects.create(title="test")
    #     article.save()

    #     response = self.client.get('/article/1')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "newwws_app/article.html")
    #     self.assertEqual(response.resolver_match.func.__name__, "article")

    def test_legal_notice_page(self):
        response = self.client.get(reverse("newwws_app:legal-notice"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newwws_app/legal_notice.html")
        self.assertEqual(response.resolver_match.func.__name__, "TemplateView")
        self.assertIn(
            "Technologies",
            response.content.decode("utf8")
        )

# login
# logout

# session

# API > methods.py

# methods all



