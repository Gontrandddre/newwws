#!/usr/bin/python3
# -*- coding: Utf-8 -*

from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views


app_name = "newwws_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("news", views.news, name="news"),
    path("article", views.article, name="article"),
    path("saved", views.saved, name="saved"),
    path("articles", views.articles, name="articles"),
    path("account", views.account, name="account"),
    path("legal-notice", TemplateView.as_view(template_name="newwws_app/legal_notices.html"), name="legal-notice"),
]

urlpatterns += [
    path("registration", views.register, name="register"),
]