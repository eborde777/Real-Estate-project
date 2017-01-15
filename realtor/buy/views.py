from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404
from .models import Buy
from .forms import BuyForm
# Create your views here.



def home(request):
    return render(request, 'base.html', {})


def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = BuyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "New Post Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }
    return render(request, 'buy_form.html', context)

def list(request):
    queryset_list = Buy.objects.all()

    search_obj = request.GET.get("search_query")
    if search_obj:
        queryset_list = queryset_list.filter(
            Q(city__icontains = search_obj)|
            Q(state__icontains = search_obj)|
            Q(zipcode__icontains = search_obj)
        ).distinct()
    paginator = Paginator(queryset_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "message": "Hello we are in",
        "object_list": queryset,
    }
    return render(request, 'home.html', context)



def detail(request, id=None):
    queryset = get_object_or_404(Buy, id= id)
    context = {
        "queryset": queryset,
    }
    return render(request, 'detail.html', context)

def update(request, id=None):
    if not request.user.is_superuser or not request.user.is_staff:
        raise Http404
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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    queryset = get_object_or_404(Buy, id= id)
    queryset.delete()
    messages.success(request, "Post Named" + " "+ queryset.owner_name +" " + "Deleted Successfully")
    return redirect("buy:list")