from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework import mixins, generics, viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import GoodsSerializer
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods


class GoodsResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 40


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'shop_price')
