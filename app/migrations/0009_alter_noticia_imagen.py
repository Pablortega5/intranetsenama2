# Generated by Django 4.0.2 on 2023-11-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_noticia_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(default='app/static/app/img/logo.png', upload_to='noticias'),
        ),
    ]
