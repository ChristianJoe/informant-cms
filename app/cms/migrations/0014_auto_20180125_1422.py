# Generated by Django 2.0.1 on 2018-01-25 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20180125_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='tags',
            field=models.ManyToManyField(related_name='items', to='cms.ReportTag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='wiki',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='wikis', to='cms.ReportTag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='wikifragment',
            name='link_wiki',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', related_query_name='+', to='cms.Wiki', verbose_name='Link Einzelheit'),
        ),
    ]
