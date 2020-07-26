from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django_bleach.models import BleachField
from django.utils.translation import gettext as _
from uuid import uuid4

def generateUUID():
    return str(uuid4())

##### User Model > Default to Email for Username #####
class user_model(AbstractUser):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    uuid = models.UUIDField(default=generateUUID, unique=True)
    is_administrator = models.BooleanField('Administrator status', default=False)
    username = models.CharField('username', max_length=150, unique=True)
    email = models.EmailField('email address', unique=True, max_length = 255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

##### Default Model > Added UUID #####
class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    uuid = models.UUIDField(default=generateUUID, unique=True, editable=False)

    class Meta:
        abstract = True
    
##### Tickets > Grab from Default Model Above #####
class ticket(BaseModel):    
    k_created_by = models.ForeignKey("backend.user_model", null=True, on_delete=models.SET_NULL)

    subject = models.CharField(max_length=360)
    content = BleachField()
    type = models.CharField(max_length=120)
    status = models.CharField(default="Open", max_length=120)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    
class ticket_message(BaseModel):
    k_ticket = models.ForeignKey("backend.ticket", on_delete=models.CASCADE)
    k_created_by = models.ForeignKey("backend.user_model", null=True, on_delete=models.SET_NULL)

    message = BleachField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)