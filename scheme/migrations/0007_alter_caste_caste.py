# Generated by Django 3.2.5 on 2023-05-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheme', '0006_scheme_beneficiaries_applicable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caste',
            name='caste',
            field=models.CharField(choices=[('General', 'General'), ('SC', 'SC'), ('ST', 'ST'), ('OBC', 'OBC'), ('EWS', 'EWS')], max_length=100),
        ),
    ]
