from django.contrib import admin

from .models import Buy

class BuyModelAdmin(admin.ModelAdmin):
    list_display = ['owner_name', 'address', 'timestamp']
    list_filter = ['zipcode', 'state', 'city']
    search_fields = ['owner_name', 'address']

    class Meta:
        model = Buy

admin.site.register(Buy, BuyModelAdmin)

