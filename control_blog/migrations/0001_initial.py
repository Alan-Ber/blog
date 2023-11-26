# Generated by Django 4.2.7 on 2023-11-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Entrada",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=64)),
                ("subtitulo", models.CharField(max_length=100)),
                ("cuerpo", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Etiqueta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_tag", models.CharField(max_length=256)),
                ("info_tag", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("apellido", models.CharField(max_length=256)),
                ("nombre", models.CharField(max_length=256)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("fecha_nacimiento", models.DateField(null=True)),
            ],
        ),
    ]
