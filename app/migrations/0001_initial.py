# Generated by Django 4.2.3 on 2023-08-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xusers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Role', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]
