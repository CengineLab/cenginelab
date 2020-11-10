from django.contrib.auth import login
from course.forms import CourseForm, EpisodeForm, StepForm
from typing import List
from django.contrib import messages
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
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



def add_course(request : HttpRequest, course_id: int = None):
    course = None
    if course_id:
        course = get_object_or_404(models.Course, pk=course_id)
    if request.method == "POST":
        course_form = CourseForm(instance=course, data=request.POST, files=request.FILES)
        if course_form.is_valid():
            course: models.Course = course_form.save(commit=False)
            course.created_by = request.user
            course.save()
            messages.success(request, f"Course {course.title} created successfully")
    else:
        course_form = CourseForm(instance=course)
    return render(request, "course/course_create.html", {"course_form": course_form})


def add_episode(request: HttpRequest, slug: str, episode_id: int=None):
    course = get_object_or_404(models.Course, created_by=request.user, slug=slug)
    episode = None
    print("\n\n getting episode \n\n")

    if episode_id:
        print("\n\n getting episode \n\n")
        episode = get_object_or_404(models.Episode, course=course, pk=episode_id)
    if request.method == "POST":
        episode_form = EpisodeForm(instance=episode, data=request.POST, files=request.FILES)
        if episode_form.is_valid():
            episode: models.Episode = episode_form.save(commit=False)
            episode.course = course
            episode.save()
            return redirect(episode.get_absolute_url())
    else:
        episode_form = EpisodeForm(instance=episode)
    return render(request, "course/episode_create.html", {'episode_form': episode_form})
    

def add_step(request,  slug: str, episode_id: int, step_id: int = None):
    course = get_object_or_404(models.Course, created_by=request.user, slug=slug)
    episode = get_object_or_404(models.Episode, course=course, pk = episode_id)
    step = None
    if step_id:
        step = get_object_or_404(models.Step, episode=episode, pk=step_id)
    if request.method == "POST":
        step_form = StepForm(instance=step, data=request.POST, files=request.FILES)
        if step_form.is_valid():
            step: models.Step = step_form.save(commit=False)
            step.episode = episode
            step.save()
            return redirect(episode.get_absolute_url())
    else:
        step_form = StepForm(instance=step)
    return render(request, "course/episode_create.html", {'episode_form': step_form})