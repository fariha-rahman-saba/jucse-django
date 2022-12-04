from django.db import models

class Classes(models.Model):
    title = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    # link = 

    def __str__(self):
        return self.title

