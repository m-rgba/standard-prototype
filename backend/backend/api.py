from rest_framework.permissions import BasePermission
from rest_framework import viewsets, permissions
from . import serializers
from . import models

##### Custom Permissions #####
class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_administrator

##### Viewsets #####
# Uses base ID as the lookup from model
class BaseModelViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    
class ticketViewSet(BaseModelViewSet):
    queryset = models.ticket.objects.all()
    serializer_class = serializers.ticketSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ticket_messageViewSet(BaseModelViewSet):
    queryset = models.ticket_message.objects.all()
    serializer_class = serializers.ticket_messageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['k_ticket']

# Limits all users access => just app Administrators or Super Admins 
class userViewSet(BaseModelViewSet):
    queryset = models.user_model.objects.all()
    serializer_class = serializers.userSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdministrator|permissions.IsAdminUser]
    
# My Profile - filters data on myself
class my_profileViewSet(BaseModelViewSet):
    queryset = models.user_model.objects.all()
    serializer_class = serializers.profileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(email=self.request.user)
        return self.queryset