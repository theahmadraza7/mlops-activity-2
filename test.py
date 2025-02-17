from main import Bank

bankObj = Bank()

def test_getAmount():
    assert bankObj.getAmount() == 0

def test_deposit():
    bankObj.deposit(100)
    assert bankObj.getAmount() == 100

def test_withdraw():
    bankObj.withdraw(50)
    assert bankObj.getAmount() == 50