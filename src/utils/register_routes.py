def register_routes(api, routes, prefix):
    for route in routes:
        location = prefix + route[1]
        api.add_resource(route[0], location)