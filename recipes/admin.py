from django.contrib import admin
from .models import Category

class categoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, categoryAdmin)
