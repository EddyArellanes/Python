import 

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
