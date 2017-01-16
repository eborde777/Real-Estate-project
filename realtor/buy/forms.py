from django import forms

from .models import Buy

class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = [
            'owner_name',
            'address',
            'city',
            'state',
            'zipcode',
            'bedroom',
            'bathroom',
            'square_feet',
            'price',
            'image',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'overview',
        ]
