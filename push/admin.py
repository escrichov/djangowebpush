from django.contrib import admin

# Register your models here.
from .models import SubscriptionInfo

class SubscriptionInfoAdmin(admin.ModelAdmin):
    list_display = ("browser", )

admin.site.register(SubscriptionInfo, SubscriptionInfoAdmin)