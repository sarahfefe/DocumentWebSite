from django.shortcuts import render
from confidentiality.models import Confidentiality
from django.shortcuts import render
from rest_framework import viewsets
from .models import Confidentiality
from .serializers import ConfidentialitySerializer


class ConfidentialityView(viewsets.ModelViewSet):
    queryset= Confidentiality.objects.all()
    serializer_class= ConfidentialitySerializer

    def delete(self, request, pk):
        confidentiality_object = get_object_or_404(Confidentiality.objects.all(), pk=pk)
        confidentiality_object.delete()
        return Response({"message": "confidentiality with id `{}` has been deleted.".format(pk)},status=204)
