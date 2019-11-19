# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-09 11:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BE1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('sub1', models.IntegerField(default=0)),
                ('sub2', models.IntegerField(default=0)),
                ('sub3', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'BE1',
            },
        ),
        migrations.CreateModel(
            name='BE2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('sub4', models.IntegerField(default=0)),
                ('sub5', models.IntegerField(default=0)),
                ('sub6', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'BE2',
            },
        ),
        migrations.CreateModel(
            name='dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sunday', models.DateField(default='2018-09-09')),
                ('new_week', models.DateField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Dates',
            },
        ),
        migrations.CreateModel(
            name='FE1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('physics_m', models.IntegerField(default=0)),
                ('chemistry_m', models.IntegerField(default=0)),
                ('maths_tu', models.IntegerField(default=0)),
                ('physics_tu', models.IntegerField(default=0)),
                ('physics_w', models.IntegerField(default=0)),
                ('chemistry_w', models.IntegerField(default=0)),
                ('chemistry_th', models.IntegerField(default=0)),
                ('maths_th', models.IntegerField(default=0)),
                ('chemistry_f', models.IntegerField(default=0)),
                ('physics_f', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'FE1',
            },
        ),
        migrations.CreateModel(
            name='SE1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('deld', models.IntegerField(default=0)),
                ('coa', models.IntegerField(default=0)),
                ('mp', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'SE1',
            },
        ),
        migrations.CreateModel(
            name='SE2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('pai', models.IntegerField(default=0)),
                ('psop', models.IntegerField(default=0)),
                ('fds', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'SE2',
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('enroll_no', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('division', models.CharField(choices=[('SE2', 'SE2'), ('SE1', 'SE1'), ('TE2', 'TE2'), ('TE1', 'TE1'), ('FE1', 'FE1'), ('BE2', 'BE2'), ('BE1', 'BE1')], max_length=50)),
                ('gender', models.CharField(choices=[('male', 'male'), ('other', 'other'), ('female', 'female')], max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('admission_date', models.DateTimeField()),
                ('attendance', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TE1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('toc', models.IntegerField(default=0)),
                ('sdl', models.IntegerField(default=0)),
                ('os', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
            options={
                'verbose_name_plural': 'TE1',
            },
        ),
        migrations.CreateModel(
            name='TE2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('hci', models.IntegerField(default=0)),
                ('dbms', models.IntegerField(default=0)),
                ('sepm', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
            options={
                'verbose_name_plural': 'TE2',
            },
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll_no', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('division', models.CharField(choices=[('SE2', 'SE2'), ('SE1', 'SE1'), ('TE2', 'TE2'), ('TE1', 'TE1'), ('FE1', 'FE1'), ('BE2', 'BE2'), ('BE1', 'BE1')], max_length=50)),
                ('subject', models.CharField(choices=[('chemistry', 'Chemistry'), ('coa', 'C.O.A'), ('dbms', 'D.B.M.S'), ('deld', 'D.E.L.D'), ('fds', 'F.D.S'), ('hci', 'H.C.I'), ('maths', 'Maths'), ('mp', 'M.P'), ('os', 'O.S'), ('physics', 'Physics'), ('psoop', 'PSOOP'), ('sdl', 'S.D.L'), ('sepm', 'S.E.P.M'), ('sub1', 'Sub1'), ('sub2', 'Sub2'), ('sub3', 'Sub3'), ('sub4', 'Sub4'), ('sub5', 'Sub5'), ('sub6', 'Sub6'), ('toc', 'T.O.C')], max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='se2',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
        migrations.AddField(
            model_name='se1',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
        migrations.AddField(
            model_name='fe1',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
        migrations.AddField(
            model_name='be2',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
        migrations.AddField(
            model_name='be1',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
    ]
