import facebook


def query_profile_with_graph_api(profile_id, access_token):
    graph = facebook.GraphAPI(access_token)
    profile = graph.get_object(profile_id)
    return profile
