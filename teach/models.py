from django.db import models

# Create your models here.
class TeachFile(models.Model):
    title = models.CharField(verbose_name="Название", max_length=120)
    description = models.TextField(verbose_name="Описание", blank=True)
    file = models.FileField(verbose_name="Файл", upload_to="media/upload/files/", blank=True)
    img = models.ImageField(verbose_name="Изображение", upload_to="media/upload/file/", blank=True)
    size = models.CharField(verbose_name="Размер файла", blank=True, max_length=30)
    typefile = models.CharField(verbose_name="Тип файла", blank=True, max_length=9)
    linkfile = models.URLField(verbose_name="Ссылка на файл", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

