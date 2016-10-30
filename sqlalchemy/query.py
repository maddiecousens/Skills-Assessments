"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries

#1############################################################################

# Get the brand with the **id** of 8.
Brand.query.get(8)

## Alternate Ways ##
# db.session.query(Brand).get(8)

#2############################################################################

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name=='Corvette', Model.brand_name=='Chevrolet').all()

## Alternate Ways ##
# Model.query.filter_by(brand_name='Chevrolet', name='Corvette').all()
# db.session.query(Model).filter(Model.brand_name=='Chevrolet', Model.name=='Corvette').all()
# db.session.query(Model).filter_by(brand_name='Chevrolet', name='Corvette').all()

#3############################################################################

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

## Alternate Ways ##
# db.session.query(Model).filter(Model.year < 1960).all()

#4############################################################################

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

## Alternate Ways ##
# db.session.query(Brand).filter(Brand.founded > 1920).all()


#5############################################################################

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

## Alternate Ways ##
# db.session.query(Model).filter(Model.name.like('Cor%')).all()

#6############################################################################

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()

## Alternate Ways ##
# Brand.query.filter(Brand.founded==1903, Brand.discontinued == None).all()
# Brand.query.filter( (Brand.founded==1903) & (Brand.discontinued.is_(None)) ).all()
# Brand.query.filter( (Brand.founded==1903) & (Brand.discontinued == None) ).all()
# db.session.query(Brand).filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()

#7############################################################################

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter( (Brand.discontinued != None) | (Brand.founded < 1950)).all()

## Alternate Ways ##
# Brand.query.filter( (Brand.discontinued.isnot(None) | (Brand.founded < 1950)).all()
# Brand.query.filter( db.or_(Brand.discontinued != None, Brand.founded < 1950) ).all()
# Brand.query.filter( db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950) ).all()
# db.session.query(Brand).filter( (Brand.discontinued != None) | (Brand.founded < 1950)).all()


#8############################################################################

# Get all models whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()
## Alternate Ways ##
# Model.query.filter(~ Model.brand_name.in_(['Chevrolet'])).all()
# Model.query.filter( db.not_(Model.brand_name.in_(['Chevrolet'])) ).all()
# db.session.query(Model).filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    pass

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    pass

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass
