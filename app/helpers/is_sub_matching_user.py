def is_sub_matching_user(client, user_id, sub):
    # Check if the JWT is valid, but doesn't belong to the user whose ID is in the path parameter
    user = client.get(client.key("users", user_id))
    if not user or user["sub"] != sub:
        return False
    return True
