# Generated by Django 4.2.7 on 2023-12-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0020_aboutus_linkeding_aboutus_nombre_aboutus_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciob',
            name='categoria',
            field=models.IntegerField(choices=[[900, 'Diseño Web'], [901, 'Front End'], [902, 'Back End'], [903, 'Logo & Marca'], [904, 'Diseño de Apps'], [905, 'Arte'], [906, 'Ilustraciones'], [907, 'Diseño UX'], [908, 'Gaming'], [909, 'Diseño 3D'], [910, 'Marketing Digital'], [911, 'Soporte'], [912, 'Programacion y Tecnologia'], [913, 'Datos'], [914, 'Fotografia y Edicion'], [915, 'Videos y Edición']]),
        ),
    ]