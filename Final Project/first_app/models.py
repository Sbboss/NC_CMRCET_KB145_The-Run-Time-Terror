from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.


class OCR(models.Model):
    name = models.CharField(max_length=200, null=True)
    input = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'JPG', 'jpeg', 'png', 'PNG', ])])

    def __str__(self):
        return self.name