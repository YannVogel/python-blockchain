# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ The get_last_blockchain_value function returns the last value of the current blockchain."""
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ The add_value function appends a new block to the blockchain.
    Arguments:
        :transaction_amount: The amount that should be added to the blockchain.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the user input as a float. """
    return float(input('Your transaction amount please: '))


def get_user_choice():
    return input('Your choice: ')


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)


tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Please choose: ')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')

print('Done!')
