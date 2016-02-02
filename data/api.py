from rest_framework import filters, serializers, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

import django_filters
from django.shortcuts import get_object_or_404

from .models import Cause


class CauseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cause
        fields = (
            'pk',
            'year',
            'ethnicity',
            'sex',
            'cause_of_death',
            'count',
            'percent',
        )


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CauseViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('count', 'year', 'sex', 'percent')
    serializer_class = CauseSerializer
    queryset = Cause.objects.all()
    pagination_class = StandardResultsSetPagination
    ordering_fields = ('count', 'year', 'sex', 'percent')
    ordering = ('year',)
