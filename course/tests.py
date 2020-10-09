from django.test import TestCase
from .models import User, Episode, EpisodeComment, Course
# Create your tests here.

class BaseTest:
    def setUpdata(self):
        self.user = User.objects.create(username="someusername", password="somerandompassword", email="someemail@gmail.com")
        self.course = Course.objects.create()