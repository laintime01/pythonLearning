from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}) {self.firstname}{self.lastname} ({self.gender},{self.age})"


class Thing(Base):
    __tablename__ = 'things'

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

p1 = Person(111, "Mike", "Smith", "m", 38)
p2 = Person(222, "Bob", "Sum", "fm", 28)
p3 = Person(333, "Andy", "Wong", "m", 12)
# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.commit()

result =session.query(Person).all()
# filter_result = session.query(Person).filter(Person.age > 10)
for r in result:
    print(r)

t1 = Thing(1, "car", p1.ssn)
t2 = Thing(2, "laptop", p2.ssn)
t3 = Thing(3, "macbook", p3.ssn)
# session.add(t1)
# session.add(t2)
# session.add(t3)
# session.commit()

results = session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(Person.lastname == "Wong").all()
for r in results:
    print(r)
