# Generated by Django 3.1.1 on 2020-10-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofam_telegram', '0003_auto_20201028_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('callback_data', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Event',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='mainmenubuttonmodel',
            options={'ordering': ['id'], 'verbose_name': 'Main menu button'},
        ),
    ]
