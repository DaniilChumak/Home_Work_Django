from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории', help_text='Укажите категорию')
    description = models.TextField(verbose_name='Описание категории товара', help_text='Добавьте описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование')
    description = models.TextField(verbose_name='Описание', help_text='Добавьте описание')
    image_preview = models.ImageField(upload_to='products/photo', blank=True, null=True, verbose_name='Фото',
                                      help_text='Загрузите фото товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    price = models.FloatField(verbose_name='Стоимость товара', help_text='Укажите стоимость товара')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="version",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Версия",
    )
    v_num = models.CharField(
        max_length=100,
        verbose_name="№ версии",
        help_text="Введите № версии",
    )
    v_name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    curr_v = models.BooleanField(
        verbose_name="Признак текущей версии",
        help_text="Активно?"
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["product"]

    def __str__(self):
        return f"Наименование продукта - {self.product}, Версия - {self.v_num}"
