from rest_framework import serializers
from passerelle.models import Room, Booking, Closure, ClosureRoom


class RoomSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Room model """
    class Meta:
        model = Room
        fields = ("name", "description", "price", "capacity")


class BookingSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Booking model """
    class Meta:
        model = Booking
        fields = (
            "room", "name", "email", "guests_number", "date_in", "date_out",
            "date_reservation", "status", "notes", "telephone", "channel"
        )


class ClosureSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Closure model """
    class Meta:
        model = Closure
        fields = ("label", "date_start", "date_end", "notes")

class ClosureRoomSerializer(serializers.ModelSerializer):
    """ Serializer to represent the ClosureRoom model """
    class Meta:
        model = ClosureRoom
        fields = ("room", "closure")
