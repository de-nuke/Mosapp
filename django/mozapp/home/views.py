from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MainImageSerializer


class MainImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = (BasicAuthentication, )

    def post(self, request, *args, **kwargs):
        image_serializer = MainImageSerializer(data=request.data)

        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

