from closer import Closer

class ColaCloser(Closer):
    def ColaCloser(self):
        print('Создали крышку Кола')

    def copy(self):
        return ColaCloser()
