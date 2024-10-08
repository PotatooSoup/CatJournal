# Generated by Django 5.0.3 on 2024-04-04 21:20

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, help_text='日期'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='author',
            field=models.ForeignKey(help_text='观察员', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.author'),
        ),
    ]
