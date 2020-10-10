from django.test import TestCase
from ..models import User, Episode, EpisodeComment, Course
from django.utils.text import slugify
from django.urls import reverse
from .. import views


class CourseListViewTests(TestCase):
    def test_no_error_raised(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('course:course-list'), follow=False)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No courses are available.")
        self.assertQuerysetEqual(response.context['courses'], [])

