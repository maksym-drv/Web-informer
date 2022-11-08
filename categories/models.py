from django.db import models

class Category(models.Model):
    name = models.CharField("Category's name", max_length=200, null=False)
    description = models.CharField("Category's description", max_length=600, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
 
    class Meta:
        verbose_name_plural = "Categories"