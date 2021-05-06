#!/usr/bin/python3
# -*- coding: Utf-8 -*

from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views


app_name = "newwws_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("daily-news", views.daily_news, name="daily_news"),
    re_path(r"^article/(?P<id_article>[^/]+)$", views.article, name="article"),
    path("my-news", views.saved, name="saved"),
    path("news", views.news, name="news"),
    path("account", views.account, name="account"),
    path("legal-notice", TemplateView.as_view(template_name="newwws_app/legal_notices.html"), name="legal-notice"),
]

urlpatterns += [
    path("registration", views.register, name="register"),
]