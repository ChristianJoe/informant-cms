# Generated by Django 2.0.5 on 2018-06-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0026_report_short_headline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='short_headline',
            field=models.CharField(help_text='Dies ist der Text, der auf dem Auswahl-Button für diese Nachricht angezeigt wird. Bitte möglichst kurzes Schlagwort eintragen.', max_length=20, verbose_name='Button-Text'),
        ),
    ]