# Generated by Django 4.2.4 on 2023-08-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='isbn',
            field=models.CharField(help_text='ingrese el ISBN del libro', max_length=100),
        ),
    ]
