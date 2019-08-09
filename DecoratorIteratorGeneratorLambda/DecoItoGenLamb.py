

def div(a, b):
    print("div:", a/b)


''' if we want to improve our function div() without changing, we have to use Decorator
'''
def smartDiv(func):

    def inner(a, b):
        if a < b:
            a, b = b, a  # swap a and b
            return func(a, b)

    return inner


# to se the difference look at the console output
div(2, 4)

#now we have to link the smartDiv with Div in order to enhance div()
div = smartDiv(div)

# to se the difference look at the console output
div(2, 4)




'''LAMBDA YANİ ANONYMOUS FUNCTION-------------------------------------------------------------------------
MAKRO GİBİ TANIMLANAN FONKSİYONLARDIR
örnek

f = lambda inputParam : EqnForOutput
f = lambda a : a*a

result = f(5) 
result is 25

'''

#lambda ex 1-----------------------------------------------------
avg = lambda a, b: (a+b)/2
print("average:", avg(3, 5))

#lambda ex 2--------------------------------------------------------

personInfo = lambda name, idNum: "Name:" + name + " Id:" + str(idNum)
print(personInfo("Ali", 1651718))





'''FILTER FUNCTION-------------------------------------------------------------------------
filtreleme fonksiyonunuzu ve input dizinizi parametre olarak alıp
herbir eleman için fonksiyonunuzu çağırıp hesaplatır ve çıkış dizisine kaydeder
yani y=f(x)
f ve x i verirseniz filter size y dizisini verir
'''


def is_even(a):
    return a % 2 == 0


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = list(filter(is_even, nums))
print("nums:", nums)
print("evens:", evens)


#filtreleme process fonksiyonumuzu lambda ile yapalım
evens = list(filter(lambda x: x % 2 == 0, nums))
print("evens:", evens)


singles = list(map(lambda x: x / 2, evens))
print("singles:", singles)

'''
#reduce fonksiyonu process ve dizi param alır,
 dizideki bir sonraki elemanı process fonks ile 
 son hesaplattığı  değerle tekrar process fonksiyonuna tabi tutar
 sonuç son hesaplattığı değerle son elemanın process değerinden geçmiş halidir

aşağıdaki örnekte toplama fonksiyonu reduce yardımıyla yapılmış
yukarıda üretilmiş singles dizisinin elemanlarına (lambda x, y: x+y) ile toplama işlemi
yapılarak sonuç üretilmiştir
singles [a,b,c,d,e,f] ise
reduce iterasyonları
lambda a,b sonucu a+b
lambda a+b,c  sonucu a+b+c
şeklinde devam edip enson:
a+b+c+d+e+f  yi döndürür
'''
from functools import reduce

sum = reduce((lambda x, y: x+y), singles)
print("sum of singles:", sum)

#başka örnek

nums2 = [3, -2, 4, 5, 6, 2, 8, 1, 0]


def returnBigOne(x, y):
    if x < y:
        return y
    else:
        return x

print("nums2:", nums2)
maxnumber = reduce(returnBigOne, nums2)
print("max:", maxnumber)
print("nums2:", nums2)


'''ITERATOR EXAMPLES--------------------------------------------------------------
'''

numarray = [3, 2, 5, 7, 3, 5, 8, 7, 9]

myiter = iter(numarray)

print("myiter points first value of numarray:", myiter.__next__())

print("myiter points second value of numarray:", next(myiter))


# iterator in class
class myrange:
    def __init__(self, Len):
        self.posindex = 1
        self.len = Len

    def __iter__(self):   # iter     will give you the object of iterator
        return self

    def __next__(self):   # next       will give you the next object
        if self.posindex <= self.len:
            val = self.posindex
            self.posindex += 1
            return val
        else:
            raise StopIteration         # it is needed for infiniteloopiteration

values = myrange(10)

for i in values:   # for loop uses __next__(self) of myrange class to iterate loop, as you can see we never say the len of the range
    print(i)

#in case for loop faces to an StopIteration exception, it will stop as if break used
# but if we use next(values)  when we reached the limit of the iteration
# we will encounter an exception like StopIteration
#print(next(values))
#print(next(values))


'''PASS LIST TO A FUNC-------------------------------------------------------------------------
'''

def countEvenOdd(lst):
    ev = 0
    od = 0
    for x in lst:
        if is_even(x):
            ev += 1
        else:
            od += 1

    return ev, od

list1 = [1, 2, 3, 6, 4, 6, 4, 8, 1, 0, 9, 5]
even, odd = countEvenOdd(list1)
print("Even count:{} Odd count:{}".format(even, odd))

rng1 = myrange(20)
even, odd = countEvenOdd(rng1)
print("Even count:{} Odd count:{}".format(even, odd))



'''GENERATOR-------------------------------------------------------------------------
butun listeyi almadan sadece sıradaki elemana erisim saglayan iterasyon aygıtıdır
yield keywordu ile bu elemana erisim saglanır
'''

def topten():

    yield 5
    yield 4
    yield 2
    yield 3
    yield -1


val = topten()
print(val)  # yield den dolayi topten bir generator oldugu icin bu satır ise yaramaz bunun yerine __next__() kullanılmali
print((val.__next__()))
print((val.__next__()))
print((val.__next__()))

for k in val:
    print(k)


'''goruldugu gibi topten de uretilen degerler icin onceden (val.__next__()) ile erisip yazdirmamiza ragmen
for loop yeniden bastan almadi kaldigi yerden devam etti
simdi topten() i biraz gelistirelim 
'''

def toptenadv(len):
    n = 1
    while n <= len:
        sq = n**2
        yield sq
        n += 1

val = toptenadv(15)

print("val array using toptenadv()")
for t in val:
    print(t)











