# Generated by Django 4.2.6 on 2023-11-23 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_dishes_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishes',
            name='link',
            field=models.CharField(default='lik', max_length=50),
        ),
    ]
