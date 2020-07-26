from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from import_export.admin import ImportExportMixin
from . import models

##### Users #####
class user_modelCreateForm(UserCreationForm):
    class Meta:
        model = models.user_model
        fields = "__all__"

class user_modelChangeForm(UserChangeForm):
    class Meta:
        model = models.user_model
        fields = "__all__"
        
class user_modelAdmin(ImportExportMixin, UserAdmin):
    add_form = user_modelCreateForm
    form = user_modelChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'password', 'date_joined', 'last_login')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_administrator')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_administrator')}
        ),
    )
    list_display = [
        "email",
        "is_staff",
        "is_administrator",
    ]

##### Ticket #####
class ticketAdminForm(forms.ModelForm):
    class Meta:
        model = models.ticket
        fields = "__all__"
class ticketAdmin(ImportExportMixin, admin.ModelAdmin):
    form = ticketAdminForm
    list_display = [
        "subject",
        "content",
        "type",
        "status",
        "created",
        "last_updated",
        "k_created_by",
    ]
    
class ticket_messageAdminForm(forms.ModelForm):
    class Meta:
        model = models.ticket_message
        fields = "__all__"
class ticket_messageAdmin(ImportExportMixin, admin.ModelAdmin):
    form = ticket_messageAdminForm
    list_display = [
        "message",
        "created",
        "last_updated",
        "k_created_by",
        "k_ticket",
    ]
    
##### Register #####
admin.site.register(models.user_model, user_modelAdmin)

admin.site.register(models.ticket_message, ticket_messageAdmin)
admin.site.register(models.ticket, ticketAdmin)