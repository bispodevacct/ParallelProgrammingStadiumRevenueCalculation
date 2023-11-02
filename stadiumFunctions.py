import random

# Function to fill the sector
def fillSector(sector, capacity, fullPrice):
    for i in range(0, capacity):
        if random.randint(0, 1) == 0:
            sector.append(fullPrice)
        else:
            sector.append(fullPrice // 2)

# Function to create the sector
def createSector():
    return []

# Function to calculate the sector revenue
def calculateSectorRevenue(sector):
    return sum(sector)