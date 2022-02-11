
# Write a Python Program to implement the following:
# Make a class Bus which has the following attributes:
# • Name of the Bus Conductor
# • Maximum Speed Limit
# • Maximum capacity
# • Ticket fare

# Read the attached csv file which contains the following:
# • Name of the bus stop
# • Number of passenger waiting

# Write a function BusBoard() which takes an object of the Bus (say Bus1) class and the csv file as input
# and does the following:
# • Read the contents of the csv file
# • And print the number of passengers Bus1 picks up at each station (it can go on picking people till
# number of passengers in bus is less than max capacity)
# • Print the number of passengers waiting whom the Bus1 won't be able to pick
# • Assume Bus1 starts from Station A and distance between each station is 20 kilometers,
# calculate the minimum duration for which the bus drives until the bus gets filled.
# • Print the conductor’s name and his total earnings.



import csv
# reading the csv file
print("reading the csv file")
with open('Station list.csv', 'r') as f:
    file = f.read()
    print(file)

# open the file in read mode
filename = open('Station list.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
Station = []
no_of_passengers = []

 
# iterating over each row and append
# values to empty list
for col in file:
    Station.append(col['Station D'])
    no_of_passengers.append(col['Number of passengers waiting'])
   
 
# printing lists of indivisual
print("                       *********")
print("indivisual list of the stations and the number of passengerss waitong at the stations")
print('station:', Station)
print('no_of_passengers:', no_of_passengers)

#printing list of passengers as integer form
if __name__ == '__main__':
    passengers = list(map(int, no_of_passengers))
    print("passengers(in interger form) :"   +   str (passengers)) 

# crating class bus
class bus:
    def __init__(self, name, speed, seatcapacity, fare):
        self.name = name
        self.speed = speed
        self.seatcapacity = seatcapacity
        self.fare = fare
        

    def getstatus(self):
        print("                        *******")
        print(f"the Name of the Bus Conductor is {self.name}")
        print(f"the maximum speed limit of the Bus is {self.speed} kmph")
        print(f"the maximum seat capacity of the Bus is {self.seatcapacity}")
        print(f"the ticket fare of the Bus is Rs. {self.fare}")
    
# creating busboard function
    def busboard(self):
        sum  = 0
        for i in range (len(passengers)):
            sum = sum + passengers[i]
            if(sum < 73):
                print("           *******")
                print(f"the bus is in {Station[i]}  and picks up  {passengers[i]} passengers")
                print(f"total no of passenger in the bus is {sum} ")
                print(f"money earned in {Station[i]} is Rs. {passengers[i]*40} /-")
                print(f"total money earned is Rs. {sum*40} /-")
                print(f"duration of time of drriving till now is {(i*20)/40} hours")
                
            elif (sum == 73):
                print("           *******")
                print(f"the bus is in {Station[i]}  and picks up {passengers[i]} passengers")
                print(f"the bus is fulled in station {Station[i]} with no. of passengers is {sum} ")
                print(f"the total money earned by the conductor {self.name} is Rs. {sum*40} /-")
                print("           *******")
                print(f"the minimum duration drives until the bus gets filled is {(i*20)/40} hours")
                
            else:
                print("           *******")
                print("!!!   NO SEAT   !!!")
                print(f"the bus is in {Station[i]} station as there is no seat for {passengers[i]} passengers")
                print(f"bus is full, total number of passengers not picked by bus {sum-73}")
    
 
#  printing the data of all
bus1 = bus("Satya Ranjan Dutta", 40 ,73 , 40)
bus1.getstatus()
bus1.busboard()







