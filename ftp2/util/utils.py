class utils:
    def dealCookie(json, mycookie):
        keys = json.keys()
        for key in keys:
            mycookie.set_cookie(key, json[key])