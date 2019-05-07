# Generated by Django 2.1 on 2019-04-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='children',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='_department_children_+', to='api.Department'),
        ),
    ]
