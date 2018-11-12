from models import *
from sqlalchemy import create_engine, func
engine = create_engine('sqlite:///weed.db')
Session = sessionmaker(bind=engine)
session = Session()

def strain_names_by_race(race):
    objs = session.query(Strain).filter(Strain.race == race).all()
    names = list(map(lambda o: o.name, objs))
    return names

def strain_names_by_flavor(flavor):
    objs = session.query(Flavor).filter(Flavor.name == flavor).first().strains
    names = list(map(lambda o: o.name, objs))
    return names

def strain_names_by_effect(effect):
    objs = session.query(Effect).filter(Effect.name == effect).first().strains
    names = list(map(lambda o: o.name, objs))
    return names