# Generated by Django 4.2.7 on 2023-11-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("control_blog", "0003_entrada_autor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entrada",
            name="autor",
            field=models.CharField(max_length=64, null=True),
        ),
    ]
