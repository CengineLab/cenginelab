from django.contrib.auth import login
from course.forms import CourseForm, EpisodeForm
from typing import List
from django.contrib import messages
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, View
from . import models
# Create your views here.

class CourseListView(ListView):
    model = models.Course
    paginate_by = 12
    context_object_name = "courses"
    template_name = "course/course_list.html"

class CourseDetailView(DetailView):
    model = models.Course
    context_object_name = "course"
    template_name = "course/course_detail.html"
    
class EpisodeDetailView(DetailView):
    model = models.Episode
    context_object_name = "episode"
    template_name = "course/episode_detail.html"


class AddCourse(View):
    def get(self, request: HttpRequest = None, **kwargs):
        course_form = CourseForm()
        return render(request, "course/add_course.html", {'course_form': course_form})

@login_required
def add_course(request : HttpRequest):
    if request.method == "POST":
        course_form = CourseForm(request.POST, files=request.FILES)
        if course_form.is_valid():
            course: models.Course = course_form.save(commit=False)
            course.created_by = request.user
            course.save()
            messages.success(request, f"Course {course.title} created successfully")
    else:
        course_form = CourseForm()
    return render(request, "course/course_create.html", {"course_form": course_form})


def add_episode(request: HttpRequest, slug: str, episode_id: int=None):
    course = get_object_or_404(models.Course, created_by=request.user, slug=slug)
    episode = None
    if episode_id:
        episode = get_object_or_404(models.Episode, course=course, pk=episode_id)
    if request.method == "POST":
        episode_form = EpisodeForm(instance=episode, data=request.POST, files=request.FILES)
        if episode_form.is_valid():
            episode = episode_form.save(commit=False)
            episode.course = course
            episode.save()
    else:
        episode_form = EpisodeForm()
    return render(request, "course/episode_create.html", {'episode_form': episode_form})
    
