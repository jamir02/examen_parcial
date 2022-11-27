# Generated by Django 4.1.3 on 2022-11-27 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="tarea",
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
                ("titulo", models.CharField(default="", max_length=64)),
                ("descripcion", models.CharField(default="", max_length=100)),
                ("fecha_creacion", models.CharField(default="", max_length=64)),
                ("fecha_entrega", models.CharField(default="", max_length=64)),
                ("usuario_designado", models.CharField(default="", max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="usuario",
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
                ("nombre", models.CharField(default="", max_length=64)),
                ("apellido", models.CharField(default="", max_length=64)),
                ("codigo_usuario", models.CharField(default="", max_length=64)),
                ("clave", models.CharField(default="", max_length=64)),
            ],
        ),
    ]
