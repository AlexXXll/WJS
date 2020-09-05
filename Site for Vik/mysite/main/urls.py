# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:06:32 2020

@author: admin
"""

from django.urls import path
from . import views

urlpatterns = {
    path('', views.index),
    path('about-us', views.about),

}

