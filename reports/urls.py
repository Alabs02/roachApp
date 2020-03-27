from django.contrib import admin
from django.urls import re_path
from django.urls import path, include
from . import views

app_name = "reports"

urlpatterns = [
    path('', views.report_list, name="list"),
    path('create/', views.report_create, name="create"),
    re_path(r'^(?P<slug>[\w-]+)/', views.report_detail, name="detail"),
]

