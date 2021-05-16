class mycookie: 
    def _init():
        global mycookies
        mycookies = {}

    def get_cookie(key, defValue = None):
        try:
            return mycookies[key]
        except KeyError:
            return defValue

    def set_cookie(key, value):
        mycookies[key] = value

    def get_allcookie():
        return mycookies