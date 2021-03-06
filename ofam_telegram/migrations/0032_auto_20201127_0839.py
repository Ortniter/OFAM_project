# Generated by Django 3.1.1 on 2020-11-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofam_telegram', '0031_auto_20201126_2215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventmodel',
            options={'verbose_name': 'Event'},
        ),
        migrations.AlterModelOptions(
            name='shopproductmodel',
            options={'verbose_name': 'Shop Product'},
        ),
        migrations.AlterModelOptions(
            name='telegramuser',
            options={'ordering': ['the_order'], 'verbose_name': 'Telegram User'},
        ),
        migrations.AlterModelOptions(
            name='visitmodel',
            options={'verbose_name': 'Visit'},
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AddField(
            model_name='exhibitionmodel',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AddField(
            model_name='mainmenubuttonmodel',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AddField(
            model_name='visitmodel',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
    ]
