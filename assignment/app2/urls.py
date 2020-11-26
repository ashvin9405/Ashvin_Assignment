from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', views.signup, name ="signup"),
    path('overview', views.overview, name ="overview"),
    path('login', views.login, name ="login"),
    path('logout', views.logout, name ="logout"),
    path('employee', views.employee, name="employee")
]