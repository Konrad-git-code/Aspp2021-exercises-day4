import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

sumRanks = numpy.zeros(1)
total = numpy.zeros(1)

sumRanks[0] = numpy.sum(rank)

comm.Reduce(sumRanks, total, op=MPI.SUM, root=0)

if comm.rank == 0:
	print(("Sum over all ranks is %f") % (total))

