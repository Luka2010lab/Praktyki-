'''Poznaj deklarację i indeksowanie tablic.

Ćwiczenia:

stwórz tablicę z 10 liczbami i wypisz elementy parzyste,

znajdź największy i najmniejszy element.'''

Tab = [8,2,7,2,7,4,9,2,5,2,1]
tab2 = Tab.copy()
tab3 = [1,2,3]
tab4 = ['a','b','c']

#Tab.append(int(input('podaj liczbe')))
print( min(Tab), max(Tab), len(Tab))
print(tab2)
y = Tab + tab2

print(y,max(y),min(y),len(y))

p = tab3 * 5
print(p)
print(Tab[3]) 
print(Tab[:3])
Tab.extend(tab4)
print(Tab)
Tab.insert(5,'a')
print(Tab)
Tab.remove(5)
print(Tab)
Tab.reverse()
print(Tab)
tab2.sort()
print(tab2)
tab2.clear()
print(tab2)