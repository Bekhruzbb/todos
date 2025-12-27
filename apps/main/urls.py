from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_home_page, name='home'),
    path('contacts/', views.show_contacts_page, name='contacts'),
    path('todos/', views.show_todos_page, name='todos'),
    path('about/', views.show_about_page, name='about'),
    path('tasks_todo/categories/<slug:category_slug>/', views.show_todos_by_category, name='todos-category'),
    path('tasks_todo/<slug:todo_slug>/', views.show_todos_by_detail, name='todo-detail')
]
