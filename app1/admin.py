from django.contrib import admin
from app1.models import course
 
# Register your models here.

@admin.register(course)
class courseadmin(admin.ModelAdmin):
    list_display = ['cname','fee','dur','trainer']