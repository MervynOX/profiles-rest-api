from django.shortcuts import render

#importing from django REST framework
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#for filter function
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
#for login API
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
#for profile feed API
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated              # only allowed register and logged in user to view it

from . import serializers
from . import models
from . import permissions

# the application logic behind our API
class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        #it is a dictionary converted to JSON, which is then outputted to the screen
        return Response({'message':'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our nane"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            first_name = serializer.data.get('first_name')
            message = 'Hello {0}'.format(first_name) #in accordance to list numbering indexx 0, 1, 2...
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        #logic to perform action here

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Users actions (list, create, retrieve, update, partial_update)',
            'Automatically maps URLs using Routers',
            'Provides more functionality with less code'
        ]

        #it is a dictionary converted to JSON, which is then outputted to the screen
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    #like HTTP POST
    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            first_name = serializer.data.get('first_name')
            message = 'Hello {0}'.format(first_name) #in accordance to list numbering indexx 0, 1, 2...
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # pk means primary key, to identify the object
    def retrieve(self, reuqest, pk=None):
        """Handles getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of the object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object"""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) # having coma to ensure that it is a tuple
    permission_classes = (permissions.UpdateOwnProfile,) # add multi auth classes to a particular viewset
    filter_backends = (filters.SearchFilter,) # allow user to use the search filter backend
    search_fields = ('first_name', 'email',) # by using the name and email to filter

class LoginViewSet(viewsets.ViewSet):
    """Check email and password and return an auth token."""

    serializer_class = AuthTokenSerializer

    #HTTP POST to the viewset
    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated) # IsAuthenticatedOrReadOnly means user who are not logged in can also view it

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile = self.request.user)

class EventProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating events."""

    #serializer_class = serializers.EventCreationSerializer
    #authentication_classes = (TokenAuthentication,)
    serializer_class=serializers.EventCreationSerializer
    queryset = models.EventProfile.objects.all()
    #permission_classes = (permissions.UpdateOwnEvent, IsAuthenticated)


    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile = self.request.user)


class EventCreationViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating events."""

    authentication_classes = (TokenAuthentication,)
    queryset = ''
    serializer_class = serializers.EventCreationSerializer
    permission_classes = (permissions.UpdateOwnEvent, IsAuthenticated) # IsAuthenticatedOrReadOnly means user who are not logged in can also view it

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile = self.request.user.__str__)

class CommunityViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating community."""

    authentication_classes = (TokenAuthentication,)
    serializer_class=serializers.CommunityCreationSerializer
    queryset = models.CommunityProfile.objects.all()
    permission_classes = (permissions.UpdateOwnCommunity, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile = self.request.user)


class CommunityCreationViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating community."""

    authentication_classes = (TokenAuthentication,)
    queryset = ''
    serializer_class = serializers.CommunityCreationSerializer
    permission_classes = (permissions.UpdateOwnCommunity, IsAuthenticated) # IsAuthenticatedOrReadOnly means user who are not logged in can also view it

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile = self.request.user)
