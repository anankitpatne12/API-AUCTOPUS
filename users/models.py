from django.db import models

# Create your models here.
class StudData(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.CharField(max_length=300)
    email = models.EmailField(max_length=200)
    college = models.CharField(max_length=200)

    def __str__(self):
        return self.name