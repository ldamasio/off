from django.db.models import fields
from rest_framework import serializers
from .models import Item
  
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('code', 'status', 'imported_t', 'url',
        'creator', 'created_t', 'last_modified_t', 'product_name',
        'quantity', 'brands', 'categories', 'labels', 'cities',
        'purchase_places', 'stores', 'ingredients_text', 'traces', 
        'serving_size', 'serving_quantity', 'nutriscore_score', 
        'nutriscore_grade', 'main_category', 'image_url')
