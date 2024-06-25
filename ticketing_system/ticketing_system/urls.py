from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('ticket/', include('ticket.urls')),
    path('accounts/', include('users.urls')),
]

