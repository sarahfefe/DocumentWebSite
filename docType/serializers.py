from rest_framework import serializers
from .models import DocType

class DocTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= DocType
        fields = ( 'id', 'name' ,  'total_docs')