from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display =[
        'from_date',
        'to_date',
        'kattalar',
        'bolalar',
        'xonalar',
        'checkbox'

    ]
    list_editable = ['checkbox']