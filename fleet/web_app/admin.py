from django.contrib import admin
from .models import client_data
from .models import fleet_data
from .models import fleet_location

# Register your models here.

admin.site.register(client_data)
admin.site.register(fleet_data)
admin.site.register(fleet_location)
