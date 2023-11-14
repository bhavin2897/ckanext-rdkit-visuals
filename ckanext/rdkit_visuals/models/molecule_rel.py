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

__all__ = [u'MolecularRelationData', u'molecule_rel_data_table']

molecule_rel_data_table = Table(u'molecule_rel_data', meta.metadata,
                            Column(u'id', types.Integer, primary_key=True, nullable=False),
                            Column(u'molecule_id', types.UnicodeText, ForeignKey('molecules.id'), nullable = False),
                            Column(u'package_id', types.UnicodeText, ForeignKey('package.id'), nullable=False),)



class MolecularRelationData(domain_object.DomainObject):
    def __init__(self, related_object):
        self.package_id = related_object.get('package_id')
        self.molecule_id = related_object.get('molecule_id')


meta.mapper(
    MolecularRelationData,
    molecule_rel_data_table,
    properties={
        u"package": orm.relation(
            _package, backref=orm.backref(u"molecules", cascade=u"all, delete, delete-orphan")
        )
    },
)
