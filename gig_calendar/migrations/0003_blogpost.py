# Generated by Django 2.2 on 2019-09-05 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_calendar', '0002_auto_20190704_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
    ]
