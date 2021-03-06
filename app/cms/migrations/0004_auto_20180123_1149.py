# Generated by Django 2.0.1 on 2018-01-23 11:49

from django.db import migrations, models
import django.db.models.deletion


def delete_topic(apps, schema_editor):
    Report = apps.get_model('cms', 'Report')
    for report in Report.objects.all():
        report.topic = None
        report.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20180123_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Thema',
                'verbose_name_plural': 'Themen',
            },
        ),
        migrations.RunPython(delete_topic),
        migrations.AlterField(
            model_name='report',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports', to='cms.Topic', verbose_name='Thema'),
        ),
    ]
