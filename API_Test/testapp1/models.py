from django.db import models

# Create your models here.
class TestModel(models.Model):
    name = models.CharField(max_length=225, unique=True)
    description = models.TextField()
    phone_number = models.CharField(max_length=255)
    is_alive = models.BooleanField()
    amount = models.FloatField()
    # extra_name = models.CharField(max_length=250, editable=False, default="null")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Test Model'