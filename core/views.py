from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Testdb1, Testdb2
from .serializers import Testdb1Serializer, Testdb2Serializer


def index(request):
    test_db1_qs = Testdb1.objects.all()
    test_db2_qs = Testdb2.objects.all()
    context = {
        'test_db1_qs': test_db1_qs,
        'test_db2_qs': test_db2_qs
    }
    return render(request, 'index.html', context)


class TestApi1(APIView):
    def get_object(self, pk):
        try:
            return Testdb1.objects.get(pk=pk)
        except Testdb1.DoesNotExist:
            return Http404

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        queryset = None
        pk = kwargs.get('pk', None)
        if pk:
            queryset = self.get_object(pk)
            serializer = Testdb1Serializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            queryset = Testdb1.objects.all()
            serializer = Testdb1Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    @method_decorator(csrf_exempt)
    def post(self, request):
        serializer = Testdb1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestApi2(APIView):
    def get_object(self, pk):
        try:
            return Testdb2.objects.get(pk=pk)
        except Testdb2.DoesNotExist:
            return Http404

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        queryset = None
        pk = kwargs.get('pk', None)
        if pk:
            queryset = self.get_object(pk)
            serializer = Testdb2Serializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            queryset = Testdb2.objects.all()
            serializer = Testdb2Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @method_decorator(csrf_exempt)
    def post(self, request):
        serializer = Testdb2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)