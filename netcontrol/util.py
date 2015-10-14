from functools import wraps


def singleton(klass):
    class wrapper(klass):
        _instance = None

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(wrapper, cls).__new__(cls, *args,
                                                            **kwargs)

                setup_attrs_func = getattr(cls, 'setup_attributes', None)
                if setup_attrs_func:
                    setup_attrs_func()

            return cls._instance

    return wrapper
