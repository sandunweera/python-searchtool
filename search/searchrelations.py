class SearchRelation:

    def __init__(self, entity, field, value):
        self.entity = entity
        self.field = field
        self.value = value


class SearchRelationManager:

    search_relation_map = {
        'organizations': {SearchRelation('tickets', 'organization_id', 'id'), SearchRelation('users',  'organization_id', 'id')},
        'users': {SearchRelation('tickets',  'assignee_id', 'id'), SearchRelation('tickets', 'submitter_id', 'id'), SearchRelation('organizations', 'id', 'organization_id')},
        'tickets': {SearchRelation('users', 'id', 'submitter_id'), SearchRelation('users', 'id', 'assignee_id'), SearchRelation('organizations', 'id', 'organization_id')}
    }
