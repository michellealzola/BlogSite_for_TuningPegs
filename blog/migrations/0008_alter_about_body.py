# Generated by Django 4.1.4 on 2022-12-23 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_about_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='body',
            field=models.TextField(),
        ),
    ]
