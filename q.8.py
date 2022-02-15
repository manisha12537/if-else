actual_cost_price=int(input("enter the number"))
sale_amount=int(input("enter the number"))
if actual_cost_price>sale_amount:
    amount=actual_cost_price-sale_amount
    print("total loss amount:",amount)
elif sale_amount>actual_cost_price:
    amount=sale_amount-actual_cost_price
    print("total profit amount:",amount)
else:
    print("not profit no loss")


