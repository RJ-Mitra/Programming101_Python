from graphNode import Person

rudra = Person("Rudra")
avi = Person("Avi")
bonu = Person("Bonu")
rohit = Person("Rohit")
arka = Person("Arka")
bom = Person("Bom")
bonku = Person("Bonku")

rudra.friends = [bonu, bom, avi]
avi.friends = [bonku, bonu]
bonu.friends = [arka]
arka.friends = [rohit]
bom.friends = [bonku, rudra]
bonku.friends = [avi]

avi.getAllConnections()
