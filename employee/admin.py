from django.contrib import admin
from .models import Employee, Address, AddressType


admin.site.register(Employee)
admin.site.register(Address)
admin.site.register(AddressType)
