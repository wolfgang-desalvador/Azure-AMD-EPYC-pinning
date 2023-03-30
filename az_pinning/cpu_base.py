class CPU:
    def __init__(self, CCDs):
        self.CCDs = CCDs

    @property
    def availableCCDS(self):
        return [ccd for ccd in self.CCDs if not ccd.fullySubscribed]

    def subscribe(self, numberOfCores):
        for _ in range(numberOfCores):
            sorted(self.availableCCDS, key=lambda x: (x.usedCores, -self.availableCCDS.index(x)))[0].subscribeCore()

    def unsubscribe(self, numberOfCores):
        for _ in range(numberOfCores):
            sorted(self.availableCCDS, key=lambda x: (-x.usedCores, self.availableCCDS.index(x)))[0].unsubscribeCore()
    
    def __str__(self):
        return ''.join([str(ccd) for ccd in self.CCDs])

    @property
    def unusedCores(self):
        return sum(ccd.unusedCores for ccd in self.CCDs)

    @property
    def usedCores(self):
        return sum(ccd.usedCores for ccd in self.CCDs)
