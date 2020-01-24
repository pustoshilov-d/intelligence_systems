import  numpy as np
import random
import math

class DNA:
    def __init__(self, str, N):
        self.N_genes = len(str)
        self.str = str
        self.STR = self.ordVecView(self.str)
        self.N_chromo = N
        self.k_population = 0
        self.population = np.array([0]*self.N_chromo*self.N_genes).reshape(self.N_chromo, self.N_genes)
        self.populationNew = np.array([0]*self.N_chromo*self.N_genes).reshape(self.N_chromo, self.N_genes)
        self.populationInit()
        self.F_res = np.array([0.0]*self.N_chromo)
        self.F_sum = 0.0
        self.F_mean = 0.0

    def charVecView(self, X):
        res = np.array([""]*len(X))
        for i in range(len(X)):
            res[i] = chr(X[i])
        return res

    def ordVecView(self, X):
        res = np.array([0]*len(X))
        for i in range(len(X)):
            res[i] = ord(X[i])
        return res

    def populationInit(self):
        for i in range(self.N_chromo):
            for j in range(self.N_genes):
                self.population[i,j] = random.randint(ord("0"),ord("z"))
        print(self.population)
        print(np.shape(self.population))

    def fetch(self, X):
        return np.sum(np.abs(self.STR - X))

    def selection(self):
        for i in range(self.N_chromo):
            self.F_res[i] = self.fetch(self.population[i])

        self.F_sum = np.sum(self.F_res)
        self.F_mean = np.mean(self.F_res)

        k = 0
        for i in range(self.N_chromo):
            self.populationNew[i] = self.population[np.argmin(self.F_res)]


    def crossover(self):
        #простой 70%
        N = int(self.N_chromo*0.5 / 2)
        for i in range(N):
            i_rand = random.randint(0, self.N_chromo - 2)
            j_rand = random.randint(0, self.N_chromo - 2)
            save = self.populationNew[i_rand]
            self.populationNew[i_rand] = np.concatenate((save[0:j_rand],self.populationNew[i_rand+1][j_rand:]))
            self.populationNew[i_rand+1] = np.concatenate((self.populationNew[i_rand+1][0:j_rand],save[j_rand:]))


    def mutation(self):
        #равномерного распределения 30%
        N = int(self.N_chromo*0.5)

        for i in range(N):
            i_rand = random.randint(0,self.N_chromo-1)
            x_new = int(random.random()*(ord("z") - ord("0")) + ord("0"))
            j_new = random.randint(0,self.N_genes-1)
            self.population[i_rand][j_new] = x_new


    def eval(self):
        Ostanov = False
        epoche = 0
        while not Ostanov:
            # print("old: ", self.population)
            self.selection()
            print("after select: ", self.populationNew)
            # print("old res: ", self.F_res)
            print("sum: ", np.sum(self.F_res))
            self.crossover()
            # print("after cross: ", self.populationNew)
            self.mutation()
            # print("after mutation: ", self.populationNew)
            self.population = self.populationNew
            epoche += 1

            print("Эпоха: ", epoche)
            for i in range(self.N_chromo):
                if self.fetch(self.population[i]) == 0:
                    Ostanov = True
                    print("Solution is found: ", self.charVecView(self.population[i]))



if __name__ == '__main__':
    dNA = DNA("ILovePython",10)
    dNA.eval()