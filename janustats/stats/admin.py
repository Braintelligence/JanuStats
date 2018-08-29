from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from janustats.stats.models import StatSource, StatValueType, StatValue

# InlineAdmins
class StatValueInline(admin.TabularInline):
    model = StatValue

# ModelAdmins
@admin.register(StatSource)
class StatSourceAdmin(admin.ModelAdmin):

    def get_statvalues(self, obj):
        return list(obj.statvalues.all())

    list_display = ('name', 'publisher', 'verdate', 'get_statvalues')
    list_display_links = ('get_statvalues',)

    inlines = [
        StatValueInline,
    ]


@admin.register(StatValueType)
class StatValueTypeAdmin(admin.ModelAdmin):

    def get_stattypes(self, obj):
        return list(obj.stattypes.all())

    list_display = ('name', 'slug', 'get_stattypes')

    inlines = [
        StatValueInline,
    ]





@admin.register(StatValue)
class StatValueAdmin(admin.ModelAdmin):

    list_display = (
        'value',
        'seasonally_adjusted',
        'real_nominal',
        'country',
        'year',
        'get_timesubtype',
        'vintage',
    )

    list_select_related = True
