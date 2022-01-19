import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


from PIL import Image
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole


import io
import base64


class RdkitVisualsController():
    def display_image(package_name):
        # package_name = request.form.get('package')
        package = toolkit.get_action('package_show')({}, {'name_or_id': package_name})
        inchi_key = package['inchi_key']

        filepath = '/var/lib/ckan/default/storage/images/' + str(inchi_key) + '.png'
        file = open(filepath, 'rb').read()
        image = Image.open(io.BytesIO(file))
        output = io.BytesIO()
        image.save(output, 'PNG')
        output.seek(0)
        byteimage = base64.b64encode(output.getvalue()).decode()

        return byteimage
