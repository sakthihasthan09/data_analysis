class Employee:
    raise_amount=1.04               #variable

    def __init__(self,first,last,pay):
        self.first=first
        self.last =last
        self.pay=pay
        self.email=first+'.'+last+'@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first , self.last)
    def raise_apply(self):
        self.pay=int(self.pay *self.raise_amount )



emp_1= Employee('sakthi','hasthan',50000)
emp_2= Employee('s','h',60000)

print(f'current pay is {emp_1.pay}')
print(emp_1.raise_amount)
emp_1.raise_apply()    #method call
print(emp_1.pay)
 