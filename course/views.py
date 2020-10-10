from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.

class CourseListView(ListView):
    model = models.Course
    paginate_by = 12
    context_object_name = "courses"
    template_name = "course/course_list.html"
