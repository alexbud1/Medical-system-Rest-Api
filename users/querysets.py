from ast import Is
from operator import is_
from django.db import models

class Boys16Queryset(models.QuerySet):

    def boys16(self):
       boys1to16 = []
       boys = self.filter(sex = "Male")
       for boy in boys:
        if boy.id not in boys1to16 and (boy.clients_age() < 16 and boy.clients_age() > 1) and boy.is_disabled == False:
            boys1to16.append(boy.id)
       return self.filter(id__in = boys1to16)

    def girls(self):
        girls_ids = []
        girls = self.filter(sex = "Female")
        for girl in girls:
            if girl.id not in girls_ids and (girl.clients_age() < 18 and girl.clients_age() > 1) and girl.is_disabled == False:
                girls_ids.append(girl.id)
        return self.filter(id__in = girls_ids)

    def guys18(self):
        guys_ids = []
        guys = self.filter(sex = "Male")
        for guy in guys:
            if guy.id not in guys_ids and (guy.clients_age() < 18 and guy.clients_age() >= 16) and guy.is_disabled == False:
                guys_ids.append(guy.id)
        return self.filter(id__in = guys_ids)

    def children(self):
        children_ids = []
        all_children = self.all()
        for child in all_children:
            if child.id not in children_ids and (child.clients_age() <= 1 and child.clients_age() >= 0) and child.is_disabled == False:
                children_ids.append(child.id)
        return self.filter(id__in = children_ids)

    def disabled(self):
        return self.filter(is_disabled = True)
        