from rest_framework import viewsets
from passerelle.models import Room, Booking, Closure
from passerelle.serializers import RoomSerializer, BookingSerializer, ClosureSerializer


class RoomViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Room objects """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Booking objects """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ClosureViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Closure objects """
    queryset = Closure.objects.all()
    serializer_class = ClosureSerializer
