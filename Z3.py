class Tomato:
    states= {1:'Зеленый',2:'Желтоватый',3:'Спелый'}
    key=1
    def __init__(self,index):
        self.index=index
        self.state=Tomato.states[Tomato.key]
    def show_index(self):
         self.index+=1
         return self.index
    def grow(self):
        Tomato.key += 1
        print('Томат  перешел на стадию созревания ',Tomato.states[Tomato.key])
        if Tomato.key==3:
            Tomato.key=1

    def is_ripe(self):
        if  self.key==len(Tomato.states):
            print('Томат  перешел на последнюю стадию созревания ')
            return True
        elif self.key<len(Tomato.states):
            print('Томат находится на стадии ',Tomato.states[Tomato.key])
            return False
        else:
            print("Ваш томат давно перезрел ")
            return False

class TomatoBush:
    def __init__(self,kolTom):
        self.kolTom=kolTom
        self.tomatoes=list()
    def add_list(self,list_tomato):
        self.tomatoes.append(list_tomato)
    def show_list(self):
        print('Список объектов томат')
        for list_tomato in self.tomatoes:
            list_tomato.is_ripe()
    def grow_all(self):
        Tomato.key += 1
        for i in range(1,len(self.tomatoes)+1):
            print('Томат',i, 'перешел на стадию созревания ', Tomato.states[Tomato.key])
    def all_are_ripe(self):
        for list_tomato in self.tomatoes:
            if list_tomato.is_ripe()==False:
                return False
        else:
            return True
    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name,_plant):
        self.name = name
        self._plant = _plant
    def work(self):
        print('Садовник работает,растения перешли на след.стадию созревания ')
        self._plant.grow_all()

    @staticmethod
    def knowledge_base():
        print('У томатов две стадии зрелости: техническая и биологическая. И не прекращаются споры о том, в какой из них плоды снимать правильнее. Что ж, давайте разберемся.')

    def harvest(self):
        if self._plant.all_are_ripe():
            print('Все томаты созрели, убираем урожай ')
            self._plant.give_away_all()
        else:
            print('не все томаты созрели,поработаем еще')

objectTom=Tomato(3)
TomatoBush_obj=TomatoBush(5)
Object_Gard=Gardener('Ivan',TomatoBush_obj)
ind=1
for i in range(TomatoBush_obj.kolTom):
    objectTom = Tomato(ind)
    objectTom.show_index()
    TomatoBush_obj.add_list(objectTom)
TomatoBush_obj.show_list()
Object_Gard.work()
Object_Gard.harvest()
Object_Gard.work()
Object_Gard.harvest()
print('куст пуст')
print(TomatoBush_obj.tomatoes)






























