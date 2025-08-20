from django.shortcuts import render
from django.views import generic

from todo_list.models import Task, Tag


def index(request):
    tasks = Task.objects.all()

    context = {"tasks": tasks}
    return render(request, "todo_list/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "todo_list/tag_list.html"
    paginate_by = 10
