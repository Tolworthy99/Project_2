import os
import uuid
import json


def add_new_data(db_directory, sampleid, river, datecol, timecol, note, pH, temper, cond, ca, mg, na, k, hco, cl, so, sio):
    """
    Persist new dam.
    """
    # Serialize data to json
    new_water_id = uuid.uuid4()
    water_dict = {
        'id': str(new_water_id),
        'sampleid': sampleid,
        'river': river,
        'datecol': datecol,
        'timecol':timecol,
        'note': note,
        'pH': pH,
        'temper': temper,
        'cond': cond,
        'ca': ca,
        'mg': mg,
        'na': na,
        'k': k,
        'hco': hco,
        'cl': cl,
        'so': so,
        'sio': sio
    }

    water_json = json.dumps(water_dict)

    # Write to file in {{db_directory}}/dams/{{uuid}}.json
    # Make dams dir if it doesn't exist
    water_dir = os.path.join(db_directory, 'Water_Data')
    if not os.path.exists(water_dir):
        os.mkdir(water_dir)

    # Name of the file is its id
    file_name = str(new_water_id) + '.json'
    file_path = os.path.join(water_dir, file_name)

    # Write json
    with open(file_path, 'w') as f:
        f.write(water_json)

def get_all_water(db_directory):
    """
    Get all persisted dams.
    """
    # Write to file in {{db_directory}}/dams/{{uuid}}.json
    # Make dams dir if it doesn't exist
    water_dir = os.path.join(db_directory, 'Water_Data')
    if not os.path.exists(water_dir):
        os.mkdir(water_dir)

    waters = []

    # Open each file and convert contents to python objects
    for water_json in os.listdir(water_dir):
        # Make sure we are only looking at json files
        if '.json' not in water_json:
            continue

        water_json_path = os.path.join(water_dir, water_json)
        with open(water_json_path, 'r') as f:
            water_dict = json.loads(f.readlines()[0])
            water.append(water_dict)

    return waters
