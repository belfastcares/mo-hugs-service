from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from web_app.serializers import LocationSerializer, PostsSerializer, PostSerializerCreate
from .models import Location, Posts


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def process_timeouts():
    locations = Location.objects.all()
    for location in locations:
        location.handle_timeout()


@api_view(['GET'])
def location_list(request):
    """
    List all locations
    """
    process_timeouts()
    if request.method == 'GET':
        locations = Location.objects.all()
        if locations.count() == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def start_event(request, location_id):
    """
    Start_event at location with ID
    """
    process_timeouts()
    if request.method == 'GET':
        if Location.objects.filter(pk=location_id).exists():
            location = Location.objects.get(pk=location_id)
            location.start_event()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def checkin_user(request, location_id):
    """
    Checkin user at location with ID
    """
    process_timeouts()
    if request.method == 'GET':
        if Location.objects.filter(pk=location_id).exists():
            location = Location.objects.get(pk=location_id)
            if location.is_active():
                location.add_user()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def checkout_user(request, location_id):
    """
    Checkout user at location with ID
    """
    process_timeouts()
    if request.method == 'GET':
        if Location.objects.filter(pk=location_id).exists():
            location = Location.objects.get(pk=location_id)
            if location.is_active():
                location.remove_user()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def posts(request, location_id):
    """
    Add or return posts at location with ID
    """
    process_timeouts()
    if not Location.objects.filter(pk=location_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        posts = Posts.objects.filter(location_id=location_id)
        if posts.count() == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializerCreate(data=request.data, context={'location_id': location_id})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


