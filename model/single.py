class MetaSigleton(type):
    _instces = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instces:
            cls._instces[cls] = super(MetaSigleton, cls).__call__(*args, **kwargs)
        return cls._instces[cls]
