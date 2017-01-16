from django.db import models
from django.core.urlresolvers import reverse

def upload_location(queryset, filename):
    return "%s/%s" %(queryset.address, filename)

class Buy(models.Model):
    image = models.ImageField( upload_to=upload_location, null=True, blank=True)
    image1 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    image2 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    image3 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    image4 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    image5 = models.ImageField(upload_to=upload_location, null=True, blank=True)
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


    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    @property
    def image1_url(self):
        if self.image1 and hasattr(self.image1, 'url'):
            return self.image1.url

    @property
    def image2_url(self):
        if self.image2 and hasattr(self.image2, 'url'):
            return self.image2.url

    @property
    def image3_url(self):
        if self.image3 and hasattr(self.image3, 'url'):
            return self.image3.url

    @property
    def image4_url(self):
        if self.image4 and hasattr(self.image4, 'url'):
            return self.image4.url

    @property
    def image5_url(self):
        if self.image5 and hasattr(self.image5, 'url'):
            return self.image5.url