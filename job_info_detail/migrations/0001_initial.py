# Generated by Django 3.2.5 on 2022-03-14 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=20)),
                ('matching_grade', models.CharField(max_length=10)),
                ('salary', models.IntegerField(default=0)),
                ('working_pattern', models.CharField(max_length=20)),
                ('requirement', models.CharField(max_length=200)),
                ('twojob_possiblity', models.CharField(max_length=10)),
                ('mainly_do', models.CharField(max_length=1000)),
                ('welfare', models.CharField(max_length=500)),
                ('working_env', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='dupl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=10)),
                ('salaryy', models.IntegerField(default=0)),
                ('pattern', models.CharField(max_length=20)),
                ('requirementt', models.CharField(max_length=200)),
                ('possiblity', models.CharField(max_length=10)),
                ('detaill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_info_detail.job_detail')),
            ],
        ),
    ]