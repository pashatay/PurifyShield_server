import random

class DataAnonymizer:
    def __init__(self):
        self.customer_name_counter = 1

    def anonymize_customer_names(self, series):
        def get_name(x):
            name = f'Customer {self.customer_name_counter}'
            self.customer_name_counter += 1
            return name
        return series.apply(get_name)

    def anonymize_social_security_numbers(self, series):
        return series.apply(lambda x: f'{random.randint(100, 999)}-XX-XXXX')

    def anonymize_account_numbers(self, series):
        def get_account_number(x):
            account_number = f'Account_{random.randint(1000000, 9999999)}'
            return account_number
        return series.apply(get_account_number)

    def anonymize_account_types(self, series):
        account_types = ['Account Type A', 'Account Type B', 'Account Type C']
        return series.apply(lambda x: random.choice(account_types))

    def anonymize_branch_codes(self, series):
        return series.apply(lambda x: f'Branch_{random.randint(1, 100)}')

    def anonymize_transaction_dates(self, series):
        return series.apply(lambda x: f'20{random.randint(10, 21)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}')

    def anonymize_transaction_amounts(self, series):
        return series.apply(lambda x: round(random.uniform(1, 1000), 2))

    def anonymize_transaction_types(self, series):
        transaction_types = ['Deposit', 'Withdrawal', 'Payment']
        return series.apply(lambda x: random.choice(transaction_types))

    def anonymize_balances(self, series):
        return series.apply(lambda x: round(random.uniform(1, 10000), 2))

    def anonymize_loan_amounts(self, series):
        return series.apply(lambda x: round(random.uniform(1000, 100000), 2))

    def anonymize_interest_rates(self, series):
        return series.apply(lambda x: round(random.uniform(1, 10), 2))

    def anonymize_credit_scores(self, series):
        return series.apply(lambda x: random.choice([300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850]))

    def anonymize_investment_details(self, series):
        return series.apply(lambda x: 'Investment Details')

    def anonymize_contact_info(self, series):
        return series.apply(lambda x: 'Contact Info')

    def anonymize_addresses(self, series):
        return series.apply(lambda x: 'Anonymized Address')

    def anonymize_dates_of_birth(self, series):
        return series.apply(lambda x: f'19{random.randint(50, 99)}-XX-XX')
