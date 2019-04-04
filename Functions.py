import time
from datetime import datetime

# update system date into string
dateAndTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def checking(m, n):
    list2 = []
    fhand = open('cardNumber' + m + '.txt')
    for line in fhand:
        if line.startswith('password'):
            list2.append(line[11:15])
    if int(list2[-1]) == n:
        return 1
    else:
        return 0


def delaying(m):
    time.sleep(m)

def balanceCheck(newbalance, balance):
    if newbalance <= 500:
        Functions.delaying(1)
        print('\nSORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT\n')
        print('YOUR CURRENT BALANCE IS\n', balance)
        return 0


def printNewAmount(newbalance, card_no):
    print('PLEASE COLLECT YOUR CASH\n')
    time.sleep(1)
    print('calculating new amount')
    time.sleep(0.5)
    print('YOUR CURRENT BALANCE IS\n', newbalance)
    fhand2 = open("cardNumber" + card_no + ".txt", "a")
    fhand2.write('\n' + 'balance = ' + str(newbalance))
    fhand2.write('\n' + 'datetime = ' + dateAndTime)
    fhand2.close()


def setPassword(card_no, password):
    fhand2 = open("cardNumber" + card_no + ".txt", "a")
    fhand2.write('\n' + 'password = ' + str(password))
    fhand2.write('\n' + 'passdatetime = ' + dateAndTime)
    time.sleep(1)
    print('password set successfully')
    fhand2.close()
