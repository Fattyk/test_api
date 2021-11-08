from .models import TestModel
from .serializers import TestSerializers
from rest_framework import generics, permissions, viewsets

class TestListCreate(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializers
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TestViewset(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
