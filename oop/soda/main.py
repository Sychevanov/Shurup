
from colaFactory import ColaFactory
from sodaBuilder import SodaBuilder
factory = ColaFactory()
builder = SodaBuilder(factory)
builder.pourSoda()
builder.putLabel()
builder.seal()
bottle1 = builder.build()
bottle2 = builder.build()

