

from django.contrib import admin
from django.urls import path
from log_in import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.login_view, name="hello"),
    
]
