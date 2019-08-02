# Generated by Django 2.2.2 on 2019-08-02 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0002_auto_20190801_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='role',
        ),
        migrations.AddField(
            model_name='team',
            name='pending_points',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='program_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255, null=True)),
                ('is_line_manager', models.BooleanField(default=False)),
                ('is_program_manager', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]