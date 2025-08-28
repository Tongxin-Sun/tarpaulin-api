from google.cloud import datastore
from .error import AuthError
from ..constants import ERROR_MESSAGE_404

client = datastore.Client()


def find_entity_by_property(kind, property_name, value, one_result=False):
    query = client.query(kind=kind)
    # query.add_filter(property_name, "=", value)
    query.add_filter(filter=datastore.query.PropertyFilter(property_name, "=", value))
    results = list(query.fetch())
    if one_result:
        if len(results) == 1:
            return results[0]
        elif not results:
            raise AuthError(ERROR_MESSAGE_404, 404)
        else:
            raise AuthError({"error": "Multiple users found for this sub"}, 500)

    return results
