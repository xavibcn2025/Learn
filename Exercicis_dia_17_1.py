# 1
print("1.Quin tipus de dada és False?")
print(type(False))
print("\r")

#2
print("2.Quin tipus és None?")
print(type(None))
print("\r")

#3
print('3. Quin tipus de dada retorna len("Hola")?')
print(type(len("Hola")))
print("\r")

#4
print("4. Què retorna type(3.0)?" )
print(type(3.0))
print("\r")

#5
print("5. Com crear una tupla amb un sol element?")
tupla=(5)
print(tupla)
print("\r")

#6
print("6. Quin tipus de dada és range(5)?")
print(type(range(5)))
print("\r")

#7
print('7. Quin és el tipus de set("aab")?')
set("aab")
print(type(set("aab")))
print("\r")

#8
print("8. Com sabries si un valor és un diccionari?")
# amb el mètode dict.values() o buscant el type
print(type(dict))
print("\r")

#9
print("9. Quindiferència hi ha entre [] i {}?")
print(type([]))
print(type({}))
print("\r")

#10
print('10. Quin tipus és int("5")?')
print(type(int("5")))
print("\r")


# 11
#print("11.Quin és el tipus de lista((1, 2, 3))?")
#nueva_lista=list((1, 2, 3))
#print(type(nueva_lista((1, 2, 3))))
#print("\r")

#12
print('12. Quina estructura retorna dict([[1, "a"], [2, "b"]])?')
print(type(dict([[1, "a"], [2, "b"]])))
print("\r")

#13
print('13. Quin és el tipus de set([1, 1, 2])?')
print(type(set([1, 1, 2])))
print("\r")

#14
print('14. Quin tipus és "3.14"?')
print(type("3.14"))
print("\r")

#15 -
print("15. Com pots verificar si un objecte és de tipus tuple?")
tupla = ("2",6)
print(type(tupla))
tupla == tuple #Joan
print(tuple)
print("\r")

#16
print('16. Quin és el resultat de type("100" + "200")?')
print(type("100" + "200"))
print("\r")

#17
print("17. Com sabries si un objecte és modificable (mutable)?")
lista = [1,2,3]
print(id(lista))
print("\r")

#18
print("18. Quin tipus de dada és un fitxer obert amb open()?")
#f = open("arxiu.txt", "r")
#print(type(f))
print("\r")

#19
print("19. Com comproves si una clau existeix en un diccionari?")
dict_prova = {}
dict_prova["Gos"] = "Animal"
print(dict_prova["Gos"]) # Comprova si la "key" existeix dintre el dict. Si no hi és donarà error.
print("\r")

#20
print('20. Quin és el tipus de {"x": [1, 2]}?')
print(type({"x": [1, 2]}))
print("\r")