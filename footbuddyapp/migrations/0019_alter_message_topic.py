# Generated by Django 4.1.5 on 2023-03-07 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('footbuddyapp', '0018_remove_message_room_topic_message_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_message', to='footbuddyapp.topic'),
        ),
    ]
