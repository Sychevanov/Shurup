from label import Label
class ColaLabel(Label):
    def colaLabel(self):
        print('СОздали Этикетку Кола')
    def copy(self):
        return ColaLabel()