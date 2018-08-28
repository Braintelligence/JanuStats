from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from janustats.stats.models import TimeSeries, StatValueTimeSeries


@admin.register(TimeSeries)
class TimeSeries(admin.ModelAdmin):
    pass

@admin.register(StatValueTimeSeries)
class StatValueTimeSeries(admin.ModelAdmin):
    pass
