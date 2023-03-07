# Generated by Django 4.0.4 on 2022-04-25 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('footbuddyapp', '0005_remove_reply_message_message_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='reply',
        ),
        migrations.AddField(
            model_name='reply',
            name='message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='footbuddyapp.message'),
        ),
    ]