from sodaFactory import SodaFactory
from colaBotle import ColaBottle
from colaSoda import ColaSoda
from colaLabel import ColaLabel
from colaCloser import ColaCloser

class ColaFactory(SodaFactory):
    def createBottle(self):
        return ColaBottle()
    def createSoda(self):
        return ColaSoda()
    def createLabel(self):
        return ColaLabel
    def createCloser(self):
        return ColaCloser