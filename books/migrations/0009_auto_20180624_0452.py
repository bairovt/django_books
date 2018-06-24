# Generated by Django 2.0.6 on 2018-06-24 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20180624_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerbook',
            name='paidSum',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerbook',
            name='received_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerbook',
            name='status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]