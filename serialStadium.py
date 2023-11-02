import time
import stadiumFunctions as sf
import stadiumConstants as sc

# Catch the starting time
start = time.time()

# Create the stadium sectors
upperNorth = sf.createSector()
lowerNorth = sf.createSector()
upperSouth = sf.createSector()
lowerSouth = sf.createSector()
upperWest  = sf.createSector()
lowerWest  = sf.createSector()
upperEast  = sf.createSector()
lowerEast  = sf.createSector()

# Fill the stadium sectors
sf.fillSector(upperNorth, sc.UPPER_NORTH_CAPACITY, sc.UPPER_NORTH_FULL_PRICE)
sf.fillSector(lowerNorth, sc.LOWER_NORTH_CAPACITY, sc.LOWER_NORTH_FULL_PRICE)
sf.fillSector(upperSouth, sc.UPPER_SOUTH_CAPACITY, sc.UPPER_SOUTH_FULL_PRICE)
sf.fillSector(lowerSouth, sc.LOWER_SOUTH_CAPACITY, sc.LOWER_SOUTH_FULL_PRICE)
sf.fillSector(upperWest,  sc.UPPER_WEST_CAPACITY,  sc.UPPER_WEST_FULL_PRICE)
sf.fillSector(lowerWest,  sc.LOWER_WEST_CAPACITY,  sc.LOWER_WEST_FULL_PRICE)
sf.fillSector(upperEast,  sc.UPPER_EAST_CAPACITY,  sc.UPPER_EAST_FULL_PRICE)
sf.fillSector(lowerEast,  sc.LOWER_EAST_CAPACITY,  sc.LOWER_EAST_FULL_PRICE)

# Declaire the revenues list
revenues = []

# Sum and append each sector revenue to the revenues list
revenues.append(sf.calculateSectorRevenue(upperNorth))
revenues.append(sf.calculateSectorRevenue(lowerNorth))
revenues.append(sf.calculateSectorRevenue(upperSouth))
revenues.append(sf.calculateSectorRevenue(lowerSouth))
revenues.append(sf.calculateSectorRevenue(upperWest))
revenues.append(sf.calculateSectorRevenue(lowerWest))
revenues.append(sf.calculateSectorRevenue(upperEast))
revenues.append(sf.calculateSectorRevenue(lowerEast))

# Sum the revenues
revenue = sum(revenues)

# Catch the finishing time
finish = time.time()

# Display the result
print(f'Revenue: {revenue}')
print(f'Time: {round(finish - start, 3)}')