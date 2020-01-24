import numpy as np

class persept:
    def __init__(self, w):
        self.w = np.array(w)

    def eval(self, input):
        self.input = np.array(input)
        self.NET = sum(self.input*self.w)

        return int(self.NET >= 0)


if __name__ == '__main__':
    print("\nИ")
    pers = persept([1,1,-3/2])
    print("1 1 ",pers.eval([1,1,1]))
    print("0 1 ",pers.eval([0,1,1]))
    print("1 0 ",pers.eval([1,0,1]))
    print("0 0 ",pers.eval([0,0,1]))

    print("\nИЛИ")
    pers = persept([1,1,-1/2])
    print("1 1 ",pers.eval([1,1,1]))
    print("0 1 ", pers.eval([0, 1, 1]))
    print("1 0 ", pers.eval([1, 0, 1]))
    print("0 0 ", pers.eval([0, 0, 1]))



    print("\nНЕ-ИЛИ")
    pers1 = persept([1,1,1/2])
    pers2 = persept([1, 1, 3/2])
    pers3 = persept([1, -1, 1/2])


    X0 = -1
    X1 = 1
    X2 = 1
    print(X1, X2, pers3.eval([pers1.eval([X1,X2,X0]), pers2.eval([X1,X2,X0]), X0]))
    X1 = 1
    X2 = 0
    print(X1, X2,pers3.eval([pers1.eval([X1,X2,X0]), pers2.eval([X1,X2,X0]), X0]))
    X1 = 0
    X2 = 1
    print(X1, X2,pers3.eval([pers1.eval([X1,X2,X0]), pers2.eval([X1,X2,X0]), X0]))
    X1 = 0
    X2 = 0
    print(X1, X2,pers3.eval([pers1.eval([X1,X2,X0]), pers2.eval([X1,X2,X0]), X0]))