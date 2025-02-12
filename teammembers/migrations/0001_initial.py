# Generated by Django 5.0.6 on 2024-05-12 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='teammembers/')),
            ],
        ),
    ]
