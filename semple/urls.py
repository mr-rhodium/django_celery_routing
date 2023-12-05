from django.urls import path
from semple.views import TaskView, SortedView, SendEmailView

urlpatterns = [
    path("task/", TaskView.as_view(), name="task"),
    path("sorted/", SortedView.as_view(), name="sorted"),
    path("send_email/", SendEmailView.as_view(), name="send_email"),
]