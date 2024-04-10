from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404

from item.models import Item
# Create your views here.

# Author: Jason Ngo, Maxine Ramos, Jenny Shen, Joyce Xuan
# Class: INF 453 - Capstone Project
# Supervisor: Maher Elshakankiri
# Purpose: views (interactivity) of user page, mainly for viewing your own items

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })


