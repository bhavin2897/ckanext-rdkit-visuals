import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from flask import render_template
import json
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from PIL import Image
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole


import io
import base64


DB_HOST = "localhost"
DB_USER = "ckan_default"
DB_NAME = "ckan_default"
DB_pwd = "123456789"

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

         # molecule_formula = None

        package = toolkit.get_action('package_show')({}, {'name_or_id': package_name})
        package_id = package['id']
        # connect to db
        con = psycopg2.connect(user=DB_USER,
                               host=DB_HOST,
                               password=DB_pwd,
                               dbname=DB_NAME)

        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        # Cursor
        cur = con.cursor()

        # Check if the row already exists, if not then INSERT

        cur.execute("SELECT mol_formula FROM molecule_data WHERE package_id = %s", (package_id,))
        molecule_formula = cur.fetchone()
        # commit cursor
        con.commit()
        # close cursor
        cur.close()
        # close connection
        con.close()
        return molecule_formula[0]

    def alternames(package_name):
        alternate_names =[]
        package = toolkit.get_action('package_show')({}, {'name_or_id': package_name})
        package_id = package['id']

        try:
        # connect to db
            con = psycopg2.connect(user=DB_USER,
                                   host=DB_HOST,
                                   password=DB_pwd,
                                   dbname=DB_NAME)

            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            # Cursor
            cur = con.cursor()

            # Check if the row already exists, if not then INSERT


            cur.execute("SELECT alternate_name FROM related_resources WHERE package_id = %s", (package_id,))
            alternate_names_list = cur.fetchall()

            # commit cursor
            con.commit()
            # close cursor
            cur.close()
            # close connection
            con.close()
            for x in alternate_names_list:
                names = "('')".join(x)
                alternate_names.append(names)

        except TypeError:
            pass

        return alternate_names


    def related_resources(package_name):

        rel_values = []
        package = toolkit.get_action('package_show')({}, {'name_or_id': package_name})
        package_id = package['id']

        try:
            # connect to db
            con = psycopg2.connect(user=DB_USER,
                                   host=DB_HOST,
                                   password=DB_pwd,
                                   dbname=DB_NAME)

            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            # Cursor
            cur = con.cursor()

            # Check if the row already exists, if not then INSERT

            cur.execute("SELECT relation_id, relation_type FROM related_resources WHERE package_id = %s", (package_id,))

            rel_values = cur.fetchall()


            # commit cursor
            con.commit()
            # close cursor
            cur.close()
            # close connection
            con.close()

        except:
            pass

        if any(None in elem for elem in rel_values):
            return None
        else:

            return rel_values





