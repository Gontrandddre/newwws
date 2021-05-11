from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from ..models import Article, CustomUser, Saved
from ..methods import ParseMode, RequestApiEverything, RequestApiHeadlines


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="normal@user.com",
            password="foo"
        )
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser("super@user.com", "foo")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False
            )


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
        self.client.session['query'] = 'politic'
        self.client.session.save()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newwws_app/daily_news.html")
        self.assertEqual(response.resolver_match.func.__name__, "daily_news")
        self.assertIn(
            "Your daily newwws !",
            response.content.decode("utf8")
        )

    def test_news_page(self):
        response = self.client.get(reverse("newwws_app:news"))
        self.client.session['query'] = 'politic'
        self.client.session.save()
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

    def test_legal_notice_page(self):
        response = self.client.get(reverse("newwws_app:legal-notice"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newwws_app/legal_notice.html")
        self.assertEqual(response.resolver_match.func.__name__, "TemplateView")
        self.assertIn(
            "Technologies",
            response.content.decode("utf8")
        )

class LogInPageTestCase(TestCase):
    def test_logIn_page(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            email="test@test.test", password="test"
        )
        self.client.login(email="test@test.test", password="test")
        self.assertIn("_auth_user_id", self.client.session)


class LogOutPageTestCase(TestCase):
    def test_logOut_page(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            email="test@test.test", password="test"
        )
        self.client.login(email="test@test2.test", password="test")
        self.client.logout()
        self.assertNotIn("_auth_user_id", self.client.session)


class ParseModeTestCase(TestCase):
    def test_parseMode(self):
        input = "Test de ParseMode %_ "
        data = ParseMode(input)
        data.cleanInput()
        self.assertEqual(
            data.user_input_cleaned,
            'test parsemode'
        )


class RequestApiEverythingTestCase(TestCase):
    def test_RequestApiEverything(self):
        data = RequestApiEverything(q='test')
        articles = data.news()
        self.assertEqual(
            articles['status'],
            'ok'
        )


class RequestApiHeadlinesTestCase(TestCase):
    def test_RequestApiHeadlines(self):
        data = RequestApiHeadlines(q='test')
        articles = data.daily_news()
        self.assertEqual(
            articles['status'],
            'ok'
        )
