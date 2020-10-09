from django.test import TestCase
from ..models import User, Episode, EpisodeComment, Course
from django.utils.text import slugify

# Create your tests here.


class BaseTestDataSetup:
    """Base Test Class To setup test data"""

    def setUpdata(self):
        self.user = User.objects.create(
            username="someusername",
            password="somerandompassword",
            email="someemail@gmail.com",
        )
        self.course = Course.objects.create(
            created_by=self.user,
            title="title",
            description="some description",
            picture="/media/some_picture.jpg",
        )
        self.episode = Episode.objects.create(
            course=self.course,
            title="title",
            description="some description",
            youtube_video_link="https://youtube.com/somerandomlink/",
        )


# -----------------------------------------
#       TEST CASES
# -----------------------------------------


class CourseTest(BaseTestDataSetup, TestCase):
    def setUp(self) -> None:
        super().setUpdata()

    def test_course_data(self):
        tests = [
            {
                "created_by": self.user,
                "title": "title",
                "description": "some description",
                "picture": "/media/some_picture.jpg",
            },
        ]
        for test in tests:
            course = Course.objects.create(**test)
            self.assertEqual(course.created_by, test["created_by"])
            self.assertEqual(course.title, test["title"])
            self.assertEqual(course.description, test["description"])
            self.assertEqual(course.picture, test["picture"])
            self.assertEqual(course.slug, slugify(test["title"]))


class EpisodeTest(BaseTestDataSetup, TestCase):
    def setUp(self) -> None:
        super().setUpdata()

    def test_course_data(self):
        tests = [
            {
                "course": self.course,
                "title": "title",
                "description": "some description",
                "youtube_video_link": "https://youtube.com/somerandomlink/",
            },
        ]
        for test in tests:
            episode = Episode.objects.create(**test)
            self.assertEqual(episode.title, test["title"])
            self.assertEqual(episode.description, test["description"])
            self.assertEqual(episode.course, test["course"])
            self.assertEqual(episode.slug, slugify(test["title"]))


class EpisodeCommentTest(BaseTestDataSetup, TestCase):
    def setUp(self) -> None:
        super().setUpdata()

    def test_course_data(self):
        tests = [
            {
                "episode": self.episode,
                "user": self.user,
                "comment": "some description",
            },
        ]
        for test in tests:
            episodecomment = EpisodeComment.objects.create(**test)
            self.assertEqual(episodecomment.episode, test["episode"])
            self.assertEqual(episodecomment.comment, test["comment"])
            self.assertEqual(episodecomment.user, test["user"])
