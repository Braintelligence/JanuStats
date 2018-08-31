# Generated by Django 2.0.8 on 2018-08-31 07:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Name der Wertesammlung, maximal 300 Zeichen.', max_length=300)),
                ('comment', models.TextField(blank=True, help_text='Kommentar zur Wertesammlung.')),
            ],
        ),
        migrations.CreateModel(
            name='StatSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name der Vintage-Quelle, maximal 300 Zeichen.', max_length=300)),
                ('publisher', models.CharField(help_text='Name des Herausgebers, maximal 100 Zeichen.', max_length=100)),
                ('verdate', models.DateField(blank=True, help_text='Formatierte Datumsangabe der Vintage-Veröffentlichung.')),
            ],
        ),
        migrations.CreateModel(
            name='StatValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=18, help_text='Wert des statistischen Datums, maximal 36 Ziffern mit maximal 18 Dezimalstellen.', max_digits=36)),
                ('seasonally_adjusted', models.CharField(choices=[('sa', 'Saisonbereinigt'), ('ns', 'Nicht saisonbereinigt'), ('na', 'Keine Angabe')], help_text='Angabe, ob das statistische Datum saisonbereinigt ist.', max_length=2)),
                ('real_nominal', models.CharField(choices=[('no', 'Nominal'), ('re', 'Real'), ('na', 'Keine Angabe')], help_text='Auswahl ob der Wert real oder nominal ist, bzw. keine Angabe möglich ist.', max_length=2)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('year', models.IntegerField(help_text='Jahr des Datums, erlaubt: (1000-9999).', validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)])),
                ('semester', models.IntegerField(blank=True, help_text='Semester des Datums, erlaubt: (1-2).', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('quarter', models.IntegerField(blank=True, help_text='Quartal des Datums, erlaubt: (1-4).', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('month', models.IntegerField(blank=True, help_text='Monat des Datums, erlaubt: (1-12).', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
            ],
        ),
        migrations.CreateModel(
            name='StatValueType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name des statistischen Datums, maximal 100 Zeichen.', max_length=100)),
                ('slug', models.CharField(help_text='Kürzel des Datums, maximal 50 Zeichen und muss einzigartig sein.', max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='statvalue',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stattypes', to='stats.StatValueType'),
        ),
        migrations.AddField(
            model_name='statvalue',
            name='vintage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statvintages', to='stats.StatSource'),
        ),
    ]
