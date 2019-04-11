# Generated by Django 2.1.1 on 2019-04-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='name')),
                ('description', models.TextField(blank=True, default='', verbose_name='description')),
                ('parent', models.IntegerField(default=0, verbose_name='父节点')),
            ],
        ),
    ]
