from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LostItem, FoundItem
from .forms import LostForm, FoundForm


def index(request):
    user = request.user
    return render(request, 'index.html')

def lost(request):
    items = LostItem.objects.all()
    ctx = {'items': items}
    return render(request, 'lost.html', ctx)

def found(request):
    items = FoundItem.objects.all()
    ctx = {'items': items}
    return render(request, 'found.html', ctx)

def about(request):
    return render(request, 'about.html')

def lost_item(request):
    items = FoundItem.objects.all()
    ctx = {'items': items}
    return render(request, 'lost_item.html', ctx)

def add_lost(request):
    form = LostForm()
    if request.method == 'POST':
        form = LostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lost')
    ctx = {'form' : form}
    return render(request, 'add_lost.html', ctx)

def add_found(request):
    form = FoundForm()
    if request.method == 'POST':
        form = FoundForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('found')
    ctx = {'form' : form}
    return render(request, 'add_found.html', ctx)

def user_lost(request):
    items = LostItem.objects.all()
    ctx = {'items': items}
    return render(request, 'user_lost.html', ctx)

def user_found(request):
    items = FoundItem.objects.all()
    ctx = {'items': items}
    return render(request, 'user_found.html', ctx)

def edit_lost(request, item_id):
    items = LostItem.objects.get(pk=item_id)
    form = LostForm(request.POST or None, instance=items)
    ctx = {'items': items, 'form': form}
    if form.is_valid():
        form.save()
        return redirect('user_lost')
    return render(request, 'edit_lost.html', ctx)

def edit_found(request, item_id):
    items = FoundItem.objects.get(pk=item_id)
    form = FoundForm(request.POST or None, instance=items)
    ctx = {'items': items, 'form': form}
    if form.is_valid():
        form.save()
        return redirect('user_found')
    return render(request, 'edit_found.html', ctx)

def delete_lost(request, item_id):
    items = LostItem.objects.get(pk=item_id)
    items.delete()
    return redirect('user_lost')

def delete_found(request, item_id):
    items = FoundItem.objects.get(pk=item_id)
    items.delete()
    return redirect('user_found')

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        lo = LostItem.objects.filter(item_name__contains=searched)
        fo = FoundItem.objects.filter(item_name__contains=searched)
        ctx = {'searched' : searched, 'lo' : lo, 'fo': fo}
        return render(request, 'search.html', ctx)