from django.shortcuts import render, redirect
from .models import project
from .forms import ProjectForm

# CRUD - create, retrieve, update, delete, list


def project_list(request):
    projects = project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects.html", context)


def project_retrieve(request, pk):
    projectt = project.objects.get(id=pk)
    context = {
        "project": projectt
    }
    return render(request, "project.html", context)


def project_create(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "project_create.html", context)


def project_update(request, pk):
    projectt = project.objects.get(id=pk)
    form = ProjectForm(instance=projectt)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=projectt)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "project_update.html", context)


def project_delete(request, pk):
    projectt = project.objects.get(id=pk)
    projectt.delete()
    return redirect("/")
