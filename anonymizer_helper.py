import random

class DataAnonymizer:
    def __init__(self):
        pass

    # Anonymization functions for different categories of data
    def anonymize_customer_names(self, data):
        data['Customer Name'] = data['Customer Name'].apply(lambda x: 'Customer Name')

    def anonymize_social_security_numbers(self, data):
        data['Social Security Number'] = data['Social Security Number'].apply(lambda x: 'XXX-XX-XXXX')

    def anonymize_account_numbers(self, data):
        data['Account Number'] = data['Account Number'].apply(lambda x: 'Account Number')

    def anonymize_account_types(self, data):
        data['Account Type'] = data['Account Type'].apply(lambda x: 'Account Type')

    def anonymize_branch_codes(self, data):
        data['Branch Code'] = data['Branch Code'].apply(lambda x: 'Branch Code')

    def anonymize_transaction_dates(self, data):
        data['Transaction Date'] = data['Transaction Date'].apply(lambda x: 'Transaction Date')

    def anonymize_transaction_amounts(self, data):
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: random.uniform(1, 1000))

    def anonymize_transaction_types(self, data):
        data['Transaction Type'] = data['Transaction Type'].apply(lambda x: 'Transaction Type')

    def anonymize_balances(self, data):
        data['Balance After Transaction'] = data['Balance After Transaction'].apply(lambda x: random.uniform(1, 10000))

    def anonymize_loan_amounts(self, data):
        data['Loan Amount'] = data['Loan Amount'].apply(lambda x: random.uniform(1000, 100000))

    def anonymize_interest_rates(self, data):
        data['Interest Rate'] = data['Interest Rate'].apply(lambda x: random.uniform(1, 10))

    def anonymize_credit_scores(self, data):
        data['Credit Score'] = data['Credit Score'].apply(lambda x: random.randint(300, 850))

    def anonymize_investment_details(self, data):
        data['Investment Portfolio Details'] = data['Investment Portfolio Details'].apply(lambda x: 'Investment Portfolio Details')

    def anonymize_contact_info(self, data):
        data['Contact Information'] = data['Contact Information'].apply(lambda x: 'Contact Information')

    def anonymize_addresses(self, data):
        data['Residential Address'] = data['Residential Address'].apply(lambda x: 'Residential Address')

    def anonymize_dates_of_birth(self, data):
        data['Date of Birth'] = data['Date of Birth'].apply(lambda x: 'Date of Birth')
