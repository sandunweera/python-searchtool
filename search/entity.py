import os
import json
import pprint
from whoosh.index import create_in
import whoosh.index as index
from whoosh.qparser import QueryParser


class EntityManager:

    context = None
    schema = None

    def __init__(self):
        pass

    def create_index(self):
        if not os.path.exists("index"):
            os.mkdir("index")

        index_path = "index/" + self.context
        if not os.path.exists(index_path):
            os.mkdir(index_path)
            ix = create_in(index_path, self.schema, indexname=self.context)
            writer = ix.writer()

            print("Indexing.... This may take few seconds. Entity = ", self.context)
            file = "json/tiny/" + self.context + ".json"
            with open(file) as entity_file:
                entities = json.load(entity_file)
                for entity in entities:
                    entity["id"] = str(entity["_id"])
                    writer.add_document(**entity)

            writer.commit()

    def get_schema(self):
        return self.schema

    def search_relations(self, relation, result):
        self.create_index()
        self.search(relation.field, str(result[relation.value]))

    def search(self, key, value):

        ix = index.open_dir("index/" + self.context, indexname=self.context)

        qp = QueryParser(key, schema=ix.schema)
        q = qp.parse(value)

        results = ix.searcher().search(q)

        if results.is_empty():
            print("No hits found")
        else:
            print("\n----- Search results for " + self.context +
                  " with " + key + " = " + value + "  --------\n")
            for result in results:
                self.print_results(result.fields())
                print("\n")

        return results

    def print_results(self, dct):
        for k, v in dct.items():
            print(f'{k:<20} {v}')
