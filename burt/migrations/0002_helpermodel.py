# Generated by Django 4.1.1 on 2022-09-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelperModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_new', models.IntegerField(default=0)),
                ('test_me', models.IntegerField(default=0)),
                ('study', models.IntegerField(default=0)),
                ('fixed', models.IntegerField(default=0)),
                ('closed', models.IntegerField(default=0)),
                ('multistate', models.IntegerField(default=0)),
            ],
        ),
    ]
