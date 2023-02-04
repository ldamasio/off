from django.db import models
  
class Item(models.Model):
    code = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    imported_t = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)
    creator = models.CharField(max_length=255, blank=True)
    created_t = models.CharField(max_length=255, blank=True)
    last_modified_t = models.CharField(max_length=255, blank=True)
    product_name = models.CharField(max_length=255, blank=True)
    quantity = models.CharField(max_length=255, blank=True)
    brands = models.CharField(max_length=255, blank=True)
    categories = models.CharField(max_length=255, blank=True)
    labels = models.CharField(max_length=255, blank=True)
    cities = models.CharField(max_length=255, blank=True)
    purchase_places = models.CharField(max_length=255, blank=True)
    stores = models.CharField(max_length=255, blank=True)
    ingredients_text = models.TextField(max_length=255, blank=True)
    traces = models.CharField(max_length=255, blank=True)
    serving_size = models.CharField(max_length=255, blank=True)
    serving_quantity = models.CharField(max_length=255, blank=True)
    nutriscore_score = models.CharField(max_length=255, blank=True)
    nutriscore_grade = models.CharField(max_length=255, blank=True)
    main_category = models.CharField(max_length=255, blank=True)
    image_url = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.product_name
