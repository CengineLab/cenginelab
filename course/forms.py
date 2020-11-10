from django import forms
from .models import Course, Episode, EpisodeComment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'picture')

class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ("title",'description', "youtube_video")


class EpisodeCommentForm(forms.ModelForm):
    class Meta:
        model = EpisodeComment
        fields = ("comment",)
