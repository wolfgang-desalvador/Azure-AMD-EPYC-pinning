class CCD:
    def __init__(self, numberOfCores):
        '''Initialize basic CCD class

        Args:
            numberOfCores (int): number of cores in the CCD
        '''
        self.numberOfCores = numberOfCores
        self.usedCores = 0

    @property
    def unusedCores(self):
        '''Unused cores CCD

        Returns:
            _type_: _description_
        '''
        return self.numberOfCores - self.usedCores
    
    @property
    def fullySubscribed(self):
        return self.usedCores == self.numberOfCores

    def __str__(self):
        binaryString =  ''.join(['1' for _ in range(self.usedCores)]) 
        binaryString += ''.join(['0'  for _ in range(self.numberOfCores - self.usedCores)])

        return binaryString

    def subscribeCore(self):
        '''Suscribe single core

        Raises:
            IndexError: If too many cores are subscribed
        '''
        if self.usedCores < self.numberOfCores:
            self.usedCores += 1
        else:
            raise IndexError('CCD is already fully subscribed.')
        
    def unsubscribeCore(self):
        '''Unsuscribe single core

        Raises:
            IndexError: If all cores are unsuscribed
        '''
        if self.usedCores > 0:
            self.usedCores -= 1
        else:
            raise IndexError('CCD is totally unsuscribed.')
        
    def subscribeCores(self, numberOfCores):
        '''Suscribe multiple cores

        Args:
            numberOfCores (int): Subscribe multiple cores

        Raises:
            IndexError: If too many cores are subscribed
        '''
        for _ in range(numberOfCores):
            self.subscribeCore()

            
    def unsubscribeCores(self, numberOfCores):
        '''Unsuscribe multiple cores

        Args:
            numberOfCores (int): Unsubscribe multiple cores

        Raises:
            IndexError: If all cores are unsuscribed
        '''
        for _ in range(numberOfCores):
            self.unsubscribeCore()