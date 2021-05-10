


from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings
from django.urls import reverse

from ..models import Article, CustomUser, Saved

from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1920x1080")

class AuthSelenium(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            executable_path=str(
                settings.BASE_DIR / "webdrivers" / "chromedriver"
            ),
            options=chrome_options,
        )
        self.browser.implicitly_wait(10)
        self.browser.maximize_window()

        CustomUser.objects.create_user(
            email="testSelenium@test.test", password="testPasswordSelenium"
        )

    def tearDown(self):
        self.browser.close()

    # def test_wrong_login_selenium(self):
    #     self.browser.get(self.live_server_url + reverse("login"))
    #     self.browser.find_element_by_id("emailLogin").send_keys(
    #         "testSelenium@test.test"
    #     )
    #     self.browser.find_element_by_id("passwordLogin").send_keys("ferfqerqsfqezrf")
    #     self.browser.find_element_by_id("submitLogin").click()

    #     self.assertEqual(
    #         self.browser.find_element_by_id("alertErrorLogin").text,
    #         "Your email or password is incorrect. Please try again.",
    #     )
    
    # def test_right_login_selenium(self):
    #     self.browser.get(self.live_server_url + reverse("login"))
    #     self.browser.find_element_by_id("emailLogin").send_keys(
    #         "testSelenium@test.test"
    #     )
    #     self.browser.find_element_by_id("passwordLogin").send_keys("testPasswordSelenium")
    #     self.browser.find_element_by_id("submitLogin").click()

    #     self.assertEqual(
    #         self.browser.current_url,
    #         self.live_server_url + reverse("newwws_app:index")
    #     )
    
    # def test_wrong_register_selenium(self):
    #     self.browser.get(self.live_server_url + reverse('newwws_app:register'))
    #     self.browser.find_element_by_id('emailRegistration').send_keys(
    #         'testSelenium2@test.test'
    #     )
    #     self.browser.find_element_by_id('passwordRegistration').send_keys('azerty')
    #     self.browser.find_element_by_id('passwordConfirmationRegistration').send_keys('azert')
    #     self.browser.find_element_by_id('submitRegistration').click()

    #     time.sleep(1)
    #     self.assertEqual(
    #         self.browser.current_url,
    #         self.live_server_url + reverse('newwws_app:register')
    #     )
    #     self.assertEqual(
    #         self.browser.find_element_by_id('alertErrorRegistration').text,
    #         "The two password fields didn’t match."
    #     )
    
    # def test_right_register_selenium(self):
    #     self.browser.get(self.live_server_url + reverse('newwws_app:register'))
    #     self.browser.find_element_by_id('emailRegistration').send_keys(
    #         'testSelenium2@test.test'
    #     )
    #     self.browser.find_element_by_id('passwordRegistration').send_keys('azerty51')
    #     self.browser.find_element_by_id('passwordConfirmationRegistration').send_keys('azerty51')
    #     self.browser.find_element_by_id('submitRegistration').click()

    #     time.sleep(1)
    #     self.assertEqual(
    #         self.browser.current_url,
    #         self.live_server_url + reverse('newwws_app:index')
    #     )
    
    # def test_logout_register_selenium(self):
        
    #     self.browser.get(self.live_server_url + reverse("login"))
    #     self.browser.find_element_by_id("emailLogin").send_keys(
    #         "testSelenium@test.test"
    #     )
    #     self.browser.find_element_by_id("passwordLogin").send_keys("testPasswordSelenium")
    #     self.browser.find_element_by_id("submitLogin").click()

    #     self.browser.find_element_by_id("accountHeader").click()
    #     self.browser.find_element_by_id("logoutHeader").click()

    #     self.assertEqual(
    #         self.browser.current_url,
    #         self.live_server_url + reverse('logout')
    #     )
    
    # def test_login_required_selenium(self):
        
    #     self.browser.get(self.live_server_url + reverse("newwws_app:saved"))

    #     self.assertIn(
    #         self.live_server_url + reverse('login'),
    #         self.browser.current_url
    #     )
    #     self.assertEqual(
    #         self.browser.find_element_by_id('alertAccessNotPermitted').text,
    #         "Connect to your account or Create one to see more."
    #     )

    #CANT SAVE element

# class DailyNewsPathSelenium(StaticLiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Chrome(
#             executable_path=str(
#                 settings.BASE_DIR / "webdrivers" / "chromedriver"
#             ),
#             options=chrome_options,
#         )
#         self.browser.implicitly_wait(10)
#         self.browser.maximize_window()

#         CustomUser.objects.create_user(
#             email="testSelenium3@test.test", password="testPasswordSelenium3"
#         )

#         self.browser.get(self.live_server_url + reverse("login"))
#         self.browser.find_element_by_id("emailLogin").send_keys(
#             "testSelenium3@test.test"
#         )
#         self.browser.find_element_by_id("passwordLogin").send_keys("testPasswordSelenium3")
#         self.browser.find_element_by_id("submitLogin").click()

#         Article.objects.create(title="Elon Musk first man on the sun ?")

