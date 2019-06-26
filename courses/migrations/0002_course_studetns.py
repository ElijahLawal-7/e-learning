# Generated by Django 2.2.2 on 2019-06-25 10:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='studetns',
            field=models.ManyToManyField(blank=True, related_name='course_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]