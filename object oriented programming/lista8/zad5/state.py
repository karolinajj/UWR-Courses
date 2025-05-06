from abc import ABC, abstractmethod

# Context
class ATMContext:
    def __init__(self):
        self.state = WaitingForCardState(self)

    def set_state(self, state):
        self.state = state

    def insert_card(self):
        self.state.insert_card()

    def verify_card(self, valid=True):
        self.state.verify_card(valid)

    def enter_pin(self, pin_correct=True):
        self.state.enter_pin(pin_correct)

    def select_amount(self):
        self.state.select_amount()

    def verify_amount(self, valid=True):
        self.state.verify_amount(valid)

    def confirm_withdrawal(self):
        self.state.confirm_withdrawal()

    def eject_card(self):
        self.state.eject_card()

# State
# abstract class
class ATMState(ABC):
    def __init__(self, atm):
        self.atm = atm

    @abstractmethod
    def insert_card(self): pass

    @abstractmethod
    def verify_card(self, valid): pass

    @abstractmethod
    def enter_pin(self, pin_correct): pass

    @abstractmethod
    def select_amount(self): pass

    @abstractmethod
    def verify_amount(self, valid): pass

    @abstractmethod
    def confirm_withdrawal(self): pass

    @abstractmethod
    def eject_card(self): pass


class WaitingForCardState(ATMState):
    def insert_card(self):
        print("Card inserted.")
        self.atm.set_state(CardVerificationState(self.atm))

    def verify_card(self, valid): print("Insert the card first.")
    def enter_pin(self, pin_correct): print("Insert the card first.")
    def select_amount(self): print("Insert the card first.")
    def verify_amount(self, valid): print("Insert the card first.")
    def confirm_withdrawal(self): print("Insert the card first.")
    def eject_card(self): print("No card to eject.")


class CardVerificationState(ATMState):
    def insert_card(self): print("Card already inserted.")
    def verify_card(self, valid):
        if valid:
            print("Card verified.")
            self.atm.set_state(WaitingForPinState(self.atm))
        else:
            print("Card rejected.")
            self.atm.set_state(CardRejectedState(self.atm))

    def enter_pin(self, pin_correct): print("Verify the card first.")
    def select_amount(self): print("Log in with PIN.")
    def verify_amount(self, valid): pass
    def confirm_withdrawal(self): pass
    def eject_card(self): print("Card cannot be ejected yet.")


class CardRejectedState(ATMState):
    def insert_card(self): print("Card already inserted.")
    def verify_card(self, valid): pass
    def enter_pin(self, pin_correct): pass
    def select_amount(self): pass
    def verify_amount(self, valid): pass
    def confirm_withdrawal(self): pass
    def eject_card(self):
        print("Card rejected. Ejecting the card.")
        self.atm.set_state(WaitingForCardState(self.atm))


class WaitingForPinState(ATMState):
    def insert_card(self): print("Card already inserted.")
    def verify_card(self, valid): pass

    def enter_pin(self, pin_correct):
        if pin_correct:
            print("PIN correct.")
            self.atm.set_state(AmountSelectionState(self.atm))
        else:
            print("Incorrect PIN. Please try again.")
            self.atm.set_state(WaitingForPinState(self.atm))

    def select_amount(self): print("Enter PIN first.")
    def verify_amount(self, valid): pass
    def confirm_withdrawal(self): pass
    def eject_card(self): print("Ejecting the card.")


class AmountSelectionState(ATMState):
    def insert_card(self): pass
    def verify_card(self, valid): pass
    def enter_pin(self, pin_correct): pass

    def select_amount(self):
        print("Amount selected.")
        self.atm.set_state(AmountVerificationState(self.atm))

    def verify_amount(self, valid): pass
    def confirm_withdrawal(self): pass
    def eject_card(self): print("Ejecting the card.")


class AmountVerificationState(ATMState):
    def insert_card(self): pass
    def verify_card(self, valid): pass
    def enter_pin(self, pin_correct): pass
    def select_amount(self): pass

    def verify_amount(self, valid):
        if valid:
            print("Amount verified.")
            self.atm.set_state(WithdrawalConfirmationState(self.atm))
        else:
            print("Invalid amount. Returning to selection.")
            self.atm.set_state(AmountSelectionState(self.atm))

    def confirm_withdrawal(self): pass
    def eject_card(self): print("Ejecting the card.")


class WithdrawalConfirmationState(ATMState):
    def insert_card(self): pass
    def verify_card(self, valid): pass
    def enter_pin(self, pin_correct): pass
    def select_amount(self): pass
    def verify_amount(self, valid): pass

    def confirm_withdrawal(self):
        print("Withdrawal confirmed.")
        self.atm.set_state(CardEjectionState(self.atm))

    def eject_card(self): print("Withdrawal not confirmed yet.")


class CardEjectionState(ATMState):
    def insert_card(self): pass
    def verify_card(self, valid): pass
    def enter_pin(self, pin_correct): pass
    def select_amount(self): pass
    def verify_amount(self, valid): pass
    def confirm_withdrawal(self): pass

    def eject_card(self):
        print("Card ejected.")
        self.atm.set_state(WaitingForCardState(self.atm))
