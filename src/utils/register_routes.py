def register_routes(api, routes):
    for route in routes:
        api.add_resource(route[0], route[1])
