# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-25 03:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0004_remove_doctor_doc_compl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_entry_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'consulta',
            },
        ),
        migrations.CreateModel(
            name='Enfermeiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enf_name', models.CharField(max_length=50, verbose_name='Nome')),
            ],
            options={
                'db_table': 'enfermeiro',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'hospital',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_name', models.CharField(max_length=50, verbose_name='Nome')),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='Triagem',
            fields=[
                ('tri_consulta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='consulta.Consulta')),
                ('tri_pressao', models.CharField(max_length=6, verbose_name='Pressao')),
                ('tri_temperatura', models.FloatField(verbose_name='Temperatura')),
                ('tri_diabete', models.FloatField(verbose_name='Diabete')),
                ('tri_problem', models.CharField(max_length=256, verbose_name='Problema')),
                ('tri_manchester', models.CharField(max_length=50, verbose_name='Manchester')),
                ('tri_enfermeiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.Enfermeiro')),
            ],
            options={
                'db_table': 'triagem',
            },
        ),
        migrations.AddField(
            model_name='consulta',
            name='con_doctor_crm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Doctor'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='con_hospital_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.Hospital'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='con_patient_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.Patient'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='con_triagem_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.Triagem'),
        ),
    ]
