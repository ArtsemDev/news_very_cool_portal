import logging
from time import sleep

from not_clean.celery import app


@app.task(name='newsletter')
def send_message(email: str):
    sleep(5)
    logging.info(f'email to {email} send successfully')


@app.task
def schedule_task():
    logging.info('SCHEDULE TASK')
