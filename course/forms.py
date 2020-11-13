from django import forms
from .models import Course, Episode, EpisodeComment, Step

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

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ("title", "content", "timestamp",)
    