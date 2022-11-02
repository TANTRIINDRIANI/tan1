# Generated by Django 4.1.2 on 2022-11-02 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mahasiswa', '0002_delete_dosen_delete_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAKULTAS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_FAKULTAS', models.CharField(max_length=9)),
                ('nama', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='prodi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Prodi', models.CharField(max_length=9)),
                ('nama', models.CharField(max_length=9)),
            ],
        ),
        migrations.RemoveField(
            model_name='mahasiswa',
            name='FAKULTAS',
        ),
        migrations.RemoveField(
            model_name='mahasiswa',
            name='PRODI',
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='FAKULTAS_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Mahasiswa.fakultas'),
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='PRODI_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Mahasiswa.prodi'),
        ),
    ]
