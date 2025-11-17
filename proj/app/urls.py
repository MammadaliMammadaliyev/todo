from django.urls import path
from . import views


urlpatterns = [
    path(
        "tasks/", 
        views.TaskAPIView.as_view(), 
        name="task-list"
    ),
]