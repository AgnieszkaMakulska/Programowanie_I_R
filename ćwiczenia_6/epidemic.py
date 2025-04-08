import random
import math
import matplotlib.pyplot as plt

class Person:

    MaxDistance = 1 # pola statyczne - wspólne dla wszystkich obiektów tej klasy
    MaxIllDistance = 0.1


    def __init__(self, x, y, status):
        self.x = x
        self.y = y
        self.status = status

    def Move(self):
        if self.status == 'healthy' or self.status == 'carrier':
            max_distance = Person.MaxDistance
        elif self.status == 'sick':
            max_distance = Person.MaxIllDistance
        
        # cyllindrical coordinates
        dr = random.uniform(0, max_distance)
        d_phi = random.uniform(0, 2 * math.pi)

        self.x += dr * math.cos(d_phi)
        self.y += dr * math.sin(d_phi)

    def Info(self):
        return f"Stan: {self.status}, Położenie: ({self.x:.2f}, {self.y:.2f})"

    def __str__(self):
        return self.Info()
    


class Population:

    InfectionProbability = 0.2
    InfectionDistance = 1

    def __init__(self, n_people, w = 100, h = 100):
        self.n_people = n_people
        self.h = h
        self.w = w
        self.people = []
        for _ in range(n_people):
            x = random.uniform(0, w)
            y = random.uniform(0, h)
            if random.uniform(0, 1) < Population.InfectionProbability:
                if random.uniform(0, 1) < 0.5:
                    status = 'sick'
                else:
                    status = 'carrier'
            else:
                status = 'healthy'
            self.people.append(Person(x, y, status))

    def Move(self):
        for person in self.people:
            person.Move()
            if person.x < 0 or person.x > self.w: #jeśli osoba wyszła poza planszę
                person.x = person.x % self.w
            if person.y < 0 or person.y > self.h:
                person.y = person.y % self.h

        # Sprawdzanie dystansu między każdą parą osób:

        enum = enumerate(self.people)
        # Enumerate zwraca listę krotek (indeks, osoba).
        # Przypisujemy osobom indeksy, żeby uniknąć sprawdzania tej samej pary dwa razy.
        for i, person1 in enum:
            for j, person2 in enum:
                if i >= j:  # Unikamy sprawdzania tej samej pary dwa razy
                    continue    
                else:
                    distance = math.sqrt((person1.x - person2.x) ** 2 + (person1.y - person2.y) ** 2)
                    if distance < Population.InfectionDistance:
                        if person1.status == 'healthy' and person2.status in ['sick', 'carrier']:
                            if random.uniform(0, 1) < 0.5:
                                person1.status = 'sick'
                        elif person2.status == 'healthy' and person1.status in ['sick', 'carrier']:
                            if random.uniform(0, 1) < 0.5:
                                person2.status = 'sick'

    def Paint(self, time):
        for person in self.people:
            if person.status == 'healthy':
                plt.scatter(person.x, person.y, c='green')
            elif person.status == 'sick':
                plt.scatter(person.x, person.y, c='red')
            elif person.status == 'carrier':
                plt.scatter(person.x, person.y, c='yellow')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.savefig(f'rysunki/epidemic_{t}.png')
        plt.clf()  # czyści wykres przed następnym rysowaniem

population = Population(100)

for t in range(10000):
    population.Move()
    if t % 100 == 0:
        population.Paint(t)