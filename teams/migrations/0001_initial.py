# Generated by Django 2.2.2 on 2019-08-01 17:56

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
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('total_points', models.IntegerField(default=0, null=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='members')),
                ('program_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]