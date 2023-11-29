# encoding: utf-8

from sqlalchemy import Column, ForeignKey, func, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from ckan.model import meta, Package, domain_object
from sqlalchemy import types as _types
from ckan.model import Session
from ckan.model import meta
from .base import Base



class Molecules(Base):
    __tablename__ = 'molecules'

    """
    Molecules is an essential table for storing the molecular information in a database using RDKit visuals while
    harvesting the metadata through CKAN harvesters.
    
    """

    id = Column(_types.Integer, primary_key=True, autoincrement=True)
    package_id = Column(_types.Integer, ForeignKey('package.id'))
    inchi = Column(_types.String)
    smiles = Column(_types.String)
    inchi_key = Column(_types.String)
    exact_mass = Column(Float)
    mol_formula = Column(_types.String)

    # Relationship with the Package model
    #package = relationship('Package')

    # Additional methods can be added here as needed

    @classmethod
    def create(cls, package_id, inchi, smiles, inchi_key, exact_mass, mol_formula):
        """
        Create a new Molecule entry and store it in the database.

        :param package_id: The ID of the package
        :param inchi: InChI string for the molecule
        :param smiles: SMILES string for the molecule
        :param inchi_key: InChI key for the molecule
        :param exact_mass: The exact mass of the molecule
        :param mol_formula: The molecular formula of the molecule
        :param session: The SQLAlchemy session for database interaction
        :return: The created Molecule instance
        """
        new_molecule = cls(
            package_id=package_id,
            inchi=inchi,
            smiles=smiles,
            inchi_key=inchi_key,
            exact_mass=exact_mass,
            mol_formula=mol_formula
        )
        Session.add(new_molecule)
        Session.commit()
        return new_molecule


