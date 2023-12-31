# Generated by Django 4.2.5 on 2023-09-22 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='example@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default='a', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='password212', max_length=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='surname',
            field=models.CharField(default='b', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default='ab', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='selectedMenu',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.menu'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
