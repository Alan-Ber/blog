# Generated by Django 4.2.7 on 2023-11-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("control_blog", "0002_entrada_fecha_publicacion"),
    ]

    operations = [
        migrations.AddField(
            model_name="entrada",
            name="autor",
            field=models.CharField(default=None, max_length=64),
        ),
    ]