def singleton(klass):
    class Wrapper(klass):
        _instance = None

        def __new__(cls, *args, **kwargs):
            # pylint:disable=E1002

            if not cls._instance:
                cls._instance = super(Wrapper, cls).__new__(cls, *args,
                                                            **kwargs)

                setup_attrs_func = getattr(cls, 'setup_attributes', None)
                if setup_attrs_func:
                    setup_attrs_func()

            return cls._instance

    return Wrapper
