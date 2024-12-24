from django.contrib import admin
from app.models import ContactMessage
# Register your models here


@admin.register(ContactMessage)
class ContactMessageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email','subject','mobile_no', 'message']
