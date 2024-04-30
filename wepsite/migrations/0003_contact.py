# Generated by Django 5.0.3 on 2024-04-25 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wepsite', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('Subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
    ]