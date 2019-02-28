#!/usr/bin/python
# -*- coding:utf-8 -*-

from django.views.generic.base import View

from .models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过Django的view实现商品列表页
        :param request:
        :return:
        """
        # json_list = []
        goods = Goods.objects.all()[:15]
        # for good in goods:
        #     json_dict = dict()
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        from django.http import HttpResponse, JsonResponse
        from django.core import serializers
        import json
        json_data = serializers.serialize('json', goods)
        json_list = json.loads(json_data)

        # return HttpResponse(json.dumps(json_list), content_type='application/json')
        return JsonResponse(json_list, safe=False)
