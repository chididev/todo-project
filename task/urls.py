from django.urls import path
from task import views
from task.views import *

urlpatterns=[
	# handles user authentication that is login, logout and registration
	path('login/', UserLoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
	path('register/', views.registration, name='register'),

	# handles page navigations and CRUD functionality
	path('', TaskListView.as_view(), name='home'),
	path('create-task/', CreateTaskView.as_view(), name='create_task'),
	path('task-detail/<pk>', TaskDetailView.as_view(), name='task_detail'),
	path('update-task/<pk>', UpdateTaskView.as_view(), name='update_task'),
	path('delete-task/<pk>', DeleteTaskView.as_view(), name='delete_task'),
]