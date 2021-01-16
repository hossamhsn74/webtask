# from rest_framework.decorators import api_view, permission_classes
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, authentication
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from ..models import Book
from . import serializers

class HelloView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class BookListView(generics.ListAPIView):
    """
    View to list all books in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

  


class BookCreateView(generics.CreateAPIView):
    """
    View to add a new book.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

    def create(self, request, *args, **kwargs):
        super(BookCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully added to books",
                    "result": request.data}
        return Response(response)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    lookup_field = 'title'
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


    def retrieve(self, request, *args, **kwargs):
        super(BookDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(BookDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(BookDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)
