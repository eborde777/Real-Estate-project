from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Buy
from .forms import BuyForm
# Create your views here.



def home(request):
    return render(request, 'base.html', {})


def create(request):
    form = BuyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, 'buy_form.html', context)

def list(request):
    queryset = Buy.objects.all()
    context = {
        "message": "Hello we are in",
        "queryset": queryset,
    }
    return render(request, 'home.html', context)

def detail(request, id=None):
    queryset = get_object_or_404(Buy, id= id)
    context = {
        "queryset": queryset,
    }
    return render(request, 'detail.html', context)

def update(request, id=None):
    instance = get_object_or_404(Buy, id=id)
    form = BuyForm(request.POST or None, request.FILES or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, 'buy_form.html', context)

def delete(request, id=None):
    queryset = get_object_or_404(Buy, id= id)
    queryset.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("buy:list")