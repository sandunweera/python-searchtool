from whoosh.fields import Schema, ID, TEXT, BOOLEAN, NUMERIC
from search.entity import EntityManager


class TicketManager(EntityManager):

    def __init__(self):
        self.schema = Schema(id=ID(stored=True),
                             url=TEXT(stored=True),
                             external_id=TEXT(stored=True),
                             created_at=TEXT(stored=True),
                             type=TEXT(stored=True),
                             subject=TEXT(stored=True),
                             description=TEXT(stored=True),
                             priority=TEXT(stored=True),
                             status=TEXT(stored=True),
                             submitter_id=NUMERIC(stored=True),
                             assignee_id=NUMERIC(stored=True),
                             organization_id=NUMERIC(stored=True),
                             tags=TEXT(stored=True),
                             has_incidents=BOOLEAN(stored=True),
                             due_at=TEXT(stored=True),
                             via=TEXT(stored=True)
                             )

        self.context = "tickets"
        self.create_index()
