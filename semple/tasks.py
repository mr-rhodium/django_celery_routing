from celery import current_app 


@current_app.task
def semple_task(first: int, second: int):
    return first + second


@current_app.task
def semple_task_sorted(info: list):
    return info.sort()


@current_app.task
def semple_task_send_email():
    return "send email"
