def sum_plus(listes):
  if type(listes[0]) == str: r = ''
  elif type(listes[0]) == int: r = 0
  else: raise TypeError('sum list\'s object is must int or str')
  for i in listes: r += i
  return r

class Definer:
  def __init__(self, name, inputs, sose):
    self.name = name
    self.inputs = inputs
    self.sose = sose
  lambdas = lambda self: f'{self.name} = lambda {self.inputs}: {self.sose}'
class MakerMom(Definer):
  ob1 = Definer('define', 'self' , 'f\'def {self.name}({self.inputs}):\\n{self.sose}\'')
  ob2 = Definer('son_class', 'self' , 'f\'class {self.name}({self.inputs}):\\n{self.sose}\'')
  ob1 = ob1.lambdas()
  ob2 = ob2.lambdas()
  exec(f'{ob1}\n{ob2}')
class Makers(MakerMom):
  ob1 = MakerMom('classes', 'self', '  ob = MakerMom(self.name, \'\', self.sose)\n  return ob.son_class()' )
  ob2 = MakerMom('Error', 'self', '  ob = MakerMom(self.name, \'Exception\', self.sose)\n  return ob.son_class()' )
  ob1 = ob1.define()
  ob2 = ob2.define()
  exec(f'{ob1}\n{ob2}')


def Maker(name, inputs, sose, option):
  ob = Makers(name, inputs, sose)
  return eval(f'ob.{option}()')

Makes = lambda make_list: [Maker(i['name'], i['inputs'], i['sose'], i['option']) + '\n' for i in make_list]