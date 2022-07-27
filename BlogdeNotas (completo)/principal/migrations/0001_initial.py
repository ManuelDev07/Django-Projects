# Generated by Django 4.0.4 on 2022-05-12 22:37

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='nombre de usuario')),
                ('first_name', models.CharField(max_length=150, verbose_name='Primer Nombre')),
                ('email', models.EmailField(max_length=250, verbose_name='correo')),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Título')),
                ('author', models.CharField(default='null', max_length=80, verbose_name='Autor')),
                ('content', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Nota',
                'verbose_name_plural': 'Notas',
            },
        ),
    ]
