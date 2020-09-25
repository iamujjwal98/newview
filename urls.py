# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:46:50 2020

@author: HP
"""


from django.urls import path, include
from holidays.views import bankHeaderList, exHeaderList

urlpatterns = [
    path('bankholiday', bankHeaderList.as_view()),
    path('exholiday', exHeaderList.as_view()),
    
]