from whoosh.fields import Schema, ID, TEXT, BOOLEAN
from search.entity import EntityManager


class OrganizationManager(EntityManager):
    def __init__(self):
        self.schema = Schema(id=ID(stored=True),
                             url=TEXT(stored=True),
                             external_id=TEXT(stored=True),
                             name=TEXT(stored=True),
                             domain_names=TEXT(stored=True),
                             created_at=TEXT(stored=True),
                             details=TEXT(stored=True),
                             shared_tickets=BOOLEAN(stored=True),
                             tags=TEXT(stored=True)
                             )

        self.context = "organizations"
        self.create_index()
