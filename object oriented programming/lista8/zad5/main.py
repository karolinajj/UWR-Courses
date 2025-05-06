from state import ATMContext
if __name__ == "__main__":
    atm = ATMContext()

    atm.insert_card()
    atm.verify_card(valid=True)
    atm.enter_pin(pin_correct=False)
    atm.enter_pin(pin_correct=True)
    atm.select_amount()
    atm.verify_amount(valid=False)
    atm.select_amount()
    atm.verify_amount(valid=True)
    atm.confirm_withdrawal()
    atm.eject_card()
