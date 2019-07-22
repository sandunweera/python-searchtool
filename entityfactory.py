from organizations import OrganizationManager
from tickets import TicketManager
from users import UserManager
import const


class EntityFactory:
    @staticmethod
    def getInstance(type):
        if type == const.USERS:
            return UserManager()
        elif type == const.ORGANIZATIONS:
            return OrganizationManager()
        elif type == const.TICKETS:
            return TicketManager()