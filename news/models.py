from django.db import models


class PostManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(PostManager, self).get_queryset().filter(avilable=True)


class NewsPost(models.Model):
    title = models.CharField(verbose_name="Название", max_length=30, db_index=True)
    img = models.ImageField(verbose_name="Изображение", upload_to="media/upload", blank=True)
    text = models.TextField(verbose_name="Текс", blank=True, db_index=True)
    textcut = models.TextField(verbose_name="Сокращенный текст", blank=True, db_index=True)
    pub_date = models.DateField(verbose_name="Дата публикации")
    avilable = models.BooleanField(default=True)
    objects = PostManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"