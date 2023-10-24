from abc import ABCMeta, abstractmethod
from database import Database


# this is an interface because it defines what a subclass must do
class Saveable(metaclass=ABCMeta):

    #provides a functionality that will be shared across subclasses
    def save(self):
        Database.insert(self.to_dict())

    @abstractmethod
    def to_dict(self):
        pass
