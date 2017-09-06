class Person:
    def __init__(self, name, sons, daughters, is_alive=True):
        self.mName = name
        self.mSons = sons
        self.mDaughters = daughters
        self.mParent = None
        self.isAlive = is_alive

    def __str__(self):
        return self.mName

    def set_parent(self, parent):
        self.mParent = parent

    def get_parent(self):
        return self.mParent

    def get_sons(self):
        return self.mSons

    def get_daughters(self):
        return self.mDaughters

    def get_children(self):
        return self.mSons + self.mDaughters

    def get_name(self):
        return self.mName

    def is_alive(self):
        return self.isAlive

    def kill(self):
        self.isAlive = False

    def fire_magic(self):
        self.isAlive = True
