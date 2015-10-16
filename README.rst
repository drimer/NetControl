==========
NetControl
==========

Web-based software to monitor and control data in your LAN network


Description
===========

As it is at the moment, this app hardly does anything. It only lists the devices
connected to your LAN network. Its main objective (which needs to be implemented) is
to give the option to select what device is able to use a certain service outside the
network.

An example of a use case would be to select the mobile phones of our kids, and
prevent them from accessing Facebook until they've completed their school homework.
Re-enabling access would be a manual step too, as for the time being I don't intend to
add any timers.


Set-up instrucions
==================

Run:

.. code-block:: bash

    $ pip install -r requirements.txt"

Make sure the following packages are present in your
system:

* phantomjs

Using the app
=============

Run:

.. code-block:: bash

    $ sudo python manage.py runserver 8000

Running it as sudo or root is important as the app needs it in order to retrieve MAC
addresses from the network.

Open the following link in your browser: http://localhost:8000/

