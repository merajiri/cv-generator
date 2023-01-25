from django.db import models
class profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    univercity = models.CharField(max_length=200)
    skills = models.TextField()
    previous_works = models.TextField()
    def __str__(self):
        return self.name