price = 'от 31 р'
strong_price = [int(i) for i in price.split() if i.isdigit()][0]
print(strong_price)