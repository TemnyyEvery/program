class money(object):
    def show(self):
        raise NotImplementedError()
 
class dollar(money):
    def show(self):
        print('dollar')
    def create(self):
        payment = "dollar"
        print(payment)
 
 
class euro(money):
    def show(self):
        print ('euro')
    def create(self):
        payment = "euro"
        print(payment)
 

class rouble(money):
    def show(self):
        print ('rouble')
    def create(self):
        payment = "rouble"
        print(payment)
 
class Choise():
    def choose_money(self, types):
        if types == 'DOL':
            return dollar()
        if types == 'EUR':
            return euro()
        
        if types == 'RUB':
            return rouble()
 
app = Choise()
app.choose_money('DOL').show()
app.choose_money('DOL').create()