from django.urls import include, path


urlpatterns = [path("", include("tasks.urls"))]
