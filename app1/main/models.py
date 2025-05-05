from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, help_text='Введите название пряжи')
    origin = models.CharField(max_length=50, help_text='Введите происхождение пряжи')
    price = models.IntegerField(help_text='Введите цену пряжи')

    photo = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
       return self.name
    