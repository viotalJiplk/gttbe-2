def register_routes(api, routes, prefix, isapi = True):
    for route in routes:
        if(isapi):
            location = "/backend" + prefix + route[1]
        else:
            location = prefix + route[1]
        api.add_resource(route[0], location)