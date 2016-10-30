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
Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

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

    # Get all models, pre-load brand relationship
    models = Model.query.options(db.joinedload('brand')).filter(Model.year == year).all()

    # for every model, print name, brand, and hq
    if models:
        for model in models:
            print ( "Model name: %s, Brand name: %s, Headquarters: %s" 
                    % (model.name, model.brand_name, model.brand.headquarters))
    else:
        print "No Models for that year"

    ## Alternate Way ##

    # models = (db.session
    #          .query(Model.name, Model.brand_name, Brand.headquarters)
    #          .join(Brand)
    #          .filter(Model.year==year).all())
    # if models:
    #     for model in models:
    #         print ", ".join(model)
    # else:
    #     print "No Models for that year"
    
 
def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    # Query for all brands, preload models relationship
    brands = Brand.query.options(db.joinedload('models')).all()

    # For each brand, print brand name, model, model year
    for brand in brands:
        print brand.name

        if brand.models:
            for model in brand.models:
                print "\t %s, %s" % (model.name, model.year)
        else:
            print "\t No Models"

    # # Alternate Way ##

    # # Query for All Cars
    # cars = db.session.query(Brand.name, Model.name, Model.year).outerjoin(Model).all()
    
    # # Create Car Dictionary
    # from collections import defaultdict
    # all_cars = defaultdict(list)

    # for brand, model, year in cars:
    #     all_cars[brand].append((model,year))
    
    # # Print Car Dictionary
    # for brand, models in all_cars.iteritems():
    #     print brand
    #     if models[0][0]:
    #         for model, year in models:
    #             print "\t %s, %s" % (model, year)
    #     else:
    #         print "\t No Models"
    
# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# The datatype is a Flask SQLAlchemy query object (flask_sqlalchemy.BaseQuery). 
# It doesn't have a value yet 
# but has a bunch of methods/attributes that can be called upon it. 
# Once it is executed, the value will either be a list of one Brand 
# object if the .all  method is used, or just the Brand object if .one() is used

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# An association table is a table that simply links two tables together,
# resolving one many-to-many relationship into two one-to-many relationships.
# It differs from a middle table in that it stores no other information other 
# than that necessary to link the two tables. It is necessary to use assocation 
# tables, as many-to-many relationships are almost impossible to manage 
# in a relationshal database.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """Design a function in python that takes in any string as parameter, 
    and returns a list of objects that are brands whose name contains or is 
    equal to the input string."""

    search_term = '%{}%'.format(mystr)
    return Brand.query.filter(Brand.name.like(search_term)).all()

    ## Alternate:
    # return Brand.query.filter(Brand.name.like('%{}%'format(mystr))).all()




def get_models_between(start_year, end_year):
    """Design a function that takes in a start year and end year (two integers),
     and returns a list of objects that are models with years that fall between 
     the start year (inclusive) and end year (exclusive)."""

    return Model.query.filter(Model.year.in_(range(start_year, end_year))).all()

    ## Alternate:
    # return Model.query.filter(Model.year.between(start_year,end_year-1)).all()


