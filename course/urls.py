from django.urls import path
from . import views

app_name = "course"

urlpatterns = [
    path("", views.CourseListView.as_view(), name="course-list"),
    path("detail/<slug:slug>/", views.CourseDetailView.as_view(), name="course-detail"),
    path("episodes/<int:pk>/", views.EpisodeDetailView.as_view(), name="episode-detail"),
    path("add/", views.add_course, name="add-course"),
    path("add/<int:course_id>/", views.add_course, name="edit-course"),
    path("add/<slug:slug>/", views.add_episode, name="add-episode"),
    path("add/<slug:slug>/<int:episode_id>/", views.add_episode, name="edit-episode"),
    path("add/<slug:slug>/<int:episode_id>/step/", views.add_step, name="add-step"),
    path("add/<slug:slug>/<int:episode_id>/step/<int:step_id>/", views.add_step, name="edit-step"),
]