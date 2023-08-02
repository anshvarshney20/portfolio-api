from . models import *
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields='__all__'

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = certificates
        fields='__all__'