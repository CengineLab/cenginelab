from django.urls import path
from . import views

app_name = "course"

urlpatterns = [
    path("", views.CourseListView.as_view(), name="course-list"),
]