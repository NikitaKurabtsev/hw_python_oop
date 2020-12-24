import datetime as dt

class Calculator:
    """Класс калькулятор имеет свой лимит и список."""
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    
    def add_record(self, record):
        """Метод add_record() делает запись в список records."""
        self.records.append(record)

    def get_today_stats(self):
        """С помощью метода get_today_stats() считаем, сколько потрачено каллорий/денег за день."""
        date_today = dt.datetime.today().date()
        day_spent = sum(i.amount for i in self.records if i.date == date_today)
        return day_spent
 
    def get_week_stats(self):
        """С помощью метода get_week_stats() считаем, сколько потрачено каллорий/денег за неделю."""
        today = dt.datetime.today().date()
        delta = dt.timedelta(days=7)
        date_week_ago = today - delta
        week_stats = sum(i.amount for i in self.records if date_week_ago < i.date <= today)
        return week_stats

    def difference(self):
        calories_remained = self.limit - self.get_today_stats()
        return calories_remained


class Record:
    """Класс для создания записи."""
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date == None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CaloriesCalculator(Calculator):
    """Определяем превысили лимит или нет, выводя соответсвующие сообщения."""    
    def get_calories_remained(self):
        if self.difference() <= 0:
            return 'Хватит есть!'
        return('Сегодня можно съесть что-нибудь ещё, но с общей '
               f'калорийностью не более {self.difference()} кКал')



class CashCalculator(Calculator):
    """Создаем словарь с кортежами, чтобы обращатся к нему по ключу и получать данные на выходе."""    
    USD_RATE = 74.12
    EURO_RATE = 88.34
    
    def get_today_cash_remained(self, currency):
        if self.difference() == 0:
            return 'Денег нет, держись'
        money_dict = {"rub" : (1, "руб"),
                      "usd" : (self.USD_RATE, "USD"),
                      "eur" : (self.EURO_RATE, "Euro")}
        currency_rate, currency_name = money_dict[currency]
        final_cash = abs(round(self.difference() / currency_rate, 2))
        if self.difference() > 0:
            return f'На сегодня осталось {final_cash:.2f} {currency_name}'
        return f'Денег нет, держись: твой долг - {final_cash:.2f} {currency_name}'


        
        
        


        


if __name__ == '__main__':

# для CashCalculator
    r1 = Record(amount=213, comment="Безудержный шопинг", date="07.12.2020")
    r2 = Record(amount=1568, comment="Наполнение потребительской корзины",
                date="09.03.2019")
    r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")
    # для CaloriesCalculator
    r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.",
                date="05.12.2020")
    r5 = Record(amount=84, comment="Йогурт.")
    r6 = Record(amount=1140, comment="Баночка чипсов.",
                date="12.12.2020")
    # создаем экземпляр класса Calculator и обращаемся
    # к его методам.
    c1 = Calculator(10000)
    c1.add_record(r1)
    c1.add_record(r2)
    c1.add_record(r3)
    c1.add_record(r4)
    c1.add_record(r5)
    c1.add_record(r6)
    c1.get_today_stats()
    print(c1.get_week_stats())
    # проверка калькулятора денег
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=400, comment="кофе"))
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др",
                                      date="12.12.2020"))
    print(cash_calculator.get_today_cash_remained('rub'))
    # проверка калькулятора калорий
    calories_calculator = CaloriesCalculator(1000)
    calories_calculator.add_record(Record(amount=468, comment="биг мак"))
    calories_calculator.add_record(Record(amount=700, comment="биг тейсти"))
    calories_calculator.add_record(Record(amount=3900, comment="биг тейсти + биг мак меню и пирожок???",
                                          date="08.11.2019"))
    print(calories_calculator.get_calories_remained())