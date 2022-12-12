# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.home import views as display

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('measure', views.all_measure, name="list-measure"),
    path('ajax/getMeasure', views.getMeasure,name="getMeasure"),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
