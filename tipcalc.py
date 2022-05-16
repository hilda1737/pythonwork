print("welcome to tip calculator")
bill=float(input("what was the total bill? &"))
tip=int(input("How much tip would you like to give? 10 ,20,30"))
people=int(input("how many would spilt the  bill?"))
bill_with_tip=tip/100 * bill + 100
print(bill_with_tip)
