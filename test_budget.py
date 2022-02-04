from budget import Budget

def test___init__():
    var1 = Budget('bob', 500)
    assert var1.name == 'bob'
    assert var1.balance == 500

def test_deposit():
    var1 = Budget('bob', 500)
    var1.deposit(300)
    assert var1.balance == 800
    assert var1.history == [[800, 300]]

def test_withdraw():
    var1 = Budget('bob', 500)
    var1.withdraw(300)
    assert var1.balance == 200
    assert var1.history == [[200, -300]]

def test_transfer():
    var1 = Budget('bob', 500)
    var2 = Budget('bob', 500)
    Budget.transfer(var1, var2, 250)
    assert var1.balance == 250
    assert var2.balance == 750
    assert var1.history == [[250,-250]]
    assert var2.history == [[750,250]]