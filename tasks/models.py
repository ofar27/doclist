from django.db import models
from django.utils.text import slugify


class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    is_default = models.BooleanField(default=False)

    @classmethod
    def get_default_collection(cls) -> "Collection":
        # Crée ou récupère la collection par défaut
        collection, created = cls.objects.get_or_create(
            slug="_default",
            defaults={"name": "Default", "is_default": True},
        )
        return collection

    def delete(self, *args, **kwargs):
        if self.is_default:
            raise ValueError("La collection par défaut ne peut pas être supprimée.")
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Si le slug n'est pas défini, on le génère à partir du nom
        if not self.slug:
            self.slug = slugify(self.name)

        if self.is_default:
            # Assure qu'il n'y a qu'une seule collection par défaut
            Collection.objects.filter(is_default=True).exclude(pk=self.pk).update(is_default=False)

        super().save(*args, **kwargs)


class Task(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
