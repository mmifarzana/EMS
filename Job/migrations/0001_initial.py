# Generated by Django 3.2.5 on 2021-12-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applyparticipent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circular_No', models.IntegerField()),
                ('full_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('job_type', models.CharField(max_length=50)),
                ('field', models.CharField(max_length=50)),
                ('related_exprience', models.CharField(max_length=500)),
                ('job_reason', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='participent_profiles/')),
                ('cv', models.FileField(upload_to='participent_cv/')),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Circular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circular_No', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('company_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('field', models.CharField(max_length=50)),
                ('job_type', models.CharField(max_length=50)),
                ('requirement', models.TextField(max_length=500)),
                ('exprience', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('last_date_apply', models.DateField()),
                ('action', models.CharField(max_length=50)),
            ],
        ),
    ]
