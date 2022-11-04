class Person:
    def __init__(self, name, age, id):
        self.id = id
        self.name = name
        self.age = age

class PersonRepository:
    def __init__(self):
        self.persons = []

    def add(self, person):
        self.persons.append(person)

    def get(self, id):
        for person in self.persons:
            if person.id == id:
                return person
        return None

    def get_all(self):
        return self.persons

    def update(self, old_person, new_person):
        self.delete(old_person.id)
        self.add(new_person)
        raise Exception("Person not found")

    def delete(self, id):
        for p in self.persons:
            if p.id == id:
                self.persons.remove(p)
                return
        raise Exception("Person not found")

# A Person Service class for Person, which is a service layer for PersonRepository
class PersonService:
    def __init__(self, repository):
        self.repository = repository

    def get(self, id):
        return self.repository.get(id)

    def get_all(self):
        return self.repository.get_all()

    def add(self, person):
        self.repository.add(person)

    def update(self, old_person, new_person):
        self.repository.update(old_person, new_person)

    def delete(self, id):
        self.repository.delete(id)

    # OTHER BUSINESS LOGIC CAN BE ADDED HERE
    def get_by_name(self, name):
        for person in self.repository.get_all():
            if person.name == name:
                return person
        return None
    
    # FILTER PERSON BY AGE
    def filter_by_age(self, age):
        persons = []
        for person in self.repository.get_all():
            if person.age == age:
                persons.append(person)
        return persons