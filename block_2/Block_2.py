
#1. Declara una variable de cada tipo simple y complejo e imprímelas.
myint = 12
myfloat = 9.81
mystring = "hi"
mybool1 = True
mybool2 = False

print(myint)
print(myfloat)
print(mystring)
print(mybool1)
print(mybool2)

mylist = [12,25,30]
mytupple = (11, "september",2001)
mydict = {"name": "albert", "date": 12}
print(mylist)
print(mytupple)
print(mydict)


print("____________________________")
# 2. Crea una lista con 5 elementos. 
#Imprime el primero, el último y lista[1:4]. 
# ✓ lista[0], lista[-1], lista[1:4]

mylist1 = [11,12,31,65,34]

print(mylist1[1:4])
print(mylist1[0])
print(mylist1[-1])


print("________________________________________")
# 3. Crea una clase con un método que declare un str, una list y un dict. 
#✓ Imprimir: primer carácter del texto, último elemento de la lista, valor de una clave del dict. 

class ant():
    def __init__(self,str2,list3,dict2):
        self.str = str2
        self.list3 = list3
        self.dict2 = dict2

    def GreetList(self):
        print(f"first character of text is: {self.str[0]}")
        print(f"last item on the list is: {self.list3[-1]}")
        print(f"value of a dictionary key is: {self.dict2['name1']}")


mylist3 = ant("valheim", [1,2,3,], {"name1": "robert"})

mylist3.GreetList()
