from .cpu_milan import Milan7V73X
from .sku_base import SKU


class HB120v3(SKU):
    def __init__(self, cpuCores=None):
        super().__init__([Milan7V73X(), Milan7V73X()])
        if cpuCores is not None:
            self.subscribe(cpuCores)