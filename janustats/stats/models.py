# Basic modules
from django.db import models

# Validators
from django.core.validators import MinValueValidator, MaxValueValidator

# Translation modules
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext_lazy as __


# Statistical models

class StatSource(models.Model):
    """
    Generic class for statistical data sources.
    """

    name = models.CharField(blank=False, max_length=300, help_text=_("Name der Vintage-Quelle, maximal 300 Zeichen."))
    publisher = models.CharField(blank=False, max_length=100, help_text=_("Name des Herausgebers, maximal 100 Zeichen."))
    verdate = models.DateField(blank=True, help_text=_('Formatierte Datumsangabe der Vintage-Veröffentlichung.'))

    def __str__(self):
        return self.name + '_' + str(self.verdate)


# Value models and managers
class StatValueType(models.Model):
    """
    Store different types of statistical values.
    """

    name = models.CharField(
        blank=False, max_length=100, help_text=_("Name des statistischen Datums, maximal 100 Zeichen."))
    slug = models.CharField(blank=False, unique=True, max_length=50,
                            help_text=_("Kürzel des Datums, maximal 50 Zeichen und muss einzigartig sein."))

    def __str__(self):
        return self.slug

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

    # Choices
    ## Tell if seasonally adjusted or not or N/A
    SA_CHOICES = (
        ('sa', _('Saisonbereinigt')),
        ('ns', _('Nicht saisonbereinigt')),
        ('na', _('Keine Angabe'))
    )
    ## Tell if the statistical value is real, nominal or N/A
    REAL_NOMINAL_CHOICES = (
        ('no', _('Nominal')),
        ('re', _('Real')),
        ('na', _('Keine Angabe'))
    )

    # ForeignKeys
    type = models.ForeignKey(StatValueType, blank=False,  on_delete=models.CASCADE, related_name='stattypes')
    vintage = models.ForeignKey(StatSource, blank=False, on_delete=models.CASCADE, related_name='statvintages')

    # Fields
    value = models.DecimalField(
        blank=False, max_digits=36,
        decimal_places=18,
        help_text=_("Wert des statistischen Datums, maximal 36 Ziffern mit maximal 18 Dezimalstellen."))
    seasonally_adjusted = models.CharField(
        blank=False,
        choices=SA_CHOICES,
        max_length=2,
        help_text=_("Angabe, ob das statistische Datum saisonbereinigt ist."))
    real_nominal = models.CharField(
        blank=False,
        choices=REAL_NOMINAL_CHOICES,
        max_length=2,
        help_text=_("Auswahl ob der Wert real oder nominal ist, bzw. keine Angabe möglich ist."))
    country = models.CharField(blank=False, max_length=100, help_text=_("Land des Datums, maximal 100 Zeichen."))
    ## TimeFields
    year = models.IntegerField(blank=False, validators=[MinValueValidator(1000), MaxValueValidator(9999)],
                               help_text=_("Jahr des Datums, erlaubt: (1000-9999)."))
    semester = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(2)],
                               help_text=_("Semester des Datums, erlaubt: (1-2)."))
    quarter = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(4)],
                                  help_text=_("Quartal des Datums, erlaubt: (1-4)."))
    month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)],
                               help_text=_("Monat des Datums, erlaubt: (1-12)."))

    # HelperFunctions
    def get_timesubtype(self):
        if self.semester:
            return str(self.semester) + str(_('. Semester'))
        if self.quarter:
            return str(self.quarter) + str(_('. Quartal'))
        if self.month:
            return str(self.month) + str(_('. Monat'))

    def __str__(self):
        return str(self.year) + '_' + self.get_timesubtype() \
               + '_' + str(self.type) + '_' + str(self.value)

    # Manager
    objects = StatValueManager()
