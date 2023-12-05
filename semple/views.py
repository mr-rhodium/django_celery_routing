from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from semple.tasks import semple_task, semple_task_sorted, semple_task_send_email


class TaskView(View):
    def get(self, request, *args, **kwargs):
        result = semple_task.delay(1, 2).get()
        return HttpResponse(f"result: {result}")
    
class SortedView(View):
    def get(self, request, *args, **kwargs):
        result = semple_task_sorted.delay([5, 7, 1, 3, 2]).get()
        return HttpResponse(f"result: {'.'.join(result)}")

class SendEmailView(View):
    def get(self, request, *args, **kwargs):
        result = semple_task_send_email.delay()
        return HttpResponse(f"result: {result.get()}")