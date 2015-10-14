from unittest import TestCase

from netcontrol.util import singleton


@singleton
class SingletonClass(object):
    pass


@singleton
class SingletonClassWithAttributes(object):
    @classmethod
    def setup_attributes(cls):
        cls.value = 1


class SingletonTest(TestCase):
    def test_that_only_instance_is_created(self):
        obj_one = SingletonClass()
        obj_two = SingletonClass()

        self.assertIs(obj_one, obj_two)

    def test_that_instance_is_created_using_setup_method(self):
        obj = SingletonClassWithAttributes()

        self.assertEqual(1, obj.value)

