# Generated by Django 4.1.1 on 2022-10-18 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0004_remove_material_country'),
        ('favorites', '0002_remove_favorite_owner_alter_favorite_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='materials',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='material.material'),
        ),
    ]