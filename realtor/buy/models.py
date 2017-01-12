from django.db import models
from django.core.urlresolvers import reverse

class Buy(models.Model):
    image = models.FileField(null=True, blank=True)
    owner_name = models.CharField(max_length=50)
    address = models.CharField(max_length= 225)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    bedroom = models.IntegerField(default=0)
    bathroom = models.DecimalField(default=0.0, decimal_places=1, max_length=10, max_digits=4)
    square_feet = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, max_length=10)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    overview = models.TextField(blank= True, null=True)


    def __str__(self):
        return self.owner_name

    def get_absolute_url(self):
        return reverse("buy:detail", kwargs={'id':self.id})

    class Meta:
        ordering = ['-timestamp']