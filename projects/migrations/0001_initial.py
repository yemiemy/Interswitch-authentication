# Generated by Django 2.2.2 on 2019-08-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('attachment', models.FileField(null=True, upload_to='attachments/%Y/%m/%d/')),
                ('point', models.IntegerField(null=True)),
                ('startdate', models.DateTimeField(null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
