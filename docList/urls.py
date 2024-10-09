from django.contrib import admin
from django.urls import path
import tasks.views as views


urlpatterns = [
    path('', views.index, name="home"),
    path('add_collection/', views.add_collection, name="add_collection"),
    path('admin/', admin.site.urls),

]
