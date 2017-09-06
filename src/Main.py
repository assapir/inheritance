#!/usr/bin/env python2

from Person import Person


def find_heir_downward(person):
    """

    :type person: Person
    """
    if person.is_alive():
        return person

    for son in person.get_sons() or []:
        heir = find_heir_downward(son)
        if heir is not None:
            return heir

    for daughter in person.get_daughters() or []:
        heir = find_heir_downward(daughter)
        if heir is not None:
            return heir

    return None


def find_heir(person):
    """

    :type person: Person
    """
    heir = find_heir_downward(person)
    if heir is not None:
        return heir

    return find_heir(person.get_parent())


if __name__ == '__main__':
    robb = Person("Robb", None, None, False)
    bran = Person("Brandon", None, None, True)
    rickon = Person("Rickon", None, None, False)
    sansa = Person("Sansa", None, None, True)
    arya = Person("Arya", None, None, True)
    jon = Person("Jon", None, None, True)

    ned = Person("Eddard", [robb, bran, rickon, jon], [sansa, arya], False)
    for child in ned.get_children():
        child.set_parent(ned)

    print find_heir(ned)
