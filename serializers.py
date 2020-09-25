# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:46:30 2020

@author: HP
"""

from holidays.models import EX_hol, Bank_hol

from rest_framework import serializers

class bankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank_hol
        fields = ['h_type','h_name','h_date','sc_gp']
           
class exSerializer(serializers.ModelSerializer):
    class Meta:
        model = EX_hol
        fields = ['h_type','h_name','h_date','sc_gp']
