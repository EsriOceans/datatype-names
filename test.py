import unittest
import arcpy

import datatype

class TestDataTypes(unittest.TestCase):
    def setUp(self):
        # create a data type object.
        self.dt = datatype.DataType()

    def testVersionMatches(self):
        self.assertTrue(arcpy.GetInstallInfo()['Version'] == self.dt.version)

    def testForKeyword(self):
        self.assertTrue('GPString' in self.dt.keywords)

    def testForLabels(self):
        self.assertTrue('Raster Band' in self.dt.labels)

    def testFormatWithSP(self):
        # test as if service pack is installed at 10.1
        self.dt.service_pack = '1'
        self.assertTrue(self.dt.service_pack == '1')
        self.assertTrue('DEFeatureClass' == self.dt.format('Feature Class'))
        self.assertTrue('DEFeatureClass' == self.dt.format('DEFeatureClass'))
       
    def testFormatWithoutSP(self):
        # now, test for 10.1 without the service pack where names aren't 
        # associated by keyword
        self.dt.service_pack = 'N/A'
        self.assertTrue(self.dt.service_pack == 'N/A')
        self.assertTrue('Feature Class' == self.dt.format('Feature Class'))
        self.assertTrue('Feature Class' == self.dt.format('DEFeatureClass'))


