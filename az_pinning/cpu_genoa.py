from .ccd_base import CCD
from .cpu_base import CPU


class GenoaX(CPU):
    def __init__(self):
        super().__init__([ CCD(8), CCD(8), CCD(8), CCD(8),CCD(6), CCD(6), CCD(8), CCD(8), CCD(8), CCD(8), CCD(6), CCD(6)])
