"""
Test Cases TestAccountModel
"""
import json
from random import randrange
from unittest import TestCase
from models import db
from models.account import Account, DataValidationError
from factories import AccountFactory

ACCOUNT_DATA_JSON = 'tests/fixtures/account_data.json'
ACCOUNT_DATA = {}


class TestAccountModel(TestCase):
    """ Test Account Model """

    @classmethod
    def setUpClass(cls):  # runs before any tests
        """ Connect and load needed by tests """
        db.create_all()
        global ACCOUNT_DATA
        with open(ACCOUNT_DATA_JSON) as account_data_json:
            ACCOUNT_DATA = json.load(account_data_json)
        
    @classmethod
    def tearDownClass(cls):  # runs after all tests
        """Disconnect from Database"""
        db.session.close()
        
    def setUp(self) -> None:  # runs before each test
        """Truncate the tables"""
        self.rand = randrange(0, len(ACCOUNT_DATA))
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self) -> None:  # runs after each test
        """Remove the session"""
        db.session.remove()
        
    ###############################################
    #          T E S T  C A S E S                 #
    ###############################################
    
    def test_create_an_account(self):  # test case 1
        """ Testing creating an account """
        accnt = Account(**ACCOUNT_DATA[0])
        accnt.create()
        self.assertEqual(len(Account.all()), 1)

    def test_create_all_account(self):  # test case 2
        """ Testing creating all account """
        # Test if the length of account created == Lengh of Account Data (json)
        # Avoiding arbitary number
        for data in ACCOUNT_DATA:
            accnt = Account(**data)
            accnt.create()
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))

    def test_repr(self):  # test case 3
        """ Testing repr """
        accnt = Account()
        accnt.name = "Foo"
        self.assertEqual(str(accnt), "<Account 'Foo'>")
    
    def test_to_dict(self):  # test case 4
        """ Testing to_dict """
        data = ACCOUNT_DATA[self.rand]  # get a random account data
        accnt = Account(**data)
        result = accnt.to_dict()
        self.assertEqual(accnt.name, result['name'])
        self.assertEqual(accnt.email, result['email'])
        self.assertEqual(accnt.phone_number, result['phone_number'])
        self.assertEqual(accnt.disabled, result['disabled'])
        self.assertEqual(accnt.date_joined, result['date_joined'])

    def test_from_dict(self):  # test case 5
        """ Testing from_dict """
        data = ACCOUNT_DATA[self.rand]  # get a random account data
        accnt = Account()
        accnt.from_dict(data)
        self.assertEqual(accnt.name, data["name"])
        self.assertEqual(accnt.email, data["email"])
        self.assertEqual(accnt.phone_number, data["phone_number"])
        self.assertEqual(accnt.disabled, data["disabled"])
        
    def test_update_an_account(self):
        """ Test Account update using known data """
        data = ACCOUNT_DATA[self.rand]  # get a random account
        account = Account(**data)
        account.create()
        self.assertIsNotNone(account.id)
        account.name = "Rumpelstiltskin"
        account.update()
        found = Account.find(account.id)
        self.assertEqual(found.name, account.name)
    
    def test_invalid_id_on_update(self):
        """ Test invalid ID update """
        data = ACCOUNT_DATA[self.rand]  # get a random account
        accnt = Account(**data)
        accnt.id = None
        self.assertRaises(DataValidationError, accnt.update)
    
    def test_delete_an_account(self):
        """ Test Account delete using known data """
        data = ACCOUNT_DATA[self.rand]  # get a random account
        accnt = Account(**data)
        accnt.create()
        self.assertEqual(len(Account.all()), 1)
        accnt.delete()
        self.assertEqual(len(Account.all()), 0)

    def test_create_all_accounts_accountfactory(self):
        """ Test creating multiple account with fake data"""
        for _ in range(10):
            accnt = AccountFactory()
            accnt.create()
        self.assertEqual(len(Account.all()), 10)
    
    def test_create_an_account_accountfactory(self):
        """ Test creating an account with fake data"""
        accnt = AccountFactory()
        accnt.create()
        self.assertEqual(len(Account.all()), 1)
    
    def test_to_dict_accountfactory(self):
        """ Test creating an account with fake data"""
        accnt = AccountFactory()  # get a random account data
        result = accnt.to_dict()
        self.assertEqual(accnt.name, result["name"])
        self.assertEqual(accnt.email, result["email"])
        self.assertEqual(accnt.phone_number, result["phone_number"])
        self.assertEqual(accnt.disabled, result["disabled"])
    
    def test_from_dict_accountfactory(self):
        """ Test creating an account with fake data"""
        data = AccountFactory().to_dict()  # get a random account data
        accnt = Account()
        accnt.from_dict(data)
        self.assertEqual(accnt.name, data["name"])
        self.assertEqual(accnt.email, data["email"])
        self.assertEqual(accnt.phone_number, data["phone_number"])
        self.assertEqual(accnt.disabled, data["disabled"])
    
    def test_update_an_account_accountfactory(self):
        """ Test Account update using known data """
        account = AccountFactory()
        account.create()
        self.assertIsNotNone(account.id)
        account.name = "Rumpelstiltskin"
        account.update()
        found = Account.find(account.id)
        self.assertEqual(found.name, account.name)
    
    def test_invalid_id_on_update_accountfactory(self):
        """ Test invalid ID update """
        accnt = AccountFactory()
        accnt.id = None
        self.assertRaises(DataValidationError, accnt.update)
    
    def test_delete_an_account_accountfactory(self):
        """ Test Account delete using known data """
        account = AccountFactory()
        account.create()
        self.assertEqual(len(Account.all()), 1)
        account.delete()
        self.assertEqual(len(Account.all()), 0)