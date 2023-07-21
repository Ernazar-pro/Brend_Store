from django.db import models

class Product(models.Model):
    image=models.ImageField(upload_to='products/%Y/%m/%d/',blank=True,null=True)
    title=models.CharField(max_length=30)
    description=models.TextField(blank=True,null=True)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['-id']