[![Tests](https://github.com/BhavHub/ckanext-rdkit-visuals/workflows/Tests/badge.svg?branch=main)](https://github.com/BhavHub/ckanext-rdkit-visuals/actions)

# ckanext-rdkit-visuals

RDKit Module is an Open source toolkit for cheminformatics and Machine Learning. 
Here Rdkit python module is used as an important library extension to CKAN venv to create various cheminformatics, perform and provide various chemical solution from metadata harvested (fetched) from different chemistry repositories. 

More information about RDKit: https://www.rdkit.org/

In this plugin, the major rdkit library must be installed giving an assess to perform chemical logics to create:
InChI
Smiles
InChIKey
Molecule
Molecular Image
Molecular Formula
Exact Mass 

Most of the chemistry repository provide standard InChI key in their metadata fields. We have used this field to create other chemical information to enrich the dataset display and provide more information of the sample or research dataset, as the user can easily go through. 

Not only on the "dataset" page of CKAN, but also on "resource" page. 


Approach while harvesting (For more information about the harvester [OAI-PMH Harvester](https://github.com/bhavin2897/ckanext-oaipmh)): 
- InChI → Smiles
- InChI → InChIKey
- InChI → Molecule
- Molecule → Molecular Image
- Molecule → Molecular Formula
- Molecule → Exact Mass 

## CKAN Crystal Structure Viewer

This CKAN extension enables automatic rendering of 3D crystal structures on dataset pages using `.cif` (Crystallographic Information File) resources. It uses [3Dmol.js](https://3dmol.csb.pitt.edu/) to visualize molecular geometry interactively within the browser.

### Features

- Embeds an interactive 3D viewer when a CIF file is present.
- Displays crystallographic metadata in a styled table.
- Responsive layout for dataset detail pages.
- Works without requiring any CKAN plugin—just a template override.

### Usage

To enable the viewer:

1. Upload a `.cif` file as a resource in your dataset.
2. Ensure metadata (e.g., space group, unit cell dimensions) is stored in `package.extras`.
3. The viewer and metadata table will automatically appear on the dataset page.

### Example Output

- 3D viewer rendered using WebGL
- Metadata like unit cell (`a`, `b`, `c`, `α`, `β`, `γ`), formula, and space group shown alongside

### Dependencies

- [3Dmol.js](https://3dmol.csb.pitt.edu/) (loaded via CDN)

### Acknowledgments

- Visualization powered by [3Dmol.js](https://3dmol.csb.pitt.edu/)
- Inspired by molecular crystal display needs in chemistry research repositories


****
### Data Models and Migration 
This Plugin also contains database migration tables to store molecule data of each dataset molecule in molecule table. 
Name of the database tables: `molecules` & `molecules_rel_data` 

Database Migration is done, to establish new tables within the CKAN PostgreSQL database. For more information please check offical documenation: https://docs.ckan.org/en/2.9/extensions/best-practices.html

**Data Models**
Two data models scripts are sued for interaction with database tables of Molecules and MolecularRelationData. 

1. _Molecules Table_: The data table schema is indexed to store molecule data while harvesting using RDKit Python Library, 
which contains id for every entry and their molecules information. (Highly based on InChIKey)

2. _Molecules Relation Data Table_ : The data table schema is indexed to store moleculesID and their corresponding
package ID. 

The classmethods are designed to store/create rows during each harvesting and also get information via packageID and 
their moelcular information.

***Note***: If you are creating your own migration tables then, Please follow official documentation preciesly. (https://docs.ckan.org/en/2.9/extensions/best-practices.html)

You can copy migration python file and version control files, after creating migration is done. if you are using different table names & column names, please name them using "lower_cases" instead of CamelCase.

****
## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.8 & eariler             | not tested    |
| 2.9             | yes    |


## Installation


To install ckanext-rdkit-visuals:

Activate your CKAN virtual environment, for example:

	. /usr/lib/ckan/default/bin/activate

Clone the source and install it on the virtualenv

	git clone https://github.com/bhavin2897/ckanext-rdkit-visuals.git
	cd ckanext-rdkit-visuals
	pip install -e .
		pip install -r requirements.txt

Add `rdkit-visuals` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

	sudo service apache2 reload
     

To upgrade ckan database, for the tables you have created:
	
	ckan -c /etc/ckan/default/ckan.ini db upgrade -p rdkit-visuals

You will get a message `Upgrading DB: SUCCESS`

Later, check the database list of tables for the ckan user to see the table for the migrated/generated table.


## Config settings

None at present


## Developer installation

To install ckanext-rdkit-visuals for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/bhavin2897/ckanext-rdkit-visuals.git
    cd ckanext-rdkit-visuals
    python setup.py develop
    pip install -r dev-requirements.txt
    
Add Plugin-in int he confirguation file
	
	sudo nano /etc/ckan/default/ckan.ini 
	
	ckan.plugin: <other plugins> rdkit_visuals

Restart Server if you are using Supervisor and Nginx

    sudo service supervisor reload
    sudo service nginx reload 

   
To upgrade ckan database, for the tables you have created:

    ckan -c /etc/ckan/default/ckan.ini db upgrade -p rdkit_visuals

You will get a message `Upgrading DB: SUCCESS`

Later, check the database list of tables for the ckan user to see the table for the migrated/generated table.


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-rdkit-visuals

If ckanext-rdkit-visuals should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
