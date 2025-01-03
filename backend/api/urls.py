from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.TaskListCreate.as_view(), name="task-list"),
    path("task/delete/<int:pk>/", views.TaskDelete.as_view(), name="delete-task"),
    path("tasks/update/<int:pk>/", views.TaskUpdate.as_view(), name="update-task"),
    path("tasks/thismonth/", views.RetrieveMonthlyTasks.as_view(), name="monthly-tasks"),
    path("tasks/thisweek/", views.RetrieveWeeklyTasks.as_view(), name="weekly-tasks"),
    path("tasks/lastweek/", views.RetrieveLastWeeksTasks.as_view(), name="last-weeks-tasks"),
    path("task/<int:pk>/", views.TaskFromID.as_view(), name="task"),
    path("tasks/recurring/", views.RetrieveRecurringTasks.as_view(), name="recurring-tasks"),
    path("tasks/nextmonth/", views.RetrieveNextMonthsTasks.as_view(), name="next-month-tasks")
]