from whoosh.fields import Schema, ID, TEXT, BOOLEAN, NUMERIC
from search.entity import EntityManager


class UserManager(EntityManager):

    def __init__(self):
        self.schema = Schema(id=ID(stored=True),
                             url=TEXT(stored=True),
                             external_id=TEXT(stored=True),
                             name=TEXT(stored=True),
                             alias=TEXT(stored=True),
                             created_at=TEXT(stored=True),
                             active=BOOLEAN(stored=True),
                             verified=BOOLEAN(stored=True),
                             shared=BOOLEAN(stored=True),
                             locale=TEXT(stored=True),
                             timezone=TEXT(stored=True),
                             last_login_at=TEXT(stored=True),
                             email=TEXT(stored=True),
                             phone=TEXT(stored=True),
                             signature=TEXT(stored=True),
                             organization_id=NUMERIC(stored=True),
                             tags=TEXT(stored=True),
                             suspended=BOOLEAN(stored=True),
                             role=TEXT(stored=True)
                             )

        self.context = "users"
        self.create_index()
