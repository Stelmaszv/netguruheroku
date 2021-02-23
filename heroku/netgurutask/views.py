from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Car,Rate
from heroku.serializers import user_serializer
from .serializers import CarSerializer,CarSerializerPopular,CarDeleteSerializer,RateSerializer
from rest_framework.views import  APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views.generic.edit import DeleteView
import json
# Create your views here.

class API_prototype_get(APIView):

    queryset=[]

    def get(self, request, *args, **kwargs):
        self.set_query_set(request)
        return self.API_get(request)

    def API_get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def set_query_set(self,request):
        pass

class API_prototype(APIView):

    many=True

    def set_query_set(self,request):
        pass

    def post(self, request, *args, **kwargs):
        self.set_query_set(request)
        serializer = self.serializer_class(data=request.data,many=False)
        if serializer.is_valid():
            serializer.save()
            return self.return_respanse(request)
        return self.return_respanse(request)

    def _API_get(self, request, *args, **kwargs):
        self.auth=False
        serializer = self.serializer_class(self.queryset, many=self.many)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        self.permission_classes = []
        self.set_query_set(request)
        return self.return_respanse(request)

    def return_respanse(self,request):
        return self._API_get(request)

    def _return_pages_json(self,request):
        pages={
            'valid':self._validPages(self.num_pages,int(self.page)),
            'max': self.num_pages,
            'page':int(self.page)
        }
        return Response(data=pages, status=status.HTTP_200_OK)

class CarList (API_prototype):
    serializer_class = CarSerializer

    def set_query_set(self, request):
        self.queryset = Car.objects.order_by('-avg_rating')

class CarListPupular (API_prototype):
    serializer_class = CarSerializerPopular

    def set_query_set(self, request):
        self.queryset = Car.objects.order_by('-rates_number')

class AddRate(API_prototype):
    serializer_class = RateSerializer

    def set_query_set(self, request):
        self.queryset = Rate.objects.all()


class CarDelete(API_prototype_get):
    many=False
    serializer_class = CarDeleteSerializer

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def delete(self, request, *args, **kwargs):
        car = self.get_object(self.kwargs.get("id"))
        car.delete()
        mess =str(car)+' Has been removed from data base'
        return Response(data=mess, status=status.HTTP_200_OK)