#     def tearDown(self):
#         self.browser.close()

    # def test_index_search_daily_news_selenium(self):

    #     self.browser.get(self.live_server_url)

    #     self.browser.find_element_by_id("querySearch").send_keys("Musk")
    #     self.browser.find_element_by_id("queryDailyNews").click()
    #     self.browser.find_element_by_id("querySubmit").click()

    #     time.sleep(1)

    #     self.assertEqual(
    #         self.live_server_url + reverse('newwws_app:daily-news'),
    #         self.browser.current_url
    #     )
    
    # def test_daily_news_search_selenium(self):

    #     self.browser.get(self.live_server_url + reverse('newwws_app:daily_news'))

    #     self.browser.find_element_by_id("querySearch").clear()
    #     self.browser.find_element_by_id("querySearch").send_keys("China")
    #     self.browser.find_element_by_id("queryCategory").send_keys("Business")
    #     self.browser.find_element_by_id("queryLanguage").send_keys("English")
    #     self.browser.find_element_by_id("querySubmit").click()

    #     time.sleep(1)

    #     self.assertEqual(
    #         self.live_server_url + reverse('newwws_app:daily_news'),
    #         self.browser.current_url
    #     )

    # def test_daily_news_url_selenium(self):

    #     self.browser.get(self.live_server_url + reverse('newwws_app:daily_news'))
    #     self.browser.find_element_by_class_name("urlArticle").click()

    # def test_daily_news_save_selenium(self):

    #     self.browser.get(self.live_server_url + reverse('newwws_app:daily_news'))
    #     self.browser.find_element_by_class_name("btn-save-article-1").click()

    #     time.sleep(1)

    #     self.assertEqual(
    #         self.browser.find_element_by_class_name("alert-saved-daily-news").text,
    #         'Article saved ! Now available in my-news section.'
    #     )




# class NewsPathSelenium(StaticLiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Chrome(
#             executable_path=str(
#                 settings.BASE_DIR / "webdrivers" / "chromedriver"
#             ),
#             options=chrome_options,
#         )
#         self.browser.implicitly_wait(10)
#         self.browser.maximize_window()

#         user = CustomUser.objects.create_user(
#             email="testSelenium4@test.test", password="testPasswordSelenium4"
#         )
#         article = Article.objects.create(title="Elon Musk first man on the sun ?")
#         Saved.objects.create(article_id=article.id, user_id=user.id)

#         self.browser.get(self.live_server_url + reverse("login"))
#         self.browser.find_element_by_id("emailLogin").send_keys(
#             "testSelenium4@test.test"
#         )
#         self.browser.find_element_by_id("passwordLogin").send_keys("testPasswordSelenium4")
#         self.browser.find_element_by_id("submitLogin").click()

#     def tearDown(self):
#         self.browser.close()
    
    # def test_index_search_news_selenium(self):
        
    #     self.browser.get(self.live_server_url)

    #     self.browser.find_element_by_id("querySearch").send_keys("Musk")
    #     self.browser.find_element_by_id("querySubmit").click()

    #     time.sleep(1)

    #     self.assertEqual(
    #         self.live_server_url + reverse('newwws_app:news'),
    #         self.browser.current_url
    #     )

    # def test_news_search_selenium(self):

    #     self.browser.get(self.live_server_url + reverse('newwws_app:news'))

    #     self.browser.find_element_by_id("querySearch").clear()
    #     self.browser.find_element_by_id("querySearch").send_keys("China")
    #     self.browser.find_element_by_id("querySortBy").send_keys("Elevancy")
    #     self.browser.find_element_by_id("queryLanguage").send_keys("English")
    #     self.browser.find_element_by_id("querySubmit").click()

    #     time.sleep(1)

    #     self.assertEqual(
    #         self.live_server_url + reverse('newwws_app:news'),
    #         self.browser.current_url
    #     )

    # def test_news_url_selenium(self):

    #     self.browser.get(self.live_server_url + reverse('newwws_app:daily_news'))
    #     self.browser.find_element_by_class_name("urlArticle").click()

    # def test_daily_news_save_selenium(self):

    #     self.browser.get(self.live_server_url + reverse('newwws_app:news'))
    #     self.browser.find_element_by_class_name("btn-save-article-1").click()

    #     time.sleep(1)

    #     self.assertEqual(
    #         self.browser.find_element_by_class_name("alert-saved-daily-news").text,
    #         'Article saved ! Now available in my-news section.'
    #     )


class MyNewsPathSelenium(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            executable_path=str(
                settings.BASE_DIR / "webdrivers" / "chromedriver"
            ),
            options=chrome_options,
        )
        self.browser.implicitly_wait(10)
        self.browser.maximize_window()

        user = CustomUser.objects.create_user(
            email="testSelenium5@test.test", password="testPasswordSelenium5"
        )
        article = Article.objects.create(title="Elon Musk first man on the sun ?", published_at="2021-04-03")
        article = Article.objects.create(title="Lens première équipe à gagner la LDC !", published_at="2021-04-04")
        article = Article.objects.create(title="Article test 3", published_at="2021-04-05")
        article = Article.objects.create(title="Article test 4", published_at="2021-04-06")
        article = Article.objects.create(title="Article test 5", published_at="2021-04-07")
        article = Article.objects.create(title="Article test 6", published_at="2021-04-08")
        article = Article.objects.create(title="Article test 7", published_at="2021-04-09")
        article = Article.objects.create(title="Article test 8", published_at="2021-04-10")
        article = Article.objects.create(title="Article test 9", published_at="2021-04-11")
        article = Article.objects.create(title="Article test 10", published_at="2021-04-12")
        article = Article.objects.create(title="Article test 11", published_at="2021-04-13")
        article = Article.objects.create(title="Article test 12", published_at="2021-04-14")
        article = Article.objects.create(title="Article test 13", published_at="2021-04-15")
        

        Saved.objects.create(article_id=article.id, user_id=user.id)

        self.browser.get(self.live_server_url + reverse("login"))
        self.browser.find_element_by_id("emailLogin").send_keys(
            "testSelenium5@test.test"
        )
        self.browser.find_element_by_id("passwordLogin").send_keys("testPasswordSelenium5")
        self.browser.find_element_by_id("submitLogin").click()

    def tearDown(self):
        self.browser.close()