#OOP based on 
# https://www.freecodecamp.org/news/how-to-use-oop-in-python/

class Sneaker:
    brand = "Adidas" # class attr.

    #instance attr.
    def __init__(self, color, model):
        self._color = color #private
        self._model = model  #private
    
    #instance meth.

    def cleaning(self):
        print(f"cleaning {self._color} {self._model} sneaker.")

    def putting_back(self):
        print(f"putting back {self._color} {self._model} sneaker.")

    def get_color(self):
        return self._color #private
    
    def set_color(self, new_color):
        self._color =  new_color # _ means private

class VintageSneaker(Sneaker):
    def __init__(self, color, model, year):
        super().__init__(color, model)
        self._year = year

    def sayYear(self):
        print(f"My year is {self._year}.")


s1 = Sneaker("black", "samba")
print(s1)

s2 = Sneaker("red", "superstar")

if s1 == s2:
    print("eq")
else:
    print("not eq")
    print(f"s1 has color {s1._color} and s2 has color {s2._color}.") #not rec. best with get.
    print(f"s1's brand is {s1.brand} and s2's brand is {s2.brand}.")


s1.putting_back()
s2.cleaning()

print("s1 is", s1.get_color() + ".")

s1.set_color("blue")
print("now, s1 is", s1.get_color() + ".")

#instance of vintage s.
vint98 = VintageSneaker("black", "samba", 1998)

vint98.sayYear()