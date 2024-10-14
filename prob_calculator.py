import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      i = 0
      while i < int(value):
        self.contents.append(key)
        i += 1

  def draw(self, number_to_draw):
    if number_to_draw >= len(self.contents):
      return self.contents
    else:
      largo_del_array = len(self.contents)
      bolas_sacadas = []
      while number_to_draw > 0:
        indice_a_sacar = random.randint(0,largo_del_array-1)
        bolas_sacadas.append(self.contents[indice_a_sacar])
        self.contents.pop(indice_a_sacar)
        largo_del_array -= 1
        number_to_draw -= 1
      return bolas_sacadas

  def return_balls(self, balls_to_return):
    self.contents += balls_to_return


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  if num_balls_drawn >= len(hat.contents):
    return 1

  num_exp_success = 0

  list_balls_expected = []

  for key, value in expected_balls.items():
    i = 0
    while i < int(value):
      list_balls_expected.append(key)
      i += 1

  print(expected_balls,list_balls_expected)

  for i in range(num_experiments):
    flag_success = True

    test_hat = copy.deepcopy(hat)
    bolas_sacadas = test_hat.draw(num_balls_drawn)
    lista_a_remover = list_balls_expected.copy()

    bolas_sacadas_no_esperadas = 0
    bolas_sacadas_esperadas = 0

    for balls in list_balls_expected:
      try:
        bolas_sacadas.remove(balls)
        lista_a_remover.remove(balls)
        bolas_sacadas_esperadas += 1
      except:
        bolas_sacadas_no_esperadas += 1

    if lista_a_remover:
      flag_success = False
    else:
      num_exp_success += 1

  return num_exp_success / num_experiments