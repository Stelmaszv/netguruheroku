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

class APIPrototypeGet(APIView):

    def get(self, request, *args, **kwargs):
        return self.api_get(request)

    def api_get(self, request, *args, **kwargs):

        serializer = self.serializer_class(self.queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class APIPrototype(APIView):

    many     = True
    order_by = ''

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data,many=False)
        if serializer.is_valid():
            serializer.save()
            return self.api_get(request)
        return self.api_get(request)

    def api_get(self, request, *args, **kwargs):

        self.auth=False
        serializer = self.serializer_class(self.queryset, many=self.many)
        if len(self.order_by):
            list = sorted(serializer.data, key=lambda tup: tup[self.order_by],reverse=True)
        else:
            list= serializer.data
        return Response(data=list, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):

        return self.api_get(request)

class CarList (APIPrototype):

    serializer_class  = CarSerializer
    queryset          = Car.objects
    order_by          = 'avg_rating'

class CarListPupular (APIPrototype):

    serializer_class = CarSerializerPopular
    queryset         = Car.objects
    order_by         = 'rates_number'

class AddRate(APIPrototype):

    serializer_class = RateSerializer
    queryset=  Rate.objects

class CarDelete(APIPrototypeGet):

    many             = False
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



