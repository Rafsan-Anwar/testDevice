from rest_framework import serializers

from .models import Testdb1, Testdb2

class Testdb1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Testdb1
        fields = '__all__'


class Testdb2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Testdb2
        fields = '__all__'


class Dictionary(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary


class JsonSerializer(serializers.Serializer):
    response = serializers.DictField(child=serializers.CharField())