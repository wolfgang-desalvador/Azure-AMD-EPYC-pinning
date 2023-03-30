class SKU:
    def __init__(self, CPUs):
        self.CPUs = CPUs

    def subscribe(self, numberOfCores):
        for _ in range(numberOfCores):
            sorted(self.CPUs, key=lambda cpu: (cpu.usedCores, -self.CPUs.index(cpu)))[0].subscribe(1)

        
    def __str__(self):
        return ''.join([str(cpu) for cpu in self.CPUs])

    def getMPIString(self, MPIType):
        if MPIType == 'PMPI':
            mpiParameters = '-affopt=coreindex -affmanual={}'.format(str(hex(int(str(self), 2))))
        elif MPIType == 'IMPI':
            mpiParameters = '-genv I_MPI_PIN_PROCESSOR_LIST=' + ','.join([str(coreIndex) for coreIndex, core in enumerate(str(self)) if core == '1'])
        elif MPIType == 'OMPI':
            mpiParameters = '--bind-to cpulist:ordered --cpu-set ' + ','.join([str(coreIndex) for coreIndex, core in enumerate(str(self)) if core == '1'])
        return mpiParameters