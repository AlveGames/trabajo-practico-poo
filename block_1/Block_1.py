def run():
    
    #  1. Crea la clase Producto con código, nombre y precio. Instancia 2 productos. 
    #      ✓ Producto("P001","Laptop",900) y Producto("P002","Mouse",25). 
    #   2. Agrega validación para que el precio no sea negativo. 
    #      ✓ if precio < 0: raise ValueError(...) 
    class Product():
        def __init__(self,code,name,price):
    
            if price < 0:
                raise ValueError("Error: the price cannot be negative")
        
            self.code = code
            self.name = name
            self.price = price
    
        def display(self):  
                print (f"The product ID is: {self.code} ...with the name of: {self.name} ...at a price of: {self.price}")
    
    prod1 = Product("r1", "camera" , 50)
    prod2 = Product("r2", "chair" , 21)
    prod3 = Product("r3", "bed" , 180)
    
    prod1.display()
    #   3. Crea Estudiante con nombre y notas=None. Si no hay notas, inicia lista vacía. 
    #      ✓ if notas is None: self.notas = [] 
    #   4. Agrega un @classmethod desde_diccionario que cree un Estudiante desde un dict.
    
    class Estudent():
        def __init__(self,name ,notes = None):
    
            if notes is None:
                self.notes = []
            else:
                self.notes = notes
                
            self.name = name
    
        def display1(self):
            print(f"estudent: {self.name} note: {self.notes}")
    
            
        @classmethod 
        def from_dictionary(cls, data):
            return cls(data["name"], data["notes"])
    
    est1 = Estudent("keni", [8, 9, 10])
    est1.display1()
    
    data = {"name": "caiza", "notes": [7,8,9]}
    est2 = Estudent.from_dictionary(data)
    
    est2.display1()
