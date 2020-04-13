import os
import uuid
import json


def add_new_dam(db_directory, name, owner, river, date_built):
    """
    Persist new dam.
    """
    # Serialize data to json
    new_dam_id = uuid.uuid4()
    dam_dict = {
        'id': str(new_dam_id),
        'name': name,
        'owner': owner,
        'river': river,
        'date_built': date_built
    }

    dam_json = json.dumps(dam_dict)

    # Write to file in {{db_directory}}/dams/{{uuid}}.json
    # Make dams dir if it doesn't exist
    dams_dir = os.path.join(db_directory, 'dams')
    if not os.path.exists(dams_dir):
        os.mkdir(dams_dir)

    # Name of the file is its id
    file_name = str(new_dam_id) + '.json'
    file_path = os.path.join(dams_dir, file_name)

    # Write json
    with open(file_path, 'w') as f:
        f.write(dam_json)
