# Generated by Django 4.2.7 on 2023-12-10 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0019_aboutus'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='linkedIng',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='nombre',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='rol',
            field=models.CharField(max_length=80, null=True),
        ),
    ]