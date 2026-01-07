class OA:
    def _init_(self,n1=0,n2=0):
        self.n1=n1
        self.n2=n2

    def s_d_n(self):
        return self.n1 + self.n2

n1= int(input("Ingrese el primer Numero: "))
n2= int(input("Ingrese el segundo Numero: "))

operaciones=OA(n1,n2)
print("la suma es: ", operaciones.s_d_n())