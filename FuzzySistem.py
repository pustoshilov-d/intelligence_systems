import numpy as np

class FuzzySistem:
    def __init__(self, s, v):
        self.s = s
        self.v = v
        self.t = 0.0
        self.VALUES = ["Нуль, близкое к нулю", "Положительное, близкое к нулю",
                       "Положительное малое", "Положительное среднее", "Положительное большое"]
        self.num_val = 5

    def eval(self):
        #фазификация s
        self.S = int(((self.s-1) / (501-1))*self.num_val)
        print("Тормозной путь: " + self.VALUES[self.S])

        #фазификация v
        self.V = int(((self.v - 1) / (121 - 1))*self.num_val)
        print("Скорость: " + self.VALUES[self.V])

        #правила формируются по типу
        #S=PB and V=PB => T=PS
        #S=PB and V=Z => T=PB
        #S=Z and V=PB => T=Z
        #из-за прямой зависимости T от S и обратной — от V

        #агрегирование, активация, аккамуляция
        self.T = int(self.formula(self.S+1, self.V+1)/(10-0.4)*4+0.4)
        print("Время торможения: " + self.VALUES[self.T])

        #дефазификация T
        self.t = (self.T * (self.formula(501,1) - 1)/self.num_val + 1)
        print("Время торможения: "+ str(int(self.formula(self.s, self.v))))

    def formula(self, s, v):
        return s*2/v

if __name__ == '__main__':
    s = float(input("Введите тормозной путь (от 1 до 500м): "))
    v = float(input("Введите скорость автомобиля (от 1 до 120м/мин): "))
    fuzzySistem = FuzzySistem(s,v)
    fuzzySistem.eval()


