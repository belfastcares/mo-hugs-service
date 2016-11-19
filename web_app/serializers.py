from rest_framework import serializers

from web_app.models import Location, Posts


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'address', 'active', 'date_started', 'completion_time', 'active_users')

class PostSerializerCreate(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    date_posted = serializers.DateTimeField(required=False)
    message = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        new_post = Posts()
        new_post.username = validated_data.get('username')
        new_post.message = validated_data.get('message')
        new_post.location_id = self.context['location_id']
        new_post.save()
        return new_post


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('location', 'username', 'date_posted', 'message')
