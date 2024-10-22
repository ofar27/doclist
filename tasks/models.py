from django.db import models
from django.utils.text import slugify


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()

    @classmethod
    def get_default_collection(cls) -> "Collection":
        collection, _ = cls.objects.get_or_create(name="Défault", slug="_default")
        return collection

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)


class Task(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)



def __str__(self):
    return self.description


class Task(models.Model):
    description = models.CharField(max_length=255)
    PRIORITY_CHOICES = [
        ('low', 'Faible'),
        ('medium', 'Moyenne'),
        ('high', 'Élevée'),
    ]
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description} - {self.priority}'

