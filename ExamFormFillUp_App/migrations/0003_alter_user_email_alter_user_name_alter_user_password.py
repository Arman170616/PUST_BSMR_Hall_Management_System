# Generated by Django 4.0.3 on 2022-04-02 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamFormFillUp_App', '0002_alter_user_studentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
