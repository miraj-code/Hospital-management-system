# Generated by Django 4.0.4 on 2022-05-03 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auser', '0007_payment_user_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='payment',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]