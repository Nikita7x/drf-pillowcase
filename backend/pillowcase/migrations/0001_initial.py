# Generated by Django 3.2.6 on 2022-01-12 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('url', models.URLField(null=True)),
                ('picture', models.FilePathField(verbose_name='/Users/Xiaomi/Documents/backend_task-master/backend/media')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('parent_picture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pillowcase.images')),
            ],
        ),
    ]
