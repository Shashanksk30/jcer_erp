# Generated by Django 3.2.9 on 2022-05-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes_id', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
