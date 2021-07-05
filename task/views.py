from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from django.contrib.auth.views import *
from task.forms import *
from task.models import *
# Create your views here.


# handles user login
class UserLoginView(LoginView):
	template_name = 'task/login.html'
	success_url = reverse_lazy('home')
	redirect_authenticated_user = True

# handles user registration
def registration(request):
	form = RegisterForm()
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	context = {
		'form':form
	}
	return render(request, 'task/register.html', context)


# lists the task objects
class TaskListView(LoginRequiredMixin, ListView):
	model = Task
	context_object_name = 'tasks'
	template_name = 'task/home.html'
	ordering = ('complete', )

	def get_context_data(self, **kwargs):
		context_object_name  = super().get_context_data(**kwargs)
		context_object_name['tasks'] = context_object_name['tasks'].filter(user=self.request.user)
		context_object_name['count'] = context_object_name['tasks'].filter(complete=False).count()
		return context_object_name


# handles the task object detail
class TaskDetailView(DetailView):
	model = Task
	context_object_name = 'tasks'
	template_name = 'task/task_detail.html'


# handles task creation and assigns the currently logged in user as the user.id in the Task
class CreateTaskView(LoginRequiredMixin, CreateView):
	model = Task
	form_class = TaskCreationForm
	template_name = 'task/create_task.html'
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CreateTaskView, self).form_valid(form)


# updates task objects
class UpdateTaskView(LoginRequiredMixin, UpdateView):
	model = Task
	template_name = 'task/update_task.html'
	form_class = TaskCreationForm
	success_url = reverse_lazy('home')


# deletes task objects
class DeleteTaskView(LoginRequiredMixin, DeleteView):
	model = Task
	template_name = 'task/delete_task.html'
	success_url = reverse_lazy('home')