# -*- coding: utf-8 -*-
import os
import json


class Customer:
    def __init__(self, c_name="", c_middle="", c_second=""):
        self.fio = dict(name=c_name, middle=c_middle, second=c_second)
        os.system(['cls'][os.name == os.sys.platform])
        print("{0}".format("="*60))
        while self.fio["name"].__len__() is 0:
            self.fio["name"] = input("Введите Имя ==> :")
            if self.fio["name"].__len__() is 0:
                print("Error ==>: Пустое Имя \n")
        while self.fio["middle"].__len__() is 0:
            self.fio["middle"] = input("Введите Отчество ==> :")
            if self.fio["middle"].__len__() is 0:
                print("Error ==>: Отчество пустое \n")
        while self.fio["second"].__len__() is 0:
            self.fio["second"] = input("Введите Фамилию ==> :")
            if self.fio["second"].__len__() is 0:
                print("Error ==>: Фамилия пустая \n")
        print("{0}".format("="*60))
        print("Имя клиента: {0} {1} {2}".format(self.fio["second"], self.fio["name"], self.fio["middle"]))
        print("{0}".format("="*60))


class BankCustomer(Customer):
    def __init__(self, accounts={}):
        super().__init__()
        self.client_accounts = self.banks_accounts(accounts)

    def banks_information(self):
        banks = {"1": "Приват Банк",
                 "2": "Райффайзен Банк Аваль",
                 "3": "Креди Агриколь Банк",
                 "4": "УкрСиббанк",
                 "5": "Кредобанк",
                 "6": "Ощадбанк",
                 "7": "ПроКредит Банк",
                 "8": "Укргазбанк",
                 "9": "Мегабанк",
                 }
        print("Выберите из списка банк, информацию по которому вы хотите добавить: ")
        print("{0}".format("="*60))
        for i in range(banks.__len__()):
            print("{0:^6} : {1:<30}".format(i+1, banks[str(i+1)]))
        print("{0}".format("="*60))
        choice = None
        while choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            choice = input("Ваш выбор (1-9) : ")
        bank_choice = banks[choice]
        print("Выбран банк: {0}".format(bank_choice))
        bank_choice = banks[choice]
        choice = None
        while choice != "3":
            os.system(['cls'][os.name == os.sys.platform])
            print("\nСделайте выбор :")
            print("{0}".format("="*60))
            print("{0:>7} Добавить информацию о счёте клиента в {1}".format(1, bank_choice))
            print("{0:>7} Добавить информацию о кредите клиента в {1}".format(2, bank_choice))
            print("{0}".format("="*60))
            print("{0:>7} Закончить работу \n\n".format(3))
            choice = input("Ваш выбор (1-3) : ")
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass

    def banks_accounts(self, accounts):
        if accounts.__len__() is 0:
            print(">>>>  У клиента {0} {1} {2} отсутствует банковская информация".format(self.fio["second"],
                                                                                         self.fio["name"],
                                                                                         self.fio["middle"]))
            temp_flag = None
            while temp_flag not in ["Y", "N", "y", 'n', 'д', 'н']:
                temp_flag = input("Добавить инфорнмацию о клиенте (счета/кредиты)? (Y/N) :")
            if temp_flag in ["Y", "y", 'д']:
                self.banks_information()
        else:
            return accounts


class BankCredit:
    def __init__(self, bank_name=""):
        if bank_name == "":
            pass
        else:
            self.bank_name = bank_name
        self._credit_rates = self.take_rate(self.bank_name)
        self.bank_client = self.load_bd_clients()

    def take_rate(self):
        if os.path.isfile("bank_rate.dat"):
            f = open("bank_rate.dat", "a")
        # else:
        #     print("Error ==>: Процентной ставки по даннону банку не существует\n")
        #     flag = input("Добавить процентную ставку по данному банку? (Y/N)")
        #     if flag is ["Y", "y", :
        #         pass
        # if f.

    # def load_bd_clients(self):
    #     if os.path.isfile("bank_clients.dat"):
    #         content = json.load(open("bank_client.json", "r"))
    #         if content.__len__() is not 0:
    #
    #
    #     else:
    #         return []

    def save_bd_clients(self, content):
        if os.path.isfile("bank_clients.dat"):
            json.dump(content, open("bank_client.json", "w"))

    def add_new_client_to_bd(self):
        client = BankCustomer()


if __name__ == "__main__":
    choice = None
    client = ""
    while choice != "4":
        os.system(['cls'][os.name == os.sys.platform])
        print("\nСделайте выбор :")
        print("{0}".format("="*60))
        print("{0:>7} Выбрать клиента из базы данных ".format(1))
        print("{0:>7} Добавить клиента в базу данных ".format(2))
        print("{0:>7} Работать со счетами клиента ".format(1))
        print("{0}".format("="*60))
        print("{0:>7} Закончить работу \n\n".format(4))
        choice = input("Ваш выбор (1-4) : ")
        if choice == "1":
            pass
        elif choice == "2":
            bd_client = BankCustomer()
        elif choice == "3":
            pass
        elif choice == "4":
            pass
    # user1 = BankCustomer()
