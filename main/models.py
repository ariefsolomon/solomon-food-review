import uuid
from django.db import models

# Create your models here.
class Food(models.Model):
    CATEGORY_CHOICES = [
        ('dish', 'Dish'),
        ('protein', 'Protein'),
        ('appetizer', 'Appetizer'),
        ('main food', 'Main Food'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food_name = models.CharField(max_length=255)
    content = models.TextField()
    thumbnail = models.URLField (blank=True, null=True)
    views = models.PositiveBigIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.food_name
    
    @property
    def is_review_hot(self):
        return self.views >= 20
    
    def increment_views(self):
        self.views += 1
        self.save()