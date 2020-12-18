food_name     ="Pizza"
food_price    =50.00
food_quantity =4
distance      = 110 
vip_card      = True

cost_food          =food_price*food_quantity
cost_delivery_free=cost_food>= 200.00 and distance<=100\
                                       or vip_card==True

print(food_price, "x", food_quantity, "=", cost_food)
print ("Is your delivery free?", cost_delivery_free)