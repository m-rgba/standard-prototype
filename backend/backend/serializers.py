from rest_framework import serializers
from . import models

##### Ticket Serializer #####
class ticketSerializer(serializers.ModelSerializer):
    # Added the linked username to API response
    k_username = serializers.CharField(source='k_created_by.email', read_only=True)
    k_created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = models.ticket
        fields = '__all__'
        # Don't want all fields > this is how you show certain fields
        # fields = [
        #     "subject",
        #     "last_updated",
        # ]
        
class ticket_messageSerializer(serializers.ModelSerializer):
    k_username = serializers.CharField(source='k_created_by.email', read_only=True)
    k_created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = models.ticket_message
        fields = '__all__'

##### User Serializer #####
# My Profile
class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.user_model
        fields = ('id', 'email', 'is_administrator')
        read_only_fields = ('is_administrator',)

# All Users
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.user_model
        fields = ('id', 'email', 'username', 'is_active', 'is_administrator', 'date_joined')