def get_vat(price, vat_rate):
    vat = price / 100 * vat_rate
    price_no_vat = price - vat
    print(price_no_vat)

    if price > 0:
        print(price)
    else:
        print("error")

get_vat(-100, 18)