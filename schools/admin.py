from django.contrib import admin

# Register your models here.

from .models import School
from .models import Comment


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author']