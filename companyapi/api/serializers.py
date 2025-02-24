from rest_framework import serializers
from .models import Company
# create serializers here
#The Companyserializer converts Company model instances into JSON format and vice versa.
class Companyserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"