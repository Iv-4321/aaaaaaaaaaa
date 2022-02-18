import fitz as fitz
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer


def parce_pdf(test):
    doc = fitz.open(test)  # open document
    pixel = doc[0]  # page pdf
    pix = pixel.get_pixmap()  # render page to an image
    pix.save("media/page.png")  # store image as a PNG
    print(doc.metadata)


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        # test = request.data['file'].content_type
        test = request.data['file']
        # print(request.data.get)
        print(test)
        print(request.accepted_media_type)

        parce_pdf(test)
        print(file_serializer)
        # print(test)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
