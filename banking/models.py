from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=100)
    _balance = models.FloatField(default=0)

    def display_info(self):
        return "Account of " + self.name + " has balance " + str(self._balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.save()

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self.save()

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
            self.save()
