import random
import json

from asgiref.sync import async_to_sync
from apscheduler.schedulers.background import BackgroundScheduler
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()
MY_NUMBER = [1]


def job():
    global MY_NUMBER
    MY_NUMBER[0] = random.randint(100, 1000)
    async_to_sync(channel_layer.group_send)('gr_num',
                                            {
                                                'type': 'send_num',
                                                'message': str(MY_NUMBER[0])
                                            })


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', seconds=5)
    scheduler.start()
