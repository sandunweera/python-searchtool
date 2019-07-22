from search.organizations import OrganizationManager
from search.tickets import TicketManager
from search.users import UserManager
from core import const


class EntityFactory:
    @staticmethod
    def getInstance(type):
        if type == const.USERS:
            return UserManager()
        elif type == const.ORGANIZATIONS:
            return OrganizationManager()
        elif type == const.TICKETS:
            return TicketManager()