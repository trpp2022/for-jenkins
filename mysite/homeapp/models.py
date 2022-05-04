from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name