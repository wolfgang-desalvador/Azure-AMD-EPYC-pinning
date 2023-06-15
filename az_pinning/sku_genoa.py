from .cpu_genoa import GenoaX
from .sku_base import SKU


class HB176v4(SKU):
    def __init__(self, cpuCores=None):
        super().__init__([GenoaX(), GenoaX()])
        if cpuCores is not None:
            self.subscribe(cpuCores)

class HX(HB176v4):
    pass