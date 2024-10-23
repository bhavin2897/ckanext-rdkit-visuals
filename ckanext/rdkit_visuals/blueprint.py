# encoding: utf-8

from flask import Blueprint, redirect, url_for

from ckan.plugins.toolkit import c, render, request
import ckan.lib.helpers as h
from ckanext.sparql_interface.utils import sparql_query_SPARQLWrapper as utils_sparqlQuery
from flask import Response


rdkit_visuals_blueprint = Blueprint(u'rdkit_visuals',__name__)

@rdkit_visuals_blueprint.add_url_rule(u'/localhost:5000/dataset/<package_name>')
def display_image(package_name):
    return render('')

