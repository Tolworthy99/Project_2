from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import TextInput, DatePicker, SelectInput, DataTableView, MVDraw, MVView, MapView, MVLayer, RangeSlider
from tethys_sdk.workspaces import app_workspace
from .model import add_new_data, get_all_water

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

@app_workspace
@login_required()
def Data(request, app_workspace):
    """
    Controller for the background page.
    """
    waters = get_all_water(app_workspace.path)
    table_rows = []

    for water in waters:
        table_rows.append(
            (
                water['sampleid'],water['river'], water['datecol'], water['timecol'],water['note'], water['pH'], water['temper'], water['cond'],
                water['ca'],water['mg'],water['na'],water['k'],water['hco'],water['cl'],water['so'],water['sio']
            )
        )

    water_table = DataTableView(
        column_names=('Sample ID', 'River', 'Date Collected', 'Time Collected', 'Notes', 'pH', 'Temperature (C)', 'Conductivity', 'Ca2+ (mg/L)', 'Mg2+ (mg/L)', 'Na+ (mg/L)', 'K+ (mg/L)','HCO3- (mg/L)', 'Cl- (mg/L)', 'SO42- (mg/L)', 'SiO2 (mg/L)'),
        rows=table_rows,
        searching=False,
        orderClasses=False,
        lengthMenu=[ [10,25,50,-1], [10,25,50,"All"]],
    )

    context = {
        'water_table':water_table
    }

    return render(request,'waimea_flux/Data.html',context)


@app_workspace
@login_required()
def New_Data(request, app_workspace):
    """
    Controller for New Data page.
    """
    # Default Values
    sampleid = ''
    river = ''
    datecol = ''
    timecol = ''
    note = ''
    pH = ''
    temper = ''
    cond = ''
    ca = ''
    mg = ''
    na = ''
    k = ''
    hco = ''
    cl = ''
    so = ''
    sio = ''
    loaction = ''

    # Errors
    sampleid_error = ''
    datecol_error = ''
    location_error = ''

    # Handle form submission
    if request.POST and 'add-button' in request.POST:
        # Get values
        has_errors = False
        sampleid = request.POST.get('sampleid',None)
        river = request.POST.get('river',None)
        datecol = request.POST.get('datecol',None)
        timecol = request.POST.get('timecol',None)
        note = request.POST.get('note',None)
        pH = request.POST.get('pH',None)
        temper = request.POST.get('temper',None)
        cond = request.POST.get('cond',None)
        ca = request.POST.get('ca',None)
        mg = request.POST.get('mg',None)
        na = request.POST.get('na',None)
        k = request.POST.get('k',None)
        hco = request.POST.get('hco',None)
        cl = request.POST.get('cl',None)
        so = request.POST.get('so',None)
        sio = request.POST.get('sio',None)
        location = request.POST.get('geometry',None)

        #validate
        if not sampleid:
            has_errors = True
            sampleid_error = 'Sample ID is required'

        if not datecol:
            has_errors = True
            datecol_error = 'Date Collected is Required'

        if not location:
            has_errors = True
            location_error = 'Location is required'

        if not has_errors:
            #Do Stuff here
            add_new_data(db_directory=app_workspace.path, location=location, sampleid=sampleid, river=river, datecol=datecol, timecol=timecol, note=note, pH=pH, temper=temper, cond=cond, ca=ca, mg=mg, na=na, k=k, hco=hco, cl=cl, so=so, sio=sio)
            return redirect(reverse('waimea_flux:home'))

        messages.error(request, "Please fix errors.")


    # Define form gizmos
    sampleid_input = TextInput(
        display_text='Sample ID',
        name='sampleid',
        initial=sampleid,
        error=sampleid_error
    )

    river_input = TextInput(
        display_text='River',
        name='river',
        placeholder='e.g.: Waimea River'
    )

    datecol_input = DatePicker(
        name='datecol',
        display_text='Date Collected',
        autoclose=True,
        format='MM d, yyyy',
        start_view='decade',
        today_button=True,
        initial=datecol,
        error=datecol_error

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
        display_text='Ca2+',
        name='ca'
    )

    mg_input = TextInput(
        display_text='Mg2+',
        name='mg'
    )

    na_input = TextInput(
        display_text='Na+',
        name='na'
    )

    k_input = TextInput(
        display_text='K+',
        name='k'
    )

    hco_input = TextInput(
        display_text='HCO3-',
        name='hco'
    )

    cl_input = TextInput(
        display_text='Cl-',
        name='cl'
    )

    so_input = TextInput(
        display_text='SO42-',
        name='so'
    )

    sio_input = TextInput(
        display_text='SiO2',
        name='sio'
    )

    initial_view = MVView(
        projection = 'EPSG:4326',
        center = [-159.5,22.07],
        zoom=6

    )

    drawing_options = MVDraw(
        controls=['Modify','Delete','Move','Point'],
        initial = 'Point',
        output_format = 'GeoJSON',
        point_color = '#FF0000'

    )

    location_input = MapView(
        height='300px',
        width='100%',
        basemap='OpenStreetMap',
        draw=drawing_options,
        view=initial_view
    )

    add_button = Button(
        display_text='Add',
        name='add-button',
        icon='glyphicon glyphicon-plus',
        style='success',
        attributes={'form': 'add-sample-form'},
        submit=True
    )

    cancel_button = Button(
        display_text='Cancel',
        name='cancel-button',
        href=reverse('waimea_flux:home')
    )

    context = {
        'sampleid_input': sampleid_input,
        'river_input': river_input,
        'datecol_input': datecol_input,
        'timecol_input':timecol_input,
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
        'location_input':location_input,
        'location_error':location_error,
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
