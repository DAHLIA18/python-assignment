import my_discount

def test_15_percent_discount():
    assert my_discount.my_discount(150, 15) == 127.5

def test_20_percent_discount():
    assert my_discount.my_discount(100, 20) == 80

def test_0_percent_discount():
    assert my_discount.my_discount(200, 0) == 200

def test_50_percent_discount():
    assert my_discount.my_discount(80, 50) == 40

def test_25_percent_discount():
    assert my_discount.my_discount(120, 25) == 90

def test_10_percent_discount():
    assert my_discount.my_discount(300, 10) == 270

def test_30_percent_discount():
    assert my_discount.my_discount(75, 30) == 52.5