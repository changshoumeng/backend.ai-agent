Backend.AI Agent
================

The Backend.AI Agent is a small daemon that reports the status of a worker
computater (either a physical server or a virtualized cloud instance)
to the manager and performs computation requests assigned by the manager.

Package Structure
-----------------

* ai.backend
   * agent: The agent daemon implementation


Installation
------------

Backend.AI Agent requires Python 3.6 or higher.  We highly recommend to use
`pyenv <https://github.com/yyuu/pyenv>`_ for an isolated setup of custom Python
versions that might be different from default installations managed by your OS
or Linux distros.

.. code-block:: sh

   pip install backend.ai-agent

For development
~~~~~~~~~~~~~~~

We recommend to use an isolated virtual environment.
This installs the current working copy and backend.ai-common as "editable" packages.

.. code-block:: sh

   git clone https://github.com/lablup/backend.ai-agent.git
   python -m venv /home/user/venv
   source /home/user/venv/bin/activate
   pip install -U pip setuptools   # ensure latest versions
   pip install -U -r requirements-dev.txt


Deployment
----------

Running from a command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Minimal command to execute:

.. code-block:: sh

   python -m ai.backend.agent.server --etcd-addr localhost:2379

The agent reads most configurations from the given etcd v3 server where
the cluster administrator or the Backend.AI manager stores all the necessary
settings.

By default the agent uses ``/var/cache/scratches`` directory for making temporary
home directories used by kernel containers (the ``/home/work`` volume mounted in
containers).  You can change the location by ``--scratch-root`` option.

For more arguments and options, run the command with ``--help`` option.

Example config for agent server/instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``/etc/supervisord/conf.d/agent.conf``:

.. code-block:: dosini

   [program:backend.ai-agent]
   user = user
   stopsignal = TERM
   stopasgroup = true
   command = /home/user/run-agent.sh

``/home/user/run-agent.sh``:

.. code-block:: sh

   #!/bin/sh
   source /home/user/venv/bin/activate
   exec python -m ai.backend.agent.server --etcd-addr localhost:2379

Networking
~~~~~~~~~~

Basically all TCP ports must be transparently open to the manager.

The operation of agent itself does not require both incoming/outgoing access to
the public Internet, but if the user's computation programs need, the docker
containers should be able to access the public Internet (maybe via some
corporate firewalls).

Several optional features such as automatic kernel image updates may require
outgoing public Internet access from the agent as well.
