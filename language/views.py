from django.shortcuts import render
from language.models import Language
from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset= Language.objects.all()
    serializer_class= LanguageSerializer
    def remove(self, request, pk):
        language_object = get_object_or_404(Language.objects.all(), pk=pk)
        language_object.remove()
        return Response({"message": "language with id `{}` has been deleted.".format(pk)},status=204)

