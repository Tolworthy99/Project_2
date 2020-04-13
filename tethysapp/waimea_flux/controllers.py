from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import TextInput, DatePicker, SelectInput

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'
        }
    )

    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button
    }

    return render(request, 'waimea_flux/home.html', context)

@login_required()
def About(request):
    """
    Controller for the background page.
    """
    context = {}

    return render(request,'waimea_flux/About.html',context)

@login_required()
def Data(request):
    """
    Controller for the background page.
    """
    context = {}

    return render(request,'waimea_flux/Data.html',context)

@login_required()
def New_Data(request):
    """
    Controller for New Data page.
    """
    # Define form gizmos
    name_input = TextInput(
        display_text='Name',
        name='name'
    )

    owner_input = SelectInput(
        display_text='Owner',
        name='owner',
        multiple=False,
        options=[('Reclamation', 'Reclamation'), ('Army Corp', 'Army Corp'), ('Other', 'Other')],
        initial=['Reclamation']
    )

    river_input = TextInput(
        display_text='River',
        name='river',
        placeholder='e.g.: Mississippi River'
    )

    date_built = DatePicker(
        name='date-built',
        display_text='Date Built',
        autoclose=True,
        format='MM d, yyyy',
        start_view='decade',
        today_button=True,
        initial='February 15, 2017'
    )

    add_button = Button(
        display_text='Add',
        name='add-button',
        icon='glyphicon glyphicon-plus',
        style='success',
        attributes={'form': 'add-dam-form'},
        submit=True
    )

    cancel_button = Button(
        display_text='Cancel',
        name='cancel-button',
        href=reverse('waimea_flux:home')
    )

    context = {
        'name_input': name_input,
        'owner_input': owner_input,
        'river_input': river_input,
        'date_built_input': date_built,
        'add_button': add_button,
        'cancel_button': cancel_button,
    }

    return render(request,'waimea_flux/New_Data.html',context)


@login_required()
def Geolmap(request):
    """
    Controller for the background page.
    """
    context = {}

    return render(request,'waimea_flux/Geolmap.html',context)
@login_required()
def Othermap(request):
    """
    Controller for the background page.
    """
    context = {}

    return render(request,'waimea_flux/Othermap.html',context)
