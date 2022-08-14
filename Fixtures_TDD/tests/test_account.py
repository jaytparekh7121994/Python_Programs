"""
Test Cases TestAccountModel
"""
import json
from unittest import TestCase
from models import db
from models.account import Account

ACCOUNT_DATA_JSON = 'tests/fixtures/account_data.json'
ACCOUNT_DATA = {}


class TestAccountModel(TestCase):
    """ Test Account Model """

    @classmethod
    def setUpClass(cls):
        """ Connect and load needed by tests """
        db.create_all()
        global ACCOUNT_DATA
        with open(ACCOUNT_DATA_JSON) as account_data_json:
            ACCOUNT_DATA = json.load(account_data_json)
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        """Disconnect from Database"""
        db.session.close()
        
    def setUp(self) -> None:
        """Truncate the tables"""
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self) -> None:
        """Remove the session"""
        db.session.remove()
        
    ###############################################
    #          T E S T  C A S E S                 #
    ###############################################
    
    def test_create_an_account(self):
        """ Testing creating an account """
        accnt = Account(**ACCOUNT_DATA[0])
        accnt.create()
        self.assertEqual(len(Account.all()), 1)

    def test_create_all_account(self):
        """ Testing if all account data are created """
        for data in ACCOUNT_DATA:
            accnt = Account(**data)
            accnt.create()
        # Length of account created == Lengh of Account Data (json)
        # Avoiding arbitary number
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))
