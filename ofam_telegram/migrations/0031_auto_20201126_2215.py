# Generated by Django 3.1.1 on 2020-11-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofam_telegram', '0030_auto_20201126_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='exhibitionmodel',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mainmenubuttonmodel',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='shopproductmodel',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='visitmodel',
            name='description',
            field=models.TextField(),
        ),
    ]
