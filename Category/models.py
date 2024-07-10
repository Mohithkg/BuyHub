from django.db import models

# Create your models here.

class Category(models.Model):
    """
       Represents a product category in the e-commerce platform.
       Attributes:
           category_name (CharField): The name of the category. This field must be unique.
           slug (CharField): A URL-friendly version of the category name, used for SEO and routing. This field must be unique.
           description (TextField): A brief description of the category. This field is optional.
           category_image (ImageField): An optional image associated with the category. The image is uploaded to 'photos/categories/'.
       """
    category_name=models.CharField(max_length=50, unique=True)
    slug= models.CharField(max_length=100, unique=True)
    description= models.TextField(max_length=255, blank=True)
    category_image= models.ImageField(upload_to='photos/categories/', blank=True)

    class Meta:
        verbose_name= 'Category'
        verbose_name_plural= 'Categories'

    def __str__(self):
        return self.category_name