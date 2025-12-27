from django.db import models
from django.contrib.auth.models import User
from apps.common.models import BasedTimedModel


# Create your models here.


class HomeSlider(BasedTimedModel):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='slider', verbose_name='Фото')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class FAQ(BasedTimedModel):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'


class Category(BasedTimedModel):
    title = models.TextField(verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Не пиши юда')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ToDo(BasedTimedModel):
    text = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(blank=True, null=True)
    full_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='todos_category')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos_category')

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'


class Comment(BasedTimedModel):
    comment = models.TextField(blank=True, null=True)

def get_image_path(instance, filename):
    return f'posts/photos{instance.Todo.slug}/{filename}'
