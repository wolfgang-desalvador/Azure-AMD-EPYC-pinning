import unittest

from ..sku_milan import HB120v3
  

class HB120V3(unittest.TestCase):

    def test_IMPIPinning(self):    
        self.maxDiff=None    
        self.assertEqual(HB120v3(16).getMPIString('IMPI'), '-genv I_MPI_PIN_PROCESSOR_LIST=0,8,16,24,30,38,46,54,60,68,76,84,90,98,106,114')
        self.assertEqual(HB120v3(32).getMPIString('IMPI'), '-genv I_MPI_PIN_PROCESSOR_LIST=0,1,8,9,16,17,24,25,30,31,38,39,46,47,54,55,60,61,68,69,76,77,84,85,90,91,98,99,106,107,114,115')
        self.assertEqual(HB120v3(64).getMPIString('IMPI'), '-genv I_MPI_PIN_PROCESSOR_LIST=0,1,2,3,8,9,10,11,16,17,18,19,24,25,26,27,30,31,32,33,38,39,40,41,46,47,48,49,54,55,56,57,60,61,62,63,68,69,70,71,76,77,78,79,84,85,86,87,90,91,92,93,98,99,100,101,106,107,108,109,114,115,116,117')
        self.assertEqual(HB120v3(96).getMPIString('IMPI'), '-genv I_MPI_PIN_PROCESSOR_LIST=0,1,2,3,4,5,8,9,10,11,12,13,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,38,39,40,41,42,43,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,68,69,70,71,72,73,76,77,78,79,80,81,84,85,86,87,88,89,90,91,92,93,94,95,98,99,100,101,102,103,106,107,108,109,110,111,114,115,116,117,118,119')

    def test_PMPIPinning(self):    
        self.assertEqual(HB120v3(16).getMPIString('PMPI'), '-affopt=coreindex -affmanual=0x808080820202020808080820202020')
        self.assertEqual(HB120v3(32).getMPIString('PMPI'), '-affopt=coreindex -affmanual=0xc0c0c0c30303030c0c0c0c30303030')
        self.assertEqual(HB120v3(48).getMPIString('PMPI'), '-affopt=coreindex -affmanual=0xe0e0e0e38383838e0e0e0e38383838')
        self.assertEqual(HB120v3(64).getMPIString('PMPI'), '-affopt=coreindex -affmanual=0xf0f0f0f3c3c3c3cf0f0f0f3c3c3c3c')
        self.assertEqual(HB120v3(96).getMPIString('PMPI'), '-affopt=coreindex -affmanual=0xfcfcfcfff3f3f3ffcfcfcfff3f3f3f')

    def test_OMPIPinning(self):    
        self.maxDiff=None    
        self.assertEqual(HB120v3(16).getMPIString('OMPI'), '--bind-to cpulist:ordered --cpu-set 0,8,16,24,30,38,46,54,60,68,76,84,90,98,106,114')
        self.assertEqual(HB120v3(32).getMPIString('OMPI'), '--bind-to cpulist:ordered --cpu-set 0,1,8,9,16,17,24,25,30,31,38,39,46,47,54,55,60,61,68,69,76,77,84,85,90,91,98,99,106,107,114,115')
        self.assertEqual(HB120v3(64).getMPIString('OMPI'), '--bind-to cpulist:ordered --cpu-set 0,1,2,3,8,9,10,11,16,17,18,19,24,25,26,27,30,31,32,33,38,39,40,41,46,47,48,49,54,55,56,57,60,61,62,63,68,69,70,71,76,77,78,79,84,85,86,87,90,91,92,93,98,99,100,101,106,107,108,109,114,115,116,117')
        self.assertEqual(HB120v3(96).getMPIString('OMPI'), '--bind-to cpulist:ordered --cpu-set 0,1,2,3,4,5,8,9,10,11,12,13,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,38,39,40,41,42,43,46,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,68,69,70,71,72,73,76,77,78,79,80,81,84,85,86,87,88,89,90,91,92,93,94,95,98,99,100,101,102,103,106,107,108,109,110,111,114,115,116,117,118,119')

        

if __name__ == '__main__':
    unittest.main()
    