from django.shortcuts import render
from .models import Workers,Orders
from .serializer import WorkersSerializers,OrdersSerializers
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class getWorker(generics.ListCreateAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializers
    permission_classes = (IsAuthenticated,)

class DetailDestroyUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers
