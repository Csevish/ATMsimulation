import Functions
import time

def withdrawal(amount):
    newBalance = balance
    newBalance = newBalance - amount

    # checking balance for less than 500
    returnValue = Functions.balanceCheck(newBalance, balance)
    if returnValue == 0:
        print()

    # updating the file with new amount
    else:
        Functions.printNewAmount(newBalance, card_no)

while True:
    time.sleep(1)
    # intro statements for display

    print('\n\nWelcome to VISHWAS BANK Co. Ltd.')
    Functions.delaying(1)
    print('services provided are:')
    print('intant small terms loans provided')
    Functions.delaying(1)
    print('\t\tintant small terms loans provided')
    Functions.delaying(1)
    print('\t\t\t\tintant small terms loans provided')

    # start of transactions



    card_no = (input('Enter your card_no\n'))
    # entering card number

    attemptsLeft = 3
    # attempts for a wrong pin for security

    done = True
    while done:
        password = int(input('Enter your password\n'))
        # enter Password

        credentialsMatch = Functions.checking(card_no, password)
        # matching card number and password

        if credentialsMatch == 1:

            done = False
            list1 = []
            fileHandler = open('cardNumber' + card_no + '.txt')

            for i in fileHandler:

                if i.startswith('balance = '):
                    list1.append(i[10:])

                else:
                    continue

            balance = float(list1[-1])

            # main option
            print('1.BALANCE ENQUIRY\t\t\t4.CHANGE PASSWORD\n')
            print('2.WITHDRAWAL\t\t\t\t5.MINI STATEMENT\n')
            print('3.FAST CASH\t\t\t\t\t6.CANCEL TRANSACTION\n')
            print("=================================")
            ch = int(input('Enter your choice\n'))
            if ch == 1:

                # balace enquiry
                print('BALANCE= ', balance)
                print('No recipt is printed\n\t\tsave trees :=)')

            elif ch == 2:

                # withdrawal
                amount = int(input('ENTER THE AMOUNT: MULTIPLE OF 100 or 500\n'))
                withdrawal(amount)

            elif ch == 3:

                # fast cash
                attemptsLeft2 = True
                while attemptsLeft2:

                    print('1. 1000.00\t\t\t3.5000.00\n')
                    print('2. 2000.00\t\t\t4.10000.00\n')

                    choice2 = int(input('enter option'))
                    if choice2 == 1:
                        attemptsLeft2 = False
                        withdrawal(1000)

                    elif choice2 == 2:
                        attemptsLeft2 = False
                        withdrawal(2000)

                    elif choice2 == 3:
                        attemptsLeft2 = False
                        withdrawal(5000)

                    elif choice2 == 4:
                        attemptsLeft2 = False
                        withdrawal(10000)

                    else:
                        print("enter correct choice\n")
                        attemptsLeft2 = True

            elif ch == 4:
                # changing password
                password1 = int(input("enter new password"))
                password2 = int(input("confirm new password"))
                if password1 == password2 and password2 >= 1000 and password2 <= 9999:
                    Functions.setPassword(card_no, password2)

            elif ch == 5:
                #print mini statement
                fhand3 = open('cardNumber' + card_no + '.txt')
                list4 = []
                list5 = []
                for line in fhand3:
                    if line.startswith('balance'):
                        list4.append(line[10:-1])
                    if line.startswith('datetime'):
                        list5.append(line[11:-1])
                list6 = list4[::-1]
                list7 = list5[::-1]
                i = len(list6)

                if i >= 6:
                    i = 5

                j = 0
                for j in range(i):
                    print('WD $ - ', list6[j], '\n', list7[j])

            elif ch == 6:
                break

        else:
            attemptsLeft -= 1
            if attemptsLeft == 0:
                exit("0 attempts left\ncontact Bank")
                done = False

            else:
                print(attemptsLeft, 'attempts left\n\t\t-->be very CAREFULL while entering pin')



