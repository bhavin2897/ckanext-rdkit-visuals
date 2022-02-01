# encoding: utf-8

from six import text_type
from sqlalchemy import orm, types, Column, Table, ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy

from ckan.model import (
    meta,
    core,
    package as _package,
    extension,
    domain_object,
    types as _types,
)


__all__ = [u'MolecularData', u'molecule_data_table']

molecule_data_table = Table(u'molecule_data', meta.metadata,
                Column(u'id', types.Integer, primary_key = True, nullable = False),
                Column(u'package_id', types.UnicodeText, ForeignKey('package.id'), nullable = False),
                Column(u'inchi',types.UnicodeText),
                Column(u'smiles',types.UnicodeText),
                Column(u'inchi_key', types.UnicodeText),
                Column(u'exact_mass', types.Float)
        )



class MolecularData(domain_object.DomainObject):
    def __init__(self, related_object):
        self.package_id = related_object.get('package_id')
        self.inchi = related_object.get('inchi')
        self.smiles = related_object.get('smiles')
        self.inchi_key = related_object.get('inchi_key')
        self.exact_mass = related_object.get('exact_mass')




meta.mapper(
    MolecularData,
    molecule_data_table,
    properties={
        u"package": orm.relation(
            _package, backref=orm.backref(u"molecule_data", cascade=u"all, delete, delete-orphan")
        )
    },
)

