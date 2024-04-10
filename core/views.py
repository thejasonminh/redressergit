from django.shortcuts import render, redirect

from item.models import Category, Item  #import the items and their categories

from .forms import SignupForm

# Author: Jason Ngo, Maxine Ramos, Jenny Shen, Joyce Xuan
# Class: INF 453 - Capstone Project
# Supervisor: Maher Elshakankiri
# Purpose: views (interactivity) of websites

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6] #show 6 items that arent sold
    categories = Category.objects.all() #show all categories
 
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

# Creating contact page
def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })