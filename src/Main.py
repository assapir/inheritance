import Person


def find_heir_downward(person):
    """

    :type person: Person
    """
    if person.is_alive():
        return person

    for son in person.get_sons():
        heir = find_heir_downward(son)
        if heir is not None:
            return heir

    for daughter in person.get_daughters():
        heir = find_heir_downward(daughter)
        if heir is not None:
            return heir

    return None


def find_heir(person):
    heir = find_heir_downward(person)
    if heir is not None:
        return heir

    return find_heir(person.get_parent())
