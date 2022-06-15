from email.headerregistry import Address
from django.contrib import admin
from testuser.models import User, Address

# Register your models here.
admin.site.register(User)
admin.site.register(Address)
