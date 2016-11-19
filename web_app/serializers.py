from rest_framework import serializers

from web_app.models import Location, Posts


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'address', 'active', 'date_started', 'completion_time', 'active_users')


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('location', 'username', 'date_posted', 'message')
