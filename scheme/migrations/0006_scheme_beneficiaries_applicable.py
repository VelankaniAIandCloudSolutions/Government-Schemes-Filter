# Generated by Django 3.2.5 on 2023-05-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheme', '0005_auto_20230502_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheme',
            name='beneficiaries_applicable',
            field=models.ManyToManyField(blank=True, null=True, to='scheme.Beneficiary'),
        ),
    ]
