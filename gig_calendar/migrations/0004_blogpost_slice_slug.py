# Generated by Django 2.2 on 2019-10-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_calendar', '0003_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slice_slug',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
