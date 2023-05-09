from rest_framework import serializers
from api.models import Comapany
# Create serilizers
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Metta:
        model: Comapany
        feilds = "__all__"