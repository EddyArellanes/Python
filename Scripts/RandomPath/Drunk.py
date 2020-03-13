# Also known as Camino de los Borrachos
import random

class Drunk:
  def __init__(self, name):
    self.name = name

class CommonDrunk(Drunk):
  def __init__(self, name):
    super().__init__(name)

  def walk(self):
    return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)]) #Options that would happen with the same potluck

class Coordinate:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def move(self, delta_x, delta_y):
    return Coordinate(self.x + delta_x, self.y + delta_y)
  
  #Pitagoras Theorem
  def distance(self, coordinate ):
    delta_x = self.x - coordinate.x
    delta_y = self.y - coordinate.y

    return (delta_x**2 + delta_y**2) ** 0.5

class Field:
  def __init__(self):
    self.drunk_coordinates = {}

  def add_drunk(self, drunk, coordinate):
    self.drunk_coordinates[drunk] = coordinate
  
  def move_drunk(self, drunk):
    delta_x, delta_y = drunk.walk()
    current_coordinate = self.drunk_coordinates[drunk]
    new_coordinate = current_coordinate.move(delta_x, delta_x)
    self.drunk_coordinates[drunk] = new_coordinate

  def get_coordinate(self, drunk):
    return self.drunk_coordinates[drunk]

def walk(field, drunk, steps):
  start = field.get_coordinate(drunk)
  for _ in range(steps):
    field.move_drunk(drunk)
  return start.distance(field.get_coordinate(drunk))

def simulation_walk(steps, tries, drunk_type):
  drunk = drunk_type(name='Eddy')
  origin = Coordinate(0,0)
  distances = []
  #Underscore means we won't use the var
  for _ in range(tries):
    field = Field()
    field.add_drunk(drunk, origin)
    simulation_walk = walk(field, drunk, steps)
    distances.append(round(simulation_walk, 1))
  return distances

def main(distance_paths, tries, drunk_type):

  for steps in distance_paths:
    distances = simulation_walk(steps, tries , drunk_type)
    distance_mid = round(sum(distances) / len(distances), 4)
    distance_max = max(distances)
    distance_min = min(distances)
    print(f'{drunk_type.__name__} Caminata aleatoria de {steps} pasos')
    print(f'Media = {distance_mid}')
    print(f'Max = {distance_max}')
    print(f'Minima = {distance_min}')

# Convention to specify that if the script is ran into terminal, this will be executed
if __name__ == '__main__':
  distance_paths = [10, 100, 1000, 10000]
  # Number of running simulation
  tries = 100
  main(distance_paths, tries, CommonDrunk)
