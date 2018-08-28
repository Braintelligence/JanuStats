from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from janustats.stats.models import StatData, StatValue


@admin.register(StatData)
class StatData(admin.ModelAdmin):
    pass

@admin.register(StatValue)
class StatValue(admin.ModelAdmin):
    pass
