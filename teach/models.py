from django.db import models

# Create your models here.
class TeachFile(models.Model):
    title = models.CharField(max_length=120)
    file = models.FileField(upload_to="media/upload/files/", blank=True)
    img = models.ImageField(upload_to="media/upload/file/", blank=True)
    size = models.IntegerField(blank=True)
    typefile = models.CharField(blank=True, max_length=9)
    linkfile = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

