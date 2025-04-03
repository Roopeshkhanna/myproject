from django.db import models

class Academics(models.Model):
    university_id = models.IntegerField(primary_key=True)
    accredation = models.CharField(max_length=255)
    website = models.URLField()
    language = models.CharField(max_length=50)
    acceptance_rate = models.FloatField()
    tution_fee = models.IntegerField()
    scholarship = models.BooleanField()
    application_deadline = models.DateField()
    entrance_exam_unive = models.BooleanField()
    entrance_exams = models.TextField()
    mode_of_study = models.CharField(max_length=50)
    campus_size = models.CharField(max_length=100)
    no_of_programs_offered = models.IntegerField()
    intl_student_percentage = models.IntegerField()
    campus_facilities = models.TextField()
    ranking = models.IntegerField()
