# round()
# f"string {variable}"
# input



bill = float(input("what is the total bill : "))
tip = int(input("how much percent tip you like to give : "))
people = int(input("in how many people you like to split the bill : "))
bill_with_tip = (tip / 100 * bill) + bill 
print("total bill is : " , round(bill_with_tip))
print(f"bill for every person : {round(bill_with_tip / people)}")