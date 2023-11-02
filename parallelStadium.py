from mpi4py import MPI
import time
import stadiumFunctions as sf
import stadiumConstants as sc

# Initialize the MPI enviroment
comm = MPI.COMM_WORLD

# Get the number of process
size = comm.Get_size()

# Get the process rank
rank = comm.Get_rank()

# Calculating
if rank == 1:
    upperNorth = sf.createSector()
    sf.fillSector(upperNorth, sc.UPPER_NORTH_CAPACITY,  sc.UPPER_NORTH_FULL_PRICE)
    upperNorthRevenue = sf.calculateSectorRevenue(upperNorth)
    comm.send(upperNorthRevenue, 0)
elif rank == 2:
    lowerNorth = sf.createSector()
    sf.fillSector(lowerNorth, sc.LOWER_NORTH_CAPACITY, sc.LOWER_NORTH_FULL_PRICE)
    lowerNorthRevenue = sf.calculateSectorRevenue(lowerNorth)
    comm.send(lowerNorthRevenue, 0)
elif rank == 3:
    upperSouth = sf.createSector()
    sf.fillSector(upperSouth, sc.UPPER_SOUTH_CAPACITY, sc.UPPER_SOUTH_FULL_PRICE)
    upperSouthRevenue = sf.calculateSectorRevenue(upperSouth)
    comm.send(upperSouthRevenue, 0)
elif rank == 4:
    lowerSouth = sf.createSector()
    sf.fillSector(lowerSouth, sc.LOWER_SOUTH_CAPACITY, sc.LOWER_SOUTH_FULL_PRICE)
    lowerSouthRevenue = sf.calculateSectorRevenue(lowerSouth)
    comm.send(lowerSouthRevenue, 0)
elif rank == 5:
    upperWest = sf.createSector()
    sf.fillSector(upperWest, sc.UPPER_WEST_CAPACITY, sc.UPPER_WEST_FULL_PRICE)
    upperWestRevenue = sf.calculateSectorRevenue(upperWest)
    comm.send(upperWestRevenue, 0)
elif rank == 6:
    lowerWest = sf.createSector()
    sf.fillSector(lowerWest, sc.LOWER_WEST_CAPACITY, sc.LOWER_WEST_FULL_PRICE)
    lowerWestRevenue = sf.calculateSectorRevenue(lowerWest)
    comm.send(lowerWestRevenue, 0)
elif rank == 7:
    upperEast = sf.createSector()
    sf.fillSector(upperEast, sc.UPPER_EAST_CAPACITY, sc.UPPER_EAST_FULL_PRICE)
    upperEastRevenue = sf.calculateSectorRevenue(upperEast)
    comm.send(upperEastRevenue, 0)
elif rank == 8:
    lowerEast = sf.createSector()
    sf.fillSector(lowerEast, sc.LOWER_EAST_CAPACITY, sc.LOWER_EAST_FULL_PRICE)
    lowerEastRevenue = sf.calculateSectorRevenue(lowerEast)
    comm.send(lowerEastRevenue, 0)
else:
    # Catch the starting time
    start = time.time()
    
    # The list to receive the sectors revenue
    revenues = []

    # Appending the each revenue to the revenue list
    revenues.append(comm.recv(source=1))
    revenues.append(comm.recv(source=2))
    revenues.append(comm.recv(source=3))
    revenues.append(comm.recv(source=4))
    revenues.append(comm.recv(source=5))
    revenues.append(comm.recv(source=6))
    revenues.append(comm.recv(source=7))
    revenues.append(comm.recv(source=8))

    # Calculate total revenue
    revenue = sum(revenues)

    # Catch the finishing time
    finish = time.time()

    print(f'Revenue: {revenue}')
    print(f'Time: {round(finish - start, 3)}')

comm.Free()