from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeSlider, Category, ToDo, Comment
# Create your views here.


def show_home_page(request):
    slides = HomeSlider.objects.all()
    todos = ToDo.objects.all()
    context = {
        'slides': slides,
        'todos': todos
    }
    return render(request, 'main/index.html', context)


def show_contacts_page(request):
    return render(request, 'main/contacts.html')


def show_todos_page(request):
    todos = ToDo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'main/tasks_todo.html', context)


def show_about_page(request):
    return render(request, 'main/about.html')


def show_todos_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    todos = ToDo.objects.filter(category=category)
    context = {
        'category': category,
        'todos': todos
    }
    return render(request, 'main/tasks_todo.html', context)


def show_todos_by_detail(request, todo_slug):
    todo = ToDo.objects.get(slug=todo_slug)
    if request.method=='POST':
        comment_text = request.POST.get('comment')
    context = {
        'todo': todo
    }
    return render(request, 'main/tasks.html', context)
