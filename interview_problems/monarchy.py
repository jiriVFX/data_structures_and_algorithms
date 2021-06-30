# Interface design - design a monarchy class and methods

# time complexity - O(n) - number of members of family
# space complexity - O(n) - number of members of family
class Member:
    def __init__(self, name, sex):
        self.name = name
        self.alive = True
        self.sex = sex
        self.children = []


class Monarchy:
    def __init__(self, ruler):
        self.ruler = ruler
        self.members = {self.ruler.name: self.ruler}

    def birth(self, child, parent, sex):
        new_member = Member(child, sex)
        self.members[new_member.name] = new_member
        # add child to the parent's children list
        self.members[parent].children.append(new_member)

    def death(self, name):
        if self.members[name] and self.members[name].alive:
            self.members[name].alive = False

    def get_succession_order(self):
        succession_order = []
        # call preorder DFS
        self.preorder_dfs(self.ruler, succession_order)
        # return the list with successors
        return succession_order

    def preorder_dfs(self, member, order_list):
        # if the member of family is alive and is male (only males were legitimate successors at that time)
        if member.alive and member.sex == "male":
            # add to succession order list
            order_list.append(member.name)
            # run DFS on all children
            for child in member.children:
                self.preorder_dfs(child, order_list)


# test the code --------------------------------------------------------------------------------------------------------
king = Member("Premysl Ottokar I.", "male")
monarchy = Monarchy(king)

monarchy.birth("Vratislav", "Premysl Ottokar I.", "male")
monarchy.birth("Dagmar", "Premysl Ottokar I.", "female")
monarchy.birth("Vaclav I.", "Premysl Ottokar I.", "male")

monarchy.death("Vratislav")

monarchy.birth("Vladislav", "Vaclav I.", "male")
monarchy.birth("Bozena", "Vaclav I.", "female")
monarchy.birth("Anezka", "Vaclav I.", "female")
monarchy.birth("Premysl Ottokar II.", "Vaclav I.", "male")

monarchy.death("Vladislav")

print(monarchy.get_succession_order())

