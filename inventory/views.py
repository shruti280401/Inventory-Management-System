from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from .serializers import *
from django.http import Http404
from django.core.cache import cache
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Read, Update, Delete Item
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_object(self):
        item_id = self.kwargs['pk']
        cache_key = f'item_{item_id}'
        item = cache.get(cache_key)

        if not item:
            try:
                item = Item.objects.get(pk=item_id)
                cache.set(cache_key, item, timeout=60 * 5)  # Cache for 5 minutes
            except Item.DoesNotExist:
                raise Http404
        return item


    # GET request (Retrieve a single Item by ID)
    def get(self, request, *args, **kwargs):
        item = self.get_object()  # Retrieve the object using the primary key (pk)
        serializer = self.get_serializer(item)  # Serialize the object
        return Response(serializer.data)  # Return the serialized data as a response

    # PUT/PATCH request (Update the Item by ID)
    def put(self, request, *args, **kwargs):
        item = self.get_object()  # Retrieve the object using the primary key (pk)
        serializer = self.get_serializer(item, data=request.data)  # Validate the input data
        if serializer.is_valid():  # If the data is valid
            serializer.save()  # Save the updated object
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return the updated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid

    # DELETE request (Delete the Item by ID)
    def delete(self, request, *args, **kwargs):
        item = self.get_object()  # Retrieve the object using the primary key (pk)
        item.delete()  # Delete the object
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return a successful response with no content

# Create your views here.
