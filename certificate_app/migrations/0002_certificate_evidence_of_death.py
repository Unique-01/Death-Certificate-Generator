# Generated by Django 4.2.4 on 2023-08-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='evidence_of_death',
            field=models.FileField(null=True, upload_to='docs'),
        ),
    ]
