# Generated by Django 4.0.4 on 2022-06-10 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productov2',
            fields=[
                ('iid', models.IntegerField(primary_key=True, serialize=False, verbose_name='codigo de barra')),
                ('nombre', models.CharField(max_length=60)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
