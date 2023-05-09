from django.shortcuts import render
from rest_framework import viewsets
from api.models import Comapany
from api.serializers import CompanySerializer
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Comapany.objects.all()
    serializer_class = CompanySerializer
    