##try:
##  x = 5 / 0
##except ZeroDivisionError as e:
##  print("Pamiętaj kolego nie dziel przez zero! Twój wyjątek to:", e)
##  x = 0

##randomList = ['a', 0, 2, 5, 6]
##
##for value in randomList:
##    try:
##        print('wartosc: ', value)
##        r = 1/int(value)
##        break
##    except (ValueError, ZeroDivisionError) as error:
##        print('Oops! Wystapil blad: ', error)
##        print('Nastepna wartosc')
##        print()
##
##
##print('Dzielenie przez', value, 'wynosi', r)
##

##
##print('Początek programu')
##raise Exception('To jest ogólny wyjątek')
##print('Koniec programu')
import sys

def predict_future():
  num = int(input("Podaj dowolną liczbę naturalną: "))
  if num < 0:
    raise ValueError("To nie jest liczba naturalna!")
  else:
    print("Za", 10 * num, "ludzkość będzie mogła się teleportować")

try:
  predict_future()
except ValueError as e:
    print(e)
    print(sys.exc_info()[0])
