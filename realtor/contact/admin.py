from django.contrib import admin
from .models import ContactModel

class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone_number', 'firstName', 'timestamp', ]
    list_filter = ['email', 'phone_number', 'firstName']
    search_fields = ['email', 'phone_number', 'firstName', 'lastName']

    class Meta:
        model = ContactModel

admin.site.register(ContactModel, ContactAdmin)
