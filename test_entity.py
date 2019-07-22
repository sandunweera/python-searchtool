import unittest
import os
import shutil
from users import UserManager
from organizations import OrganizationManager
from tickets import TicketManager


class TestEntityManager(unittest.TestCase):

    def setUp(self):
        # Try deleting index folder
        shutil.rmtree("index", True)

    def test_create_user_index(self):
        UserManager()
        self.assertTrue(os.path.exists("index/users"))

    def test_create_organization_index(self):
        OrganizationManager()
        self.assertTrue(os.path.exists("index/organizations"))

    def test_create_ticket_index(self):
        TicketManager()
        self.assertTrue(os.path.exists("index/tickets"))

    def test_search_user(self):
        results = UserManager().search("id", "71")
        self.assertIsNotNone(results)

    def test_search_organization(self):
        results = OrganizationManager().search("id", "121")
        self.assertIsNotNone(results)

    def test_search_ticket(self):
        results = TicketManager().search("assignee_id", "38")
        self.assertIsNotNone(results)


if __name__ == '__main__':
    unittest.main()
