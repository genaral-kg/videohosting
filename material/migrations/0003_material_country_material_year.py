# Generated by Django 4.1.1 on 2022-10-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_category_image_material_image_material_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='country',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='material',
            name='year',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
