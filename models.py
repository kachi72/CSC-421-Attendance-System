from django.db import models


# model to keep information about students after registration
class Student(models.Model):
    name = models.CharField(max_length=200, null=False)
    faculty_choices = [
        ('FACUS', 'FACUS'),
        ('FAHUMS', 'FAHUMS')
    ]
    faculty = models.CharField(max_length=200, null=False, choices=faculty_choices)
    department = models.CharField(max_length=100, null=False)
    studentNumber = models.CharField(max_length=100, default='AU202100400')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name', 'faculty']

    def __str__(self):
        return self.name

