from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:list')
    success_message = 'Task created successfully!'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'
    context_object_name = 'task'


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:list')
    success_message = 'Task updated successfully!'


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('todo:list')
    success_message = 'Task deleted successfully!'