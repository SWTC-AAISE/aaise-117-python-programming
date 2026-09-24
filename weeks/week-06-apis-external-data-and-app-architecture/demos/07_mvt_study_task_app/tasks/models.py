from django.db import models


class StudyTask(models.Model):
    course_name = models.CharField(max_length=80)
    title = models.CharField(max_length=120)
    estimated_minutes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.course_name}: {self.title}"
