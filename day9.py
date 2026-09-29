# ---------------exception handling ---------------------
# Create an ATM system that handles invalid PINs, insufficient balance, and invalid withdrawal amounts.
# balance = 50000

# try:
#     pin = input("enter pin : ")
#     if pin != "1234":
#         raise Exception("invalid pin")
#     else:
#         withdraw = int(input("enter how much amount you want to withdraw : "))
#     if withdraw<=0:
#         raise Exception("insufficient amount")
#     if withdraw>balance:
#         raise Exception("invald wthdrawal amount")
#     else:
#         balance -= withdraw
#         print("successful withdraw")
#         print("remaining amount : ",balance)
# except Exception as e:
#     print("error",e)
# finally:
#     print("thank you for using ATM")

# Create a student result system that validates marks and handles invalid entries.
try:
  ID = input("enter id : ")
  if len(str(ID)) != 5:
    raise Exception("invalid id enter atleast 4 number ")
  else:
    subjects = 0
    sum = 0
    while subjects<=6:
      marks = int(input("enter marks : "))
      if marks<0:
        raise Exception("invalid marks")
      else:
        sum = sum+marks
        subjects += 1
        print(sum)
        percent = sum/6
        print(percent)
    if percent<50:
      print("fail")
    if percent>=70:
      print("grade B")
    else:
      print("grade A")
except Exception as e:
  print("error",e)
finally:
  print("your result")
    