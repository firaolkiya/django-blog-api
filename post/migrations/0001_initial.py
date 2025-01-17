# Generated by Django 5.1.2 on 2024-10-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
