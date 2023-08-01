from django.db import models
from filer.fields.image import FilerImageField


class Slider(models.Model):
    image = FilerImageField(
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.image.__str__()
