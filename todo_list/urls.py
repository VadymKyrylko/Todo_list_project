from django.urls import path

from todo_list.views import (
    index,
    TagListView,
    task_toggle_status,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)
urlpatterns = [
    path(
        "",
        index,
        name="index"
    ),
    path(
        "tag/",
        TagListView.as_view(),
        name="tags"
    ),
    path("tasks/<int:pk>/toggle-status/",
         task_toggle_status,
         name="task-toggle-status"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]

app_name = "todo_list"
