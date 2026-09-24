from django import forms

from .models import StudyTask


class StudyTaskForm(forms.ModelForm):
    class Meta:
        model = StudyTask
        fields = ["course_name", "title", "estimated_minutes"]
