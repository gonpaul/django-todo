from django.urls import path

from . import views

app_name = "todo"

urlpatterns = [
    # path("", views.ArticleListView.as_view(), name="list"),
    # path("<int:pk>/", views.ArticleDetailView.as_view(), name="detail"),
    path("", views.TaskListView.as_view(), name="list"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="detail"),
    path("create/", views.TaskCreateView.as_view(), name="create"),
]

