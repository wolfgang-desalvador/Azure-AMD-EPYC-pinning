import argparse
from .sku_milan import HB120v3
from .sku_genoa import HB176v4, HX


SKU_MAP = {
    'HB120v3': HB120v3,
    'HB176v4': HB176v4,
    'HX': HX
}


def main():
    parser = argparse.ArgumentParser(
    description='Returns mpirun string for proper pinning')

    parser.add_argument('--sku', type=str,
                        help='SKU Name. It can be HB120v3, HB120v2, HB60')

    parser.add_argument('--cpus', type=int,
                        help='Number of CPUs for which pinning is desired')

    parser.add_argument('--mpi', type=str,
                        help='MPI version. It can be IMPI, PMPI, OMPI.')

    args = parser.parse_args()

    if args.sku not in SKU_MAP:
        raise NotImplementedError('SKU {} not supported. SKU should be in {}').format(args.sku, ",".join(list(SKU_MAP.keys())))

    if args.mpi not in ['OMPI', 'IMPI', 'PMPI']:
        raise NotImplementedError('MPI {} not supported. SKU should be in IMPI, PMPI, OMPI.').format(args.mpi)

    print(SKU_MAP[args.sku](args.cpus).getMPIString(args.mpi))