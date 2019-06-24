from django.db import models


class Metadata(models.Model):
    filename = models.CharField(max_length=256)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.DateTimeField()

    def __str__(self):
        return self.filename
