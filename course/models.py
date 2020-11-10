from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

User = get_user_model()


class Course(models.Model):
    """Model instance to represent a course on the website"""

    created_by = models.ForeignKey(
        User, related_name="created_courses", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=500)
    description = models.TextField()
    picture = models.ImageField(upload_to="courses/pictures/%Y/%m/")
    slug = models.SlugField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (
            "-date_created",
            "title",
        )

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"<Course: {self.title[:30]}>"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("course:course-detail", kwargs={"slug": self.slug})
    
    def get_edit_url(self) -> str:
        return reverse("course:edit-course", kwargs={"course_id": self.pk })
    

class CourseImage(models.Model):
    def get_upload_to(instance, filename):
        return f"course-images/{instance.course.date_created.year}/{instance.course.slug}/{filename}"

    course = models.ForeignKey(Course, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_to)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ("-date_created",)
    
    def get_absolute_url(self):
        return self.image.url


class Episode(models.Model):
    course = models.ForeignKey(
        Course, related_name="episodes", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)
    youtube_video = models.URLField(blank=True, null=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("date_created",)

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"<Episode: {self.title[:30]}>"

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("course:episode-detail", kwargs={"pk": self.pk})
    
    def get_edit_url(self) -> str:
        return reverse("course:edit-episode", kwargs={"slug": self.course.slug, "episode_id": self.pk })

    def next(self) -> "Episode":
        return self.course.episodes.filter(date_created__gt=self.date_created).first()
    
    def prev(self) -> "Episode":
        return self.course.episodes.filter(date_created__lt=self.date_created).last()


class Step(models.Model):
    episode = models.ForeignKey(
        Episode, related_name="steps", on_delete=models.CASCADE, blank=True, null=True
    )
    title = models.CharField(max_length=250)
    timestamp = models.TimeField(null=True, blank=True)
    content = models.TextField(
        help_text="This uses markdown format"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("date_created",)
    
    def __str__(self):
        return self.title

    def get_edit_url(self) -> str:
        return reverse("course:edit-step", kwargs={"slug": self.episode.course.slug, "episode_id": self.episode.pk, "step_id": self.pk})


class EpisodeComment(models.Model):
    user = models.ForeignKey(
        User, related_name="episode_comments", on_delete=models.CASCADE
    )
    episode = models.ForeignKey(
        Episode, related_name="comments", on_delete=models.CASCADE
    )
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self) -> str:
        return self.comment
