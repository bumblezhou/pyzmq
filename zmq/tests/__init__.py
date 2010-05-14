#
#    Copyright (c) 2010 Brian E. Granger
#
#    This file is part of pyzmq.
#
#    pyzmq is free software; you can redistribute it and/or modify it under
#    the terms of the Lesser GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    pyzmq is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    Lesser GNU General Public License for more details.
#
#    You should have received a copy of the Lesser GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from unittest import TestCase

import zmq

#-----------------------------------------------------------------------------
# Utilities
#-----------------------------------------------------------------------------


class BaseZMQTestCase(TestCase):

    def setUp(self):
        self.context = zmq.Context(1,1)

    def create_bound_pair(self, type1, type2, interface='tcp://127.0.0.1'):
        """Create a bound socket pair using a random port."""
        s1 = zmq.Socket(self.context, type1)
        port = s1.bind_to_random_port(interface)
        s2 = zmq.Socket(self.context, type2)
        s2.connect('%s:%s' % (interface, port))
        return s1, s2

    def ping_pong(self, s1, s2, msg):
        s1.send(msg)
        msg2 = s2.recv()
        s2.send(msg2)
        msg3 = s1.recv()
        return msg3

class PollZMQTestCase(BaseZMQTestCase):
    pass

