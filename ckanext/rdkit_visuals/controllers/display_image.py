import base64
import io

import ckan.plugins.toolkit as toolkit
from PIL import Image
from ckanext.related_resources.models.related_resources import RelatedResources as related_resources
from ckanext.rdkit_visuals.models.molecule_rel import MolecularRelationData as molecule_rel

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

    def molecule_data(package_name):

        molecule_formula = []

        package = toolkit.get_action('package_show')({}, {'name_or_id': package_name})
        package_id = package['id']

        molecule_formula_list = molecule_rel.get_mol_formula_by_package_id(package_id)


        try:
            for x in molecule_formula_list:
                molecule_formula = "['']".join(x)

        except TypeError:
            pass

        return molecule_formula

    def alternames(package_name):
        alternate_names = []
        package = toolkit.get_action('package_show')({}, {'name_or_id': package_name})
        package_id = package['id']

        try:
            alternate_names_list = related_resources.get_alternate_names_by_package_id(package_id)

            for x in alternate_names_list:
                names = "('')".join(x)
                alternate_names.append(names)
        except TypeError:
            pass
            # If NONE passed

        return alternate_names

    def related_resources(package_name):

        rel_values = []
        package = toolkit.get_action('package_show')({}, {'name_or_id': package_name})
        package_id = package['id']

        try:
            rel_values = related_resources.get_relation_values_by_package_id(package_id)

        except Exception:
            pass

        if any(None in elem for elem in rel_values):
            return None
        else:

            return rel_values
