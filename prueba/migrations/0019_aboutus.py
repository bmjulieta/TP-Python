# Generated by Django 4.2.7 on 2023-12-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0018_alter_serviciob_servicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/aboutus/')),
            ],
        ),
    ]
