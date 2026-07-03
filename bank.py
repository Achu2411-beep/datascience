class bank:
    def __init__(self):
        self.acc_no=0
        self.bal=0
        print(self.bal)

    def addbank(self):
        self.acc_no=int(input("Enter the bank account number:"))

    def deposit(self):
        amt=int(input("Enter amount for deposit:"))
        self.bal=self.bal+amt
        print("Amount Deposited!")
    def withdraw(self):
        amt=int(input("Enter Amount for withdraw:"))
        self.bal=self.bal-amt
        print("\nAmount withdrawed !")
    def btransfer(self):
        print("transfer")
    def balance(self):
        print("Total balance:",self.bal)
b=bank()
ch=1;

while(ch!=0):
    print("1.Add bank account")
    print("2.Deposit money")
    print("3.withdraw money")
    print("4.transfer")
    print("5.show balance")
    print("0.Exit")
    ch=int(input("Enter your choice :"))
    if(ch==1):
        b.addbank()
    if(ch==2):
        b.deposit()
    if(ch==3):
        b.withdraw()
    if(ch==4):
        b.transfer()
    if(ch==5):
        b.balance()




