from django.conf.urls import url

from . import views_task, views_parcel

app_name = 'api'

urlpatterns = [
    url(r'^task/$', views_task.TaskList.as_view()),
    url(r'^parcel/$', views_parcel.ParcelList.as_view()),
]
