from django.db import models


class News(models.Model):
    title = models.CharField("Название", max_length=50)
    text = models.TextField("Описание",)

    def __str__(self):
        return self.title
