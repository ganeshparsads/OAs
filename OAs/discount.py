
logs = [
    "sell j. 3",
    "sell p. 59",
    "discount_start p. 588. 96",
    "sell p. 12",
    "sell j. 5",
    "discount_start x. 28. 25",
    "discount_end p",
    "sell x. 5",
    "sell p. 5",
    "sell p. 54",
    "discount_start p. 102. 28",
    "sell p. 2",
    "discount_start j. 569. 50",
    "sell p. 8",
    "discount_end j",
    "sell p. 25",
    "sell j. 13",
    "sell p. 47",
    "sell p. 1",
    "sell j. 8",
]

#{"item2": (price, count)}
discount_map = {}

pList = ["p: 839", "j: 981", "x: 776"]

priceList = {}

for i in pList:
    tokens = i.split(": ")
    priceList[tokens[0]] = int(tokens[1])


# priceList = {"item1": 100, "item2": 200}



amt = 0

# import pdb
# pdb.set_trace()

for i in logs:
    tokens = i.split(' ')

    if tokens[0] == "discount_start":
        # there'll be 4 tokens
        discount_map[tokens[1].split('.')[0]] = (int(tokens[2].split('.')[0]), int(tokens[3].split('.')[0]))

    elif tokens[0] == "discount_end":
        if tokens[1] in discount_map:
            del discount_map[tokens[1]]

    elif tokens[0] == "sell":
        item_name = tokens[1].split('.')[0]
        qty = int(tokens[2].split('.')[0])
        if tokens[1].split('.')[0] in discount_map:
            discount, cnt = discount_map[item_name]

            if qty > cnt:
                disc_qty = qty - cnt
                new_price = priceList[item_name] - discount
                amt += new_price * cnt

                amt += priceList[item_name]*disc_qty 
                del discount_map[item_name]
            else:
                new_price = priceList[item_name] - discount
                if qty == cnt:
                    amt += new_price*qty
                    del discount_map[item_name]
                else:
                    disc_qty = cnt - qty
                    amt += new_price*qty
                    discount_map[item_name] = (discount, disc_qty)
        else:
            amt += priceList[item_name]*qty

print(amt)