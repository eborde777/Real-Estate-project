from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import ContactModel


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        cntct_mod = ContactModel()

        cntct_mod.firstName = form.cleaned_data.get("firstname")
        cntct_mod.lastName = form.cleaned_data.get("lastname")
        cntct_mod.email = form.cleaned_data.get("email")
        cntct_mod.phone_number = form.cleaned_data.get("phone")
        cntct_mod.description = form.cleaned_data.get("description")
        cntct_mod.save()
        messages.success(request, "Thank You !, I will reach you shortly...")
        return HttpResponseRedirect("#")

    context= {
        "form":form,
    }

    return render(request, "contact.html", context)

