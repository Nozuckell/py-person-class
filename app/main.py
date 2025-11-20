class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_one in people:
        name = person_one["name"]
        age = person_one["age"]
        one_person = Person(name, age)
        person_list.append(one_person)
    for p_two in people:
        p_name = p_two["name"]
        p_obj = Person.people[p_name]
        if p_two.get("wife") is not None:
            p_wife_name = p_two["wife"]
            wife_obj = Person.people[p_wife_name]
            p_obj.wife = wife_obj
        if p_two.get("husband") is not None:
            p_husband_name = p_two["husband"]
            husband_obj = Person.people[p_husband_name]
            p_obj.husband = husband_obj
    return person_list
