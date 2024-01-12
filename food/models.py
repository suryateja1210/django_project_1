from django.db import models

# Create your models here.
class dishes(models.Model):
    id= models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    items_required = models.CharField(max_length=100)
    process = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/dish')
    link = models.CharField(max_length=50,default='lik')

    def __str__(self) -> str:
        return self.Name
    
    class Meta:
        verbose_name_plural = 'dishes'
