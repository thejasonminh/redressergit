from django import forms

from .models import Item

# Author: Jason Ngo, Maxine Ramos, Jenny Shen, Joyce Xuan
# Class: INF 453 - Capstone Project
# Supervisor: Maher Elshakankiri
# Purpose: Item creation and edit forms

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Item Name',
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Item Description',
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'Item Price',
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            }),
            'image': forms.FileInput(attrs={
                'placeholder': 'Select Image',
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Item Name',
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Item Description',
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'Item Price',
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            }),
            'image': forms.FileInput(attrs={
                'placeholder': 'Select Image',
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            })
        }