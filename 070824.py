# '1st program'
print(9**0.5*5)
# '2nd program'
print(9.99>9.98 and 1000 != 1000.1)
# '3rd program' - 1234 and 5678
print(int((1234%1000//10)+(5678%1000/10)))
# '4th program' 13.42 and 42.13
print(int(13.42) == int(42.13%1*100) or print(int(42.13)) == int(13.42%1*100+int(13.42//10)))
print(5)
print(int(13.42) == int(42.13%1*100) and print(int(42.13)) == int(13.42%1*100+int(13.42//10)))
print(int(42.13))
print(int(13.42%1*100+int(13.42//10)))
#Старая задача
# 'длина слова'
print('Hello, world!')
print(type('Hello, world!'))
a='Hello, world!'
print(a)
print(len(a))
#Задача:суммы и разности
first = 5
second = 7
print(first + second)
print(first-second)
summa = 12
diff = -2
print(summa)
print(diff)
#Задача: Среднее арифметическое
first = 5
second = 9
third = 10
print((first+second+third)/3)
mean=8
print(mean)
# Задача:Простые строчки
first_string = 'Понедельник, '
second_string = 'Вторник'
print(first_string+second_string)
# Задача: сложная формула
a=10
b=100
c=1000
print(a+b+c)
f=(a*b)+(a*c)
print(((f)**3)/2)

y = [".ru", ".net", ".com", "@"]
collection = "nantoliy26@gmail.com"
iterable_1 = "urban@mail.ru"
x = "@"
y = ".com"
z = ".net"
b = ".ru"
print(collection.endswith((".ru", ".com", ".net")))
#print(x in collection or y in collection or z in collection or b in collection)
def is_member(value, iterable):
    value = [".ru", ".net", ".com", "@"]
    iterable = ["nantoliy26@gmail.com", "urban@mail.ru"]
    for item in iterable:
        if value is item or value == item:
            return True
    return False
is_member([".ru", ".net", ".com", "@"], ["nantoliy26@gmail.com", "urban@mail.ru"])
def probe_mail(message, recipient, sender="Urals@rambler.rambler"):
    is_member([".ru", ".net", ".com", "@"], ["Abdracadabra2mail.yandex", "Urals@rambler.rambler"])
    if is_member([".ru", ".net", ".com", "@"], ["Abdracadabra2mail.yandex", "Urals@rambler.rambler"]) == True:
        print(message, recipient, sender)
    if is_member([".ru", ".net", ".com", "@"], ["Abdracadabra2mail.yandex", "Urals@rambler.rambler"]) == False:
        print("Ошибка адреса")

probe_mail("Проверка связи", "Abdracadabra2mail.yandex")

# check_symbols = set("@.com.ru.net")
#     if any((c in check_symbols) for c in recipient) and any((c in check_symbols) for c in sender):
#         print(f"Письмо успешно отправлено на адрес {recipient} с адреса {sender}.")
#     else:
#         print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")

















