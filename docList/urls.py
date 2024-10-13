from django.contrib import admin
from django.urls import path
import tasks.views as views


urlpatterns = [
    path('', views.index, name="home"),
    path('add_collection/', views.add_collection, name="add-collection"),
    path('add_task/', views.add_task, name="add-task"),
    path('get_task/<str:collection_pk>/', views.get_task, name="get-task"),
    path('admin/', admin.site.urls),

]
