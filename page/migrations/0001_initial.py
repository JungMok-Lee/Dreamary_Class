# Generated by Django 3.1 on 2020-08-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
