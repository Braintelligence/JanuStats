# Basic modules
from django.db import models

# Validators
from django.core.validators import MinValueValidator, MaxValueValidator

# Translation modules
from django.utils.translation import ugettext_lazy as _


# TimeSeries models

class TimeSeries(models.Model):
    """
    Abstract class for time series without the time boundary.
    """

    year = models.IntegerField(blank=False, validators=[MinValueValidator(1000), MaxValueValidator(9999)],
                               help_text=_("Veröffentlichungsjahr des Datums, erlaubt: (1000-9999)."))
    quarter = models.IntegerField(blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)],
                                  help_text=_("Veröffentlichungsquartal des Datums, erlaubt: (1-4)."))



# Value models and managers
class StatValueManager(models.Manager):
    """
    Manager for StatValue objects, mainly for creation of instances.
    """

    def create_statvalue(self, name, value, seasonally_adjusted, real_or_nominal, vintage):
        statvalue = self.create(
            name=name,
            value=value,
            seasonally_adjusted=seasonally_adjusted,
            real_or_nominal=real_or_nominal,
            vintage=vintage)
        return statvalue


class StatValue(models.Model):
    """
    Class for depiction of basic statistical values.
    """

    name = models.CharField(
        blank=False, max_length=100, help_text=_("Name des statistischen Datums, maximal 100 Zeichen."))
    value = models.DecimalField(
        blank=False, max_digits=36,
        decimal_places=18,
        help_text=_("Wert des statistischen Datums, maximal 36 Ziffern mit maximal 18 Dezimalstellen."))
    seasonally_adjusted = models.BooleanField(
        blank=True, help_text=_("Angabe, ob das statistische Datum saisonbereinigt ist."))
    real_or_nominal = models.BooleanField(
        blank=True,
        help_text=_("0/False bedeutet nominal, 1/True bedeutet real, Null bedeutet weder noch."))
    vintage = models.CharField(
        blank=True, max_length=100, help_text=_("Vintage des Datums, maximal 100 Zeichen."))

    objects = StatValueManager()

    class Meta:
        abstract = True

class StatValueTimeSeries(StatValue):
    """
    Statistical values for TimeSeries objects.
    """

    statobject = models.ForeignKey(TimeSeries, on_delete=models.CASCADE)
