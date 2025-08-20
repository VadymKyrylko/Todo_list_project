from django.urls import path

from todo_list.views import (
    index,
    TagListView,
)
urlpatterns = [
    path("", index, name="index"),
    path("tag/", TagListView.as_view(), name="tags"),
]

app_name = "todo_list"