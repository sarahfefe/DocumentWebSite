from django.shortcuts import render
from docType.models import DocType
from django.shortcuts import render
from rest_framework import viewsets
from .models import DocType
from .serializers import DocTypeSerializer

class DocTypeView(viewsets.ModelViewSet):
    queryset= DocType.objects.all()
    serializer_class= DocTypeSerializer
    
    def remove(self, request, pk):
        doctype_object = get_object_or_404(DocType.objects.all(), pk=pk)
        docType_object.remove()
        return Response({"message": "docType with id `{}` has been deleted.".format(pk)},status=204)