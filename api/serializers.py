from rest_framework import serializers
from .models import Room

#ROOM
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room 
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')


#CREATE ROOM
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')

#UPDATE ROOM
class UpdateRoomSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])
    
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip', 'code')