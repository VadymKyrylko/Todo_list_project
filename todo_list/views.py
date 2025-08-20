from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST

from todo_list.forms import TaskForm
from todo_list.models import Task, Tag


def index(request):
    tasks = Task.objects.all()

    context = {"tasks": tasks}
    return render(request, "todo_list/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "todo_list/tag_list.html"
    paginate_by = 5


@require_POST
def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return redirect("todo_list:index")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:index")
    template_name = "todo_list/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:index")
    template_name = "todo_list/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:index")
    template_name = "todo_list/task_confirm_delete.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tags")
    template_name = "todo_list/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tags")
    template_name = "todo_list/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tags")
    template_name = "todo_list/tag_confirm_delete.html"
