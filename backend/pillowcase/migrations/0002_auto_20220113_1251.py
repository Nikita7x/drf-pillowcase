# Generated by Django 3.2.6 on 2022-01-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pillowcase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='images',
            name='picture',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='images',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
