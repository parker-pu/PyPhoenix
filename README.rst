pyphoenix
==================

``pyphoenix`` use java jar to operate phoenix

Installation
------------

.. figure:: https://secure.travis-ci.org/selwin/python-user-agents.png
   :alt: Build status

   Build status

``pyphoenix`` is hosted on
`PyPI <http://pypi.python.org/pypi/PyPhoenix/>`__ and can be installed
as such:

::

    pip install git+git://github.com/parker-pu/PyPhoenix.git

Alternatively, you can also get the latest source code from
Github_ and install it manually.

.. _Github: https://github.com/parker-pu/PyPhoenix

Usage
-----

For example:

.. code::

    from pyphoenix.phoenix import PhoenixDB

    sql = "SELECT * FROM user"
    pd = PhoenixDB(
        url = "jdbc:127.0.0.1:2181;",
        drive = "org.apache.phoenix.jdbc.PhoenixDriver",
        params = {'phoenix.schema.isNamespaceMappingEnabled': 'true'},
        jar_file = "xxx/phoenix-4.7.0-clabs-phoenix1.3.0-client.jar"
    )
    data = pd.execute(sql=sql)
    for row in data:
        print(row)
    pass

Changelog
---------

Version 0.1.0
~~~~~~~~~~~

-  Initial release

Initialize code development