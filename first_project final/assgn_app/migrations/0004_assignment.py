# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assgn_app', '0003_professorlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assgn_file', models.FileField(upload_to='uploaded_files/file1')),
                ('prof_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assgn_app.Professor')),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assgn_app.Student')),
            ],
        ),
    ]