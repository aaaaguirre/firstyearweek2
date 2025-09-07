# Q1





# inputs
id_number = input("Enter ID name:")
name = input("Enter name:")
address = input("Enter address:")
marital_status = input("Enter marital status:")
gross_pay = int(input("Enter gross pay:"))
password = input("Enter password:")
password_confirm = input("enter password again:")

if gross_pay < 500000:
 taxed_pay = gross_pay - 25000
 print("your allowance is: €25000 ")
else:
    taxed_pay = gross_pay - 20000
print("your allowance is: €20000 ")

if marital_status == "s":
    tax = taxed_pay * 0.2
elif marital_status == "m":
    tax = taxed_pay * 0.23
else:
    print("not valid")
net_pay = gross_pay - tax

if password != password_confirm:
  print("incorrect password")
else:
    print("correct")

print("id: ", id_number)
print("name: ", name)
print("address: ", address)
print("marital status: ", marital_status)
print("gross pay: ", gross_pay)
print("net pay: ", net_pay)
print("tax: ", tax)