from search.entityfactory import EntityFactory
from core.statemachine import StateMachine
from search.searchrelations import SearchRelationManager
from enum import Enum
from core import const


class State(Enum):
    START = 1
    READY = 2
    USER = 3
    USER_KEY = 4
    USER_VALUE = 5
    ORG = 6
    ORG_KEY = 7
    ORG_VALUE = 8
    TICKET = 9
    TICKET_KEY = 10
    TICKET_VALUE = 11
    QUIT = 98
    ERROR = 99


class App:

    def __init__(self):
        self.entity_manager = None

    # Start of Finite State Machine Wiring
    def start_transitions(self, input):
        if input != const.QUIT:
            return State.READY
        else:
            return State.QUIT

    def ready_transitions(self, input):
        global entity_manager
        if input == const.ONE:
            entity_manager = EntityFactory.getInstance(const.USERS)
            return State.USER
        elif input == const.TWO:
            entity_manager = EntityFactory.getInstance(const.ORGANIZATIONS)
            return State.ORG
        elif input == const.THREE:
            entity_manager = EntityFactory.getInstance(const.TICKETS)
            return State.TICKET
        elif input == const.QUIT:
            return State.QUIT
        else:
            return State.ERROR

    def user_transitions(self, input):
        if input == const.ONE:
            global entity_manager
            print(entity_manager.get_schema())
            return State.USER
        elif input == const.TWO:
            return State.USER_KEY
        elif input == const.QUIT:
            return State.QUIT
        else:
            return State.ERROR

    def user_key_transitions(self, input):
        if input == const.QUIT:
            return State.QUIT
        else:
            global key
            key = input
            return State.USER_VALUE

    def user_value_transitions(self, input):
        if input == const.QUIT:
            return State.QUIT
        else:
            global key
            k = key

            global entity_manager
            hits = entity_manager.search(k, input)

            for hit in hits:
                for relation in SearchRelationManager.search_relation_map[const.USERS]:
                    EntityFactory.getInstance(
                        relation.entity).search_relations(relation, hit)

            return State.READY

    def org_transitions(self, input):
        if input == const.ONE:
            global entity_manager
            print(entity_manager.get_schema())
            return State.ORG
        elif input == const.TWO:
            return State.ORG_KEY
        elif input == const.QUIT:
            return State.QUIT
        else:
            return State.ERROR

    def org_key_transitions(self, input):
        if input == const.QUIT:
            return State.QUIT
        else:
            global key
            key = input
            return State.ORG_VALUE

    def org_value_transitions(self, input):
        if input == const.QUIT:
            return State.QUIT
        else:
            global key
            k = key

            hits = entity_manager.search(k, input)

            for hit in hits:
                for relation in SearchRelationManager.search_relation_map[const.ORGANIZATIONS]:
                    obj = EntityFactory.getInstance(relation.entity)
                    obj.search_relations(relation, hit)

            return State.READY

    def ticket_transitions(self, input):
        if input == const.ONE:
            global entity_manager
            print(entity_manager.get_schema())
            return State.TICKET
        elif input == const.TWO:
            return State.TICKET_KEY
        elif input == const.QUIT:
            return State.QUIT
        else:
            return State.ERROR

    def ticket_key_transitions(self, input):
        if input == const.QUIT:
            return State.QUIT
        else:
            global key
            key = input
            return State.TICKET_VALUE

    def ticket_value_transitions(self, input):
        if input == const.QUIT:
            return State.QUIT
        else:
            global key
            k = key

            hits = entity_manager.search(k, input)

            for hit in hits:
                for relation in SearchRelationManager.search_relation_map[const.TICKETS]:
                    obj = EntityFactory.getInstance(relation.entity)
                    obj.search_relations(relation, hit)

            return State.READY
    # End of Finite State Machine Wiring

    if __name__ == "__main__":

        # Creating a new instance of Finite State Machine
        m = StateMachine()

        # Wiring the states of FSM. Refer the diagram in the documentation
        m.add_state(State.START, start_transitions,
                    message="Type 'quit' to exit at any time, press 'Enter' to continue\n")
        m.add_state(State.READY, ready_transitions, message="\n* Press 1 to search by users.\n"
                    "* Press 2 to search by organizations\n"
                    "* Press 3 to search by tickets\n"
                    "* Type 'quit' to exit\n")

        # User Pipeline
        m.add_state(State.USER, user_transitions, message="\n* Press 1 to List the fields available for Users\n"
                    "* Press 2 to search by User\n"
                    "* Type 'quit' to exit\n")
        m.add_state(State.USER_KEY, user_key_transitions,
                    message="Enter search term\n")
        m.add_state(State.USER_VALUE, user_value_transitions,
                    message="Enter search value\n")

        # Organization Pipeline
        m.add_state(State.ORG, org_transitions, message="\n* Press 1 to List the fields available for Organizations\n"
                    "* Press 2 to search by Organization\n"
                    "* Type 'quit' to exit\n")
        m.add_state(State.ORG_KEY, org_key_transitions,
                    message="Enter search term\n")
        m.add_state(State.ORG_VALUE, org_value_transitions,
                    message="Enter search value\n")

        # Ticket Pipeline
        m.add_state(State.TICKET, ticket_transitions, message="\n* Press 1 to List the fields available for Tickets\n"
                    "* Press 2 to search by Ticket\n"
                    "* Type 'quit' to exit\n")
        m.add_state(State.TICKET_KEY, ticket_key_transitions,
                    message="Enter search term\n")
        m.add_state(State.TICKET_VALUE, ticket_value_transitions,
                    message="Enter search value\n")

        # Quit State
        m.add_state(State.QUIT, None, end_state=1)

        # Error State to handle errors gracefully
        m.add_state(State.ERROR, ready_transitions, message="\n* Invalid Input. \n"
                    "\n* Press 1 to search by users.\n"
                    "* Press 2 to search by organizations\n"
                    "* Press 3 to search by tickets\n"
                    "* Type 'quit' to Exit\n")

        # Setting the Start Point
        m.set_start(State.START)

        # Invoking the Finite State Machine
        m.run()
