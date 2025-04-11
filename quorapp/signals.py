from django.dispatch import receiver
from datetime import datetime
from django.db.models.signals import post_save, pre_save
from .models import Question, Answer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json
@receiver(post_save, sender=Question)
def post_save_question(sender, created, instance, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "live_data_live_data" ,
            {
                'type': 'send_live_data' ,
                'message': json.dumps(data)
            }
        )