#!/usr/bin/python
# -*- coding:utf-8 -*-

from rest_framework import serializers

from .models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
        category = CategorySerializer()

        class Meta:
            model = Goods
            fields = '__all__'
            # fields = ('name', 'click_num', 'fav_num', 'goods_desc', 'add_time', 'goods_front_image')
