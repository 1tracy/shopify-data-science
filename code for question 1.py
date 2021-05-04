import csv

input_file = csv.DictReader(open('data.csv'))

total_orders = 0
total_items = 0
total_order_amount = 0

for row in input_file:
    total_orders += 1
    total_items += int(row['total_items'])
    total_order_amount += int(row['order_amount'])

print('\n\n')
print('Total Orders: ' + str(total_orders)) # 5000
print('Total Items Bought: ' + str(total_items)) # 43936
print('Total Order Amount: ' + str(total_order_amount)) # 15725640

'''
Q1A:
Naively calculating an AOV of $3145 doesn't take into account the fact that
multiple items can be bought in the same order. A more accurate AOV would be
to divide the total order amount by the total item count instead of the
total order count. If I had more information about the dataset I would also
suggest taking cost of goods sold into account, as a higher revenue item may
not necessarily have a higher profit.
'''
q1a = "\nQ1A:\nNaively calculating an AOV of $3145 doesn't take into account the fact that\n" + "multiple items can be bought in the same order. A more accurate AOV would be\n" + "to divide the total order amount by the total item count instead of the\n" +"total order count. If I had more information about the dataset I would also\n" +"suggest taking cost of goods sold into account, as a higher revenue item may\n" +"not necessarily have a higher profit.\n"
print(q1a)
print ("Naive AOV was found by dividing total revenue by total orders: $" + str(total_order_amount / total_orders) + " revenue per order")
print ('A more accurate metric value would be: $' + str(round(total_order_amount / total_items, 2)) + ' of revenue per item sold.') # $357.92

'''
Q1B:
The metric that I would report on would be average revenue per item sold.
'''
print ("\nQ1B: \nThe metric that I would report on would be average revenue per item sold.\n")

'''
Q1C:
The value of the metric is approximately $357.92 revenue per item sold.
'''
print ("Q1C:\nThe value of the metric is approximately $357.92 revenue per item sold.")

print('\n\n')
