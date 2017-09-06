class Person:
    def __init__(self, name, parent, sons=[], daughters=[]):
        self.mName = name
        self.mParent = parent
        self.mSons = sons
        self.mDaughters = daughters

    def __str__(self):
        return self.mName

    def get_sons(self):
        return self.mSons

    def get_daughters(self):
        return self.mDaughters

    def get_parent(self):
        return self.mParent

    def get_name(self):
        return self.mName

    def is_alive(self):
        return True