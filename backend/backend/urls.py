from django.urls import path, include
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register("ticket_message", api.ticket_messageViewSet)
router.register("ticket", api.ticketViewSet)
router.register("users", api.userViewSet)
router.register("profile", api.my_profileViewSet)

urlpatterns = (
    path("", include(router.urls)),
)