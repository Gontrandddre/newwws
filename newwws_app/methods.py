#!/usr/bin/python3
# -*- coding: Utf-8 -*

from .constantes import NO_CHARS_LIST, STOP_WORDS
from unidecode import unidecode
from newsapi import NewsApiClient
import requests

# Init NewsApi
newsapiAccess = NewsApiClient(api_key='6883ebc956424214a2aa0f47258925f9')


class ParseMode():
    """
    Allow us to manage input user.
    """

    def __init__(self, user_input):
        """
        XXX
        """

        self.user_input = user_input
        self.user_input_cleaned = None

    def emptyInput(self):
        """
        Allows us to generate warning when input user is empty.
        """    

    def cleanInput(self):
        """
        Allows us to cleaning input user.
        """

        input_lower = self.user_input.lower()
        input_withoutCharsSpe = input_lower.translate(
            {ord(c): " " for c in NO_CHARS_LIST}
        )
        input_no_accent = unidecode(input_withoutCharsSpe)
        input_split = input_no_accent.split()

        for element in input_split:
            if element in STOP_WORDS:
                input_split.remove(element)

        self.user_input_cleaned = " ".join(input_split)

        return self.user_input_cleaned


class RequestApiEverything():

    def __init__(self, q=None, qintitle=None, sources=None, domains=None, language=None, from_param=None, to=None):
        self.q = q
        self.qintitle = qintitle
        self.sources = sources
        self.domains = domains
        self.language = language
        self.from_param = from_param
        self.to = to

    def articles(self):
        articles = newsapiAccess.get_everything(q=self.q,
                                                qintitle=self.qintitle,
                                                sources=self.sources,
                                                domains=self.domains,
                                                language=self.language,
                                                from_param=self.from_param,
                                                to=self.to)
        return articles


class RequestApiHeadlines():

    def __init__(self, country=None, category=None, q=None, language=None):
        self.country = country
        self.category = category
        self.q = q
        self.language = language

    def news(self):
        top_headlines = newsapiAccess.get_top_headlines(q=self.q,
                                                  category=self.category,
                                                  language=self.language,
                                                  country=self.country)
        return top_headlines

        
# training
# articles = RequestApiEverything(q="bitcoin")
# print(articles.articles())

# news = RequestApiHeadlines(language="fr")
# print(news.news())