from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your models here.

User = get_user_model()

class Course(models.Model):
    """Model instance to represent a course on the website"""
    created_by = models.ForeignKey(User, related_name="created_courses", on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField()
    picture = models.ImageField(upload_to="courses/pictures/%Y/%m/")
    slug = models.SlugField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date_created", "title",)

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"<Course: {self.title[:30]}>"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Episode(models.Model):
    course = models.ForeignKey(Course, related_name="episodes", on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)
    youtube_video_link = models.URLField(blank=True, null=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("date_created",)
    
    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return f'<Episode: {self.title[:30]}>'
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug  = slugify(self.title)
        super().save(*args, **kwargs)


class EpisodeComment(models.Model):
    user = models.ForeignKey(User, related_name="episode_comments", on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date_created",)
    
    def __str__(self) -> str:
        return self.comment
    

    
    