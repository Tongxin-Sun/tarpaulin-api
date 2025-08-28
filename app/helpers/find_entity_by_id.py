from google.cloud import datastore

client = datastore.Client()


def find_entity_by_id(kind, id):
    entity = client.get(client.key(kind, id))
    return entity
