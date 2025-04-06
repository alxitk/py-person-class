class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    friends = [Person(friend["name"], friend["age"]) for friend in people]

    for i in people:
        instance_person = Person.people[i["name"]]
        if i.get("wife"):
            instance_person.wife = Person.people.get(i["wife"])
        if i.get("husband"):
            instance_person.husband = Person.people.get(i["husband"])

    return friends
