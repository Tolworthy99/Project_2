from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import TextInput, DatePicker, SelectInput, DataTableView, MVDraw, MVView, MapView, MVLayer, RangeSlider
from .model import add_new_dam, get_all_dams
from tethys_sdk.workspaces import app_workspace

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
    sampleid_input = TextInput(
        display_text='Sample ID',
        name='sampleid'
    )

    river_input = TextInput(
        display_text='River',
        name='river',
        placeholder='e.g.: Waimea River'
    )

    datecol_input = DatePicker(
        name='date-built',
        display_text='Date Built',
        autoclose=True,
        format='MM d, yyyy',
        start_view='decade',
        today_button=True,
        initial='February 15, 2017'
    )

    timecol_input = TextInput(
        display_text='Time of Sample Collection',
        name='timecol'
    )

    note_input = TextInput(
        display_text='Any Notes?',
        name='note'
    )

    pH_input = TextInput(
        display_text='pH',
        name='pH'
    )

    temper_input = TextInput(
        display_text='Temperature',
        name='temper'
    )

    cond_input = TextInput(
        display_text='Conductivity',
        name='cond'
    )

    ca_input = TextInput(
        display_text='Ca<sup>2+</sup>',
        name='ca'
    )

    mg_input = TextInput(
        display_text='Mg<sup>2+</sup>',
        name='mg'
    )

    na_input = TextInput(
        display_text='Na<sup>+</sup>',
        name='na'
    )

    k_input = TextInput(
        display_text='K<sup>+</sup>',
        name='k'
    )

    hco_input = TextInput(
        display_text='HCO<sub>3<sup>-</sup>',
        name='hco'
    )

    cl_input = TextInput(
        display_text='Cl<sup>-</sup>',
        name='cl'
    )

    so_input = TextInput(
        display_text='SO<sub>4</sub><sup>2-</sup>',
        name='so'
    )

    sio_input = TextInput(
        display_text='SiO<sub>2</sub>',
        name='sio'
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
        href=reverse('dam_inventory:home')
    )

    context = {
        'name_input': name_input,
        'river_input': river_input,
        'datecol_input': datecol_input,
        'timecol':timecol_input,
        'note_input': note_input,
        'pH_input': pH_input,
        'temper_input': temper_input,
        'cond_input': cond_input,
        'ca_input': ca_input,
        'mg_input': mg_input,
        'na_input': na_input,
        'k_input': k_input,
        'hco_input': hco_input,
        'cl_input': cl_input,
        'so_input': so_input,
        'sio_input': sio_input,
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

@login_required()
def Datamap(request):
    """
    Controller for the background page.
    """
    context = {}

    return render(request,'waimea_flux/Datamap.html',context)
