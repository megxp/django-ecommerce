from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description =models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self. name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # Correction : = au lieu de -
    stock = models.PositiveIntegerField() # Correction : () au lieu de O
    image = models.ImageField(upload_to='products/', blank=True, null=True) # Correction : ' autour du chemin
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name