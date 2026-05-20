from django.db import models

class Student(models.Model):

    regno = models.CharField(max_length=20, null=True, blank=True)

    name = models.CharField(max_length=100)

    email = models.EmailField()

    program_level = models.CharField(max_length=50, null=True, blank=True)

    branch = models.CharField(max_length=50, null=True, blank=True)

    year = models.CharField(max_length=20, null=True, blank=True)

    semester = models.CharField(max_length=20, null=True, blank=True)

    enroll_date = models.DateField(null=True, blank=True)

    def __str__(self):

        return self.name