# Generated by Django 4.2.7 on 2023-12-10 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0022_metododepago_idservicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metododecobro',
            name='idMetod',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
