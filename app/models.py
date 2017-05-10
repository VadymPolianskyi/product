from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ' - ' + self.description


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    price = models.FloatField(default=0)
    created_at = models.DateField()
    modified_at = models.DateField()

    def __str__(self):
        return self.song_title