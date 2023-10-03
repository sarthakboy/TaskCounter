
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name = 'index'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete-task'),
    path('increase-day-to-go/<int:task_id>/', views.increase_day_to_go, name='increase-day-to-go'),
]
