# Generated by Django 4.0.4 on 2022-04-13 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('num', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='addres',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testuser.addres'),
        ),
    ]
