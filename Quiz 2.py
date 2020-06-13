class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"პიროვნების სახელი: {self.name}, თანხა ანგარიშზე: {self.deposit}, სესხი: {self.loan}"


class House:
    def __init__(self, ID, price, owner, status="გასაყიდი"):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    def __str__(self):
        return f"ბინის ID: {self.ID}, ბინის ფასი: {self.price}, მფლობელი {self.owner}, სტატუსი: {self.status}"

    def sell(self, other, loan=None):
        if loan is None:
            p1.deposit += self.price
            other.deposit -= self.price
            self.owner = other
            new_status = "გაყიდული"
            return f"წარმატებით გაიყიდა {House(self.ID, self.price, self.owner, new_status)}"
        else:
            p1.deposit += self.price
            self.owner = other
            new_status = "გაყიდული სესხით"
            p2.loan += loan
            return f"ბინა გაიყიდა სესხით {House(self.ID, self.price, self.owner, new_status)}"


p1 = Person("Nika", 50000)
p2 = Person("kleqsela", 100000, 1500)
politkovstkaia = House(544, 80000, p1)
print(p1)
print(p2)
print(politkovstkaia.sell(p2, 90000))
print(p1.deposit)
print(politkovstkaia.owner)
