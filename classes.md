# Classes

Una classe en un llenguatge de programació és un paradigma en el qual s'intenta apropar el món de les dades digitals al món real.

Aquí per exemple tenim una persona:

<img width="768" height="659" alt="image" src="https://github.com/user-attachments/assets/34761e57-b5b9-4673-bcdb-61bb5b25c801" />

Les persones tenen uns atributs, unes característiques determinades, com poden ser: nom, edat, sexe...

A més les persones poden fer coses com menjar, parlar, caminar... Això són funcionalitats o funcions.

Les classes ens serveixen per definir objectes de qualsevol tipus: persones, animals, cotxes, cadires...

Per tant es pot dir que una classe és la **plantilla** per a crear objectes.

# Objectes

Si una classe és la plantilla, cada cas individual d'un objecte creat seguint aquesta plantilla és un objecte o una instància d'una classe.

<img width="802" height="420" alt="image" src="https://github.com/user-attachments/assets/a8d795af-97fd-4dc2-8423-b23f6667bd01" />

Si tenim la classe persona podem definir totes les persones que vulguem concretant la plantilla "persona" amb dades concretes, creant l'objecte John, Dessy, ...

# Classes a Python

Com es defineix una classe a Python?

[Aquí ho tenim](https://dungeonofbits.com/clases-en-python.html).

# Activitat

Anem a crear una classe amb els seus atributs i les seves funcions, seguim amb l'exemple persona.


- Fitxer main.py

```
from classes import *

if __name__ == '__main__':
    p = Persona(
        1,
        "Anna",
        "Garcia",
        "Lopez",
        date(1995, 2, 6),
        "12345678Z"
    )

    print(p.calcular_edat())
    print(p.inicials())
    print(p.nom_complet())
    print(p.es_aniversari())
```

- Fitxer classes.py

```
from datetime import date

# Classe persona amb els seus atributs i funcions
class Persona:

    # Funció d'inicialització, aquí li passem els atributs
    def __init__ (self, id_persona, nom, cognom1, cognom2, data_naixement, dni):
        self.id_persona = id_persona
        self.nom = nom
        self.cognom1 = cognom1
        self.cognom2 = cognom2
        self.data_naixement = data_naixement
        self.dni = dni

    # Funció que calcula l'edat d'una persona
    def calcular_edat(self):
        avui = date.today()
        edat = avui.year - self.data_naixement.year

        # Si encara no ha fet anys aquest any, restem 1
        if (avui.month, avui.day) < (self.data_naixement.month, self.data_naixement.day):
            edat -= 1

        return edat
    # Funció que escriu el nom sencer d'una persona
    def nom_complet(self):
        return f"{self.nom} {self.cognom1} {self.cognom2}"

    # Funció que imprimerix les inicials d'una persona
    def inicials(self):
        return f"{self.nom[0]}{self.cognom1[0]}{self.cognom2[0]}".upper()

    # Funció que diu si és l'aniversari d'una persona
    def es_aniversari(self):
        from datetime import date
        avui = date.today()
        return avui.month == self.data_naixement.month and avui.day == self.data_naixement.day

# Classe CRUD d' objectes persona
class PersonaCRUD:
    def __init__(self):
        self.persones = []

    def crear(self, persona):
        self.persones.append(persona)

    def obtenir_totes(self):
        return self.persones

    def obtenir_per_id(self, id_persona):
        persona  = None
        for p in self.persones:
            if p.id_persona == id_persona:
                persona = p
        return persona

    def actualitzar(self, id_persona, nom=None, cognom1=None, cognom2=None, data_naixement=None, dni=None):
        persona = self.obtenir_per_id(id_persona)
        if persona is None:
            return False

        if nom is not None:
            persona.nom = nom
        if cognom1 is not None:
            persona.cognom1 = cognom1
        if cognom2 is not None:
            persona.cognom2 = cognom2
        if data_naixement is not None:
            persona.data_naixement = data_naixement
        if dni is not None:
            persona.dni = dni
        return True

    def eliminar(self, id_persona):
        persona = self.obtenir_per_id(id_persona)
        if persona:
            self.persones.remove(persona)
            return True
        return False
```

