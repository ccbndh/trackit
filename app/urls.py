from django.conf.urls import url

from . import views_task

app_name = 'api'

urlpatterns = [
    url(r'^task/$', views_task.TaskList.as_view()),
]
