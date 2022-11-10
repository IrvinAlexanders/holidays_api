from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v2/holidays', views.Holidays.as_view())
]
