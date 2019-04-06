from django.contrib import admin
from .models import Provider

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('username', 'company_name', 'email_address', 'registration_no')
    list_filter = ('company_name', 'website', 'email_address', 'telephone')
    search_fields = ('username', 'company_name')

admin.site.register(Provider, ProviderAdmin)