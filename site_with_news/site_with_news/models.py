from django.db import models


class New(models.Model):
    title = models.CharField("Название", max_length=50)
    new_text = models.TextField("Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
