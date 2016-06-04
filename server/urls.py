"""passerelle_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from rest_framework.routers import DefaultRouter
from passerelle.views import RoomViewSet, BookingViewSet, ClosureViewSet

router = DefaultRouter()
router.register(prefix='Rooms', viewset=RoomViewSet)
router.register(prefix='Bookings', viewset=BookingViewSet)
router.register(prefix='Closures', viewset=ClosureViewSet)

urlpatterns = router.urls