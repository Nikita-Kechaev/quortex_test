from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Singer
from .serializers import SingerSerializer


class SingerViewSet(viewsets.GenericViewSet):

    def get_queryset(self):
        queryset = Singer.objects.all()
        return queryset

    def get_serializer_class(self,):
        return SingerSerializer

    def list(self, requset):
        serializer = self.get_serializer_class()
        qs = self.get_queryset()
        serializer = serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
