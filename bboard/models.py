from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

    def title_end_price(self):
        if self.price:
            return '%s %.2f рублей' % (self.title, self.price)
        else:
            return self.title

    # чёт не совсем понял, куда поместить строку ниже
    title_end_price.short_description = "Название и цена"

    # это проще сделать, задав соответствующие значения
    # параметров у конструкторов полей, а не создавая функцию "clean"
    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValueError('Укажите описание ' +
                                           'продаваемого товара')
        if self.price and self.price < 0:
            errors['price'] = ValueError('Укажите неотрицательное ' +
                                         'значание цены')
        if errors:
            raise ValueError(errors)


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
