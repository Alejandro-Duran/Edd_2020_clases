from Cola import Queue, BoundedPriorityQueue

q1 = Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print("Prueba 2 de cola")
c1={"i.d":1, "nombre":"Mario", "Aalance":20.5}
c2={"i.d":2, "nombre":"Denis", "Aalance":3456.5}
c3={"i.d":3, "nombre":"Alberto", "Aalance":10000000.0}

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente = atencion.dequeue()
print(f"Bienvenido sr. {siguiente['nombre']}, en que podemos servirle el dia de hoy")
print(atencion.to_string())


print("Pruebas de la cola con prioridad acotada")

maestres = {"prioridad":4, "descripcion":"Maestre", "personas":["Juan P","Diego H"]}
niños = {"prioridad":2, "descripcion":"Niños", "personas":["Santi H","Angel H"]}
mecanicos = {"prioridad":4, "descripción":"Mecanicos", "personas":["Diana T","Maria Z"]}

cpa=BoundedPriorityQueue(7)
cpa.enqueue(maestres["prioridad"], maestres)
cpa.enqueue(niños["prioridad"], niños)
cpa.enqueue(mecanicos["prioridad"], mecanicos)
cpa.to_string()
