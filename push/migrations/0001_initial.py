# Generated by Django 2.2.1 on 2019-05-03 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser', models.CharField(max_length=100)),
                ('endpoint', models.URLField(max_length=255)),
                ('auth', models.CharField(max_length=100)),
                ('p256dh', models.CharField(max_length=100)),
            ],
        ),
    ]
