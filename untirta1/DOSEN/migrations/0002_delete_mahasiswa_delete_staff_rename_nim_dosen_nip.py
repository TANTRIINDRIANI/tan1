# Generated by Django 4.1.2 on 2022-11-02 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOSEN', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MAHASISWA',
        ),
        migrations.DeleteModel(
            name='STAFF',
        ),
        migrations.RenameField(
            model_name='dosen',
            old_name='NIM',
            new_name='NIP',
        ),
    ]
