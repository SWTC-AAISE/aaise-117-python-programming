from django.shortcuts import redirect, render

from .forms import StudyTaskForm
from .models import StudyTask


def task_list(request):
    tasks = StudyTask.objects.order_by("course_name", "title")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def add_task(request):
    if request.method == "POST":
        form = StudyTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = StudyTaskForm()

    return render(request, "tasks/task_form.html", {"form": form})
