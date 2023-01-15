
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from todoapi import views

router = DefaultRouter()
router.register("api/todos", views.TodoViewSet, basename="todos")

urlpatterns = [
    path('admin', admin.site.urls),
    path("", include(router.urls)),
]