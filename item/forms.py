from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Name',
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Description',
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Price',
                'class': 'w-full py-4 px-6',
                'style': 'color: black; background-color: #EEB29280; border-color: black; border-style: solid; border-width: medium;'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
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
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }