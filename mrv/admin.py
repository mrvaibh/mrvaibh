from django.contrib import admin
from .models import Fact, Service

# Register your models here.

admin.site.register(Fact)
admin.site.register(Service)