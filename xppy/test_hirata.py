__author__ = 'aitor'


#!/usr/bin/python

import unittest

import os,inspect
thisdir=os.path.dirname(os.path.realpath(inspect.getfile(inspect.currentframe())))

class FooTest(unittest.TestCase):
    """Sample test case"""

    # preparing to test
    def setUp(self):
        """ Setting up for the test
        print "FooTest:setUp_:begin"
        ## do something...
        print "FooTest:setUp_:end"
        """
        pass

    # ending the test
    def tearDown(self):
        """Cleaning up after the test
        print "FooTest:tearDown_:begin"
        ## do something...
        print "FooTest:tearDown_:end"
        """
        pass

    # test routine A
    def testA(self):
        """Test routine A"""
        from xppy import parser
        out = parser.run(ode_file=os.path.join(thisdir,"../hirata04.ode"))
        assert(out['m'][1]==1.6405058)


