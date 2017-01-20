from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
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

        subject = "User named %s %s asked a question" %(cntct_mod.firstName, cntct_mod.lastName)
        from_email = cntct_mod.email
        to_email = (settings.EMAIL_HOST_USER,)
        contact_message = """
        %s %s, via %s \n \n %s
        """ % ( cntct_mod.firstName,cntct_mod.lastName, cntct_mod.email,cntct_mod.description )
        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=False,
        )
        messages.success(request, "Thank You !, I will reach you shortly...")
        return redirect("contact:contact")

    context= {
        "form":form,
    }

    return render(request, "contact.html", context)

