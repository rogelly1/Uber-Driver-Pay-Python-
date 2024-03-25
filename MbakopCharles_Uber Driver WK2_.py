# Charles Mbakop, CMSC 105, 03/24/2024
# This program calculates the total pay for an Uber driver
milesDriven = float(input('What are you total miles Driven for the day? ')) # This is where the user inputs miles driven
hoursWorked = float(input('How many hours did you work today? ')) # This is where the uber driver (user) inputs their hours worked
tipsReceived = float(input('How much in tips did you receive? ')) # This is where the uber driver (user) inputs thier tips received
hourlyRate = 25 # This is the hourly rate ($25/hr) for the uber driver  
mileageCommission = .20 # This is the uber driver mileage commission. (the driver gets $.20 per mile driven) 
dailyWage = hoursWorked * hourlyRate # This calculates daily wage by multiplying hours worked times hourly rate
dailyCommisionPay = milesDriven * mileageCommission # This Calculates Daily Comission Pay by multiplying miles driven by the mileage comission 
dailyTotalPay = dailyWage + dailyCommisionPay + tipsReceived # Calculates Daily Total Pay 
weeklyTotalPay = dailyTotalPay * 5 # Calculates Weekly Total Pay 
dailyFormattedTotal = '$' + str(dailyTotalPay) # Formats Daily Total Pay with $
weeklyFormattedTotal = '$' + str(weeklyTotalPay) # Formats Weekly Total Pay with $
print('Daily Total Pay ' + dailyFormattedTotal) # Prints Formatted Daily Total Pay
print('Weekly Total Pay ' + weeklyFormattedTotal) # Prints Formatted Weekly Total Pay