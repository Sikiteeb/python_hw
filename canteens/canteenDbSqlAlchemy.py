from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker

# Define the ORM models
Base = declarative_base()


class Provider(Base):
    __tablename__ = 'provider'
    id = Column(Integer, primary_key=True)
    provider_name = Column(String)


class Canteen(Base):
    __tablename__ = 'canteen'
    id = Column(Integer, primary_key=True)
    provider_id = Column(Integer, ForeignKey('provider.id'))
    name = Column(String)
    location = Column(String)
    time_open = Column(String)
    time_closed = Column(String)
    provider = relationship("Provider")


# Create the SQLite database and tables
engine = create_engine('sqlite:///diners_orm.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert the providers and canteens
providers = [
    Provider(id=1, provider_name='Rahva Toit'),
    Provider(id=2, provider_name='Baltic Restaurants Estonia AS'),
    Provider(id=3, provider_name='TTÜ Sport OÜ'),
    Provider(id=4, provider_name='Bitt OÜ'),
]

canteens = [
    Canteen(id=1, provider_id=1, name='Economics- and social science building canteen',
            location='Akadeemia tee 3, SOC-building', time_open='8:30', time_closed='18:30'),
    Canteen(id=2, provider_id=1, name='Library canteen', location='Akadeemia tee 1/Ehitajate tee 7', time_open='8:30',
            time_closed='19:00'),
    Canteen(id=3, provider_id=2, name='Main building Deli cafe', location='Ehitajate tee 5, U01 building',
            time_open='9:00', time_closed='16:30'),
    Canteen(id=4, provider_id=2, name='Main building Daily lunch restaurant', location='Ehitajate tee 5, U01 building',
            time_open='9:00', time_closed='16:30'),
    Canteen(id=5, provider_id=1, name='U06 building canteen', location='', time_open='9:00', time_closed='16:00'),
    Canteen(id=6, provider_id=2, name='Natural Science building canteen', location='Akadeemia tee 15, SCI building',
            time_open='9:00', time_closed='16:00'),
    Canteen(id=7, provider_id=2, name='ICT building canteen', location='Raja 15/Mäepealse 1', time_open='9:00',
            time_closed='16:00'),
    Canteen(id=8, provider_id=3, name='Sports building canteen', location='Männiliiva 7, S01 building',
            time_open='11:00', time_closed='20:00'),
    Canteen(id=9, provider_id=4, name='bitStop KOHVIK', location='IT College, Raja 4c', time_open='9:30',
            time_closed='16:00'),
]

session.add_all(providers)
session.add_all(canteens)
session.commit()

# Query for canteens open from 09:00 to 16:20

canteens_open_9_to_1620 = session.query(Canteen).filter(Canteen.time_open <= '9:00',
                                                        Canteen.time_closed >= '16:20').all()

# Query for canteens serviced by Baltic Restaurants Estonia AS

canteens_baltic_restaurants = session.query(Canteen).join(Provider).filter(
    Provider.provider_name == 'Baltic Restaurants Estonia AS').all()

# Display the queried results

print("Canteens open from 09:00 to 16:20:")
for canteen in canteens_open_9_to_1620:
    print(canteen.id, canteen.name, canteen.location, canteen.time_open, canteen.time_closed)

print("\nCanteens serviced by Baltic Restaurants Estonia AS:")
for canteen in canteens_baltic_restaurants:
    print(canteen.id, canteen.name, canteen.location, canteen.time_open, canteen.time_closed)

# Close the session

session.close()
