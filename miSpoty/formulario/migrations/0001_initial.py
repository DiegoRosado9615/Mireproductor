# Generated by Django 3.0.3 on 2020-03-27 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrearArtista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('imagen', models.ImageField(default='gallery/static/images/no-img.jpg', upload_to='gallery')),
            ],
        ),
    ]
