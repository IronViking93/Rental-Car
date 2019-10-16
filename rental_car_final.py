import sys

#asks the user for the rental code
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
Budget = 'B'
Daily = 'D'
Weekly = 'W'

#asks the user for the amount days or weeks the rental
#will be used based on the rental code provided
if rentalCode == 'B':
  rentalPeriod = int(input("Number of Days Rented:\n"))
elif rentalCode == 'D':
  rentalPeriod = int(input("Number of Days Rented:\n"))
else:
  rentalPeriod = int(input("Number of Weeks Rented:\n"))

#calculates the base charge according to the provided
#rental code
if rentalCode == 'B':
  baseCharge = float(rentalPeriod) *  40.00
if rentalCode == 'D':
  baseCharge = float(rentalPeriod) * 60.00
if rentalCode == 'W':
  baseCharge = float(rentalPeriod) * 100.00

#asks the user for the odometer reading at the start and
#end of the rental use and calcuates the total miles the
#vehicle was driven
odoStart = input("Starting Odometer Reading:\n")
odoEnd = input("Ending Odometer Reading:\n")
totalMiles = int(odoEnd) - int(odoStart)

#calculates any addiontal mile charge based on the rental
#code and the total miles or average miles driven
if rentalCode == 'B':
  mileCharge = float(totalMiles * 0.25)
averageDayMiles = totalMiles / rentalPeriod
if rentalCode == 'D' and averageDayMiles < 100:
  mileCharge = 0.00
elif rentalCode == 'D' and averageDayMiles > 100:
  extraMiles = averageDayMiles - 100
  mileCharge = float(extraMiles * 0.25)
averageWeekMiles = totalMiles / rentalPeriod
if rentalCode == 'W' and averageWeekMiles <= 900:
  mileCharge = 0.00
elif averageWeekMiles > 900:
  mileCharge = float(100 + rentalPeriod)

#displays the rental summery to the user
print("Rental Summary")
print("Rental Code: " + str(rentalCode))
print("Rental Period: " + str(rentalPeriod))
print("Starting Odometer: " + str(odoStart)) 
print("Ending Odometer: " + str(odoEnd))
print("Miles Driven: " + str(totalMiles))
print("Amount Due: " + '$' + str("%0.2f" %(mileCharge + baseCharge)))