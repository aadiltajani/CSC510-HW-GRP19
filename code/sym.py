# import csv
# import math


# class Symclass:

#     n = 0
#     def __init__(self):
#         self.symdict = {}
#         with open('input.csv','r') as f:
#             reader = csv.DictReader(f, delimiter=',')
#             self.rows = list(reader)

    
#     def sym_add(self):
#         listOfOrigins = []
#         for row in self.rows:
#             origin = row['origin']
#             if origin!= "?":
#                 listOfOrigins.append(row['origin'])
#                 self.n+=1
        
#         for origin in listOfOrigins:
#             if origin in self.symdict:
#                 self.symdict[origin]+=1
#             else:
#                 self.symdict[origin] = 1
        
#         # print(self.n)
#         # print(self.symdict)

#         return self.symdict

#     def sym_mid(self):
#         max = -1
#         mode = -1
#         for sym, count in self.symdict.items():
#             if count>max:
#                 max = count
#                 mode = sym
        
#         # print(mode)

#         return mode

#     def sym_div(self):
#         e=0
#         for sym, count in self.symdict.items():
#             if count>0:
#                 p = count/self.n
#                 e = e-p*math.log2(p)
        
#         # print(e)

#         return e



# obj1 = Symclass()
# obj1.sym_add()
# obj1.sym_mid()
# obj1.sym_div()    


import math


class Sym:
    def __init__(self,c=0,s='') -> None:
        self.n = 0
        self.name=s
        self.at=c
        self._has = dict()

    
    def add(self, v):
        if v != '?':
            self.n = self.n + 1
            self._has[v] = 1 + self._has.get(v, 0)


    def mid(self):
        return max(self._has, key=self._has.get)
    

    def div(self):
        fun = lambda p : p*math.log(p,2)
        e = 0  
        for key in self._has.keys():
            if self._has[key] > 0 :
                e = e - fun(self._has[key]/self.n)
        
        return e
