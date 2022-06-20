from django.db import models
# Create your models here.


class Planning(models.Model):

    week_number = models.IntegerField()
    validated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.week_number)
