# Generated by Django 4.2.1 on 2023-05-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('en instance', 'en instance'), ('non livré', 'non livré'), ('livré', 'livré')], max_length=200, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
