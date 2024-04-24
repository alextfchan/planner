# Generated by Django 5.0.1 on 2024-04-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hours', models.IntegerField(default=0)),
                ('minutes', models.IntegerField(default=25)),
                ('seconds', models.IntegerField(default=0)),
            ],
        ),
    ]
