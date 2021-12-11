class Definer:
    def __init__(self, name, inputs, sose):
        self.name = name
        self.inputs = inputs
        self.sose = sose
    lambdas = lambda self: '{} = lambda {}: {}'.format(self.name, self.inputs, self.sose)
class MakerMom(Definer):
    ob1 = Definer('define', 'self' , '\'def {}({}):\\n{}\'.format(self.name, self.inputs, self.sose)')
    ob2 = Definer('son_class', 'self' , '\'class {}({}):\\n{}\'.format(self.name, self.inputs, self.sose)')
    exec('{}\n{}'.format(ob1.lambdas(),ob2.lambdas()))
class Makers(MakerMom):
    ob1 = MakerMom('classes', 'self', '    ob = MakerMom(self.name, \'\', self.sose)\n    return ob.son_class()' )
    ob2 = MakerMom('Error', 'self', '    ob = MakerMom(self.name, \'Exception\', self.sose)\n    return ob.son_class()' )
    exec('{}\n{}'.format(ob1.define(),ob2.define()))


def Maker(name, inputs, sose, option):
    ob = Makers(name, inputs, sose)
    return eval('ob.{}()'.format(option))
