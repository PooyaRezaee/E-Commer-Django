from django.db import models

__all__ = ['Category','Product']

class Category(models.Model):
    name = models.CharField(max_length=200,)
    slug = models.CharField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d')
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        pass

    def __str__(self):
        return self.name

    def is_avalible(self):
        return True if self.amount == 0 else False