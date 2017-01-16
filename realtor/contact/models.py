from django.db import models
from django.core.validators import RegexValidator


class ContactModel(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'\D?(\d{0,3}?)\D{0,2}(\d{3})?\D{0,2}(\d{3})\D?(\d{4})$',
                                 message="Enter a valid phone number")
    phone_number = models.CharField(validators=[phone_regex], blank=True, null=True, max_length=16)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


