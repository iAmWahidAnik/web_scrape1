# Generated by Django 4.1.3 on 2022-11-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chaldal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chaldal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='TestProduct',
        ),
    ]