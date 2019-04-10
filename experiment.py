'''
    created on 05 April 2019
    
    @author: Gergely
'''
import aspectlib


@aspectlib.Aspect
def make_return_none(*args, **kwargs):
    result = yield aspectlib.Proceed
    print("result would have been " + result)
    yield aspectlib.Return


@aspectlib.Aspect
def make_return_something_else(*args, **kwargs):
    result = yield aspectlib.Proceed
    # print(result + " ahoy")
    yield aspectlib.Return("modified return")


@aspectlib.Aspect
def modify_param(*args, **kwargs):
    result = yield aspectlib.Proceed(args, "Noname")
    yield aspectlib.Return(result)


class Hero:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.points = 100

    def __str__(self):
        return str(self.name)

    # @make_return_none
    @modify_param
    def say_hello(self, target):
        return str(self) + " greets " + str(target)

    @make_return_something_else
    def say_something(self):
        return "exorcizamus te omnis imundus spiritus"


hero = Hero("Galaxon, Dark Lord of All", "Captain")
hero2 = Hero("Zeta", "Commander")
print(hero.say_hello(hero2))
# print(hero.say_something())
# print(hero.say_hello(hero2))
