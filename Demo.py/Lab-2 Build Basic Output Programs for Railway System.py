train_name = "Rajdhani Express"
train_number = 12951
source_station = "Mumbai"
destination_station = "Delhi"
ticket_price = 2450.75

print("Welcome to Indian Railway Reservation Syastem")
print("Train name :",train_name)
print("Train Number :",train_number)
print("Source Station :", source_station)
print("Destination Station :",destination_station)


print(type(train_name))
print(type(train_number))
print(type(ticket_price))

passenger_name = "Rahul Sharma"
seat_number = "B2-45"
is_confirmed = True

ticket_price_integer = int(ticket_price)
print(type(ticket_price_integer))

train_number_string = str(train_number)
print(type(train_number_string))


passenger_name = "Rahul Sharma"
seat_number = "B2-45"
Confirmation_status = "Confirmed"

print("----------- Railway Ticket -----------")
print("Passenger Name = ",passenger_name)
print("Seat Number =", seat_number)
print("Ticket status =",Confirmation_status)
print("--------------------------------------")



#-------------------------------------------------------------------------------------------------------------------------
# Lab - 3 Store and Manage Ticket Data Using Variables

passenger_name = "Rahul Sharma"
Passenger_age = 28
gender = "male"
mobile_number = 9876543210

print("Passenger Name :",passenger_name)
print("Passenger Age :",Passenger_age)
print("Gender :",gender)
print("Mobile Number :",mobile_number)

train_name = "Rajdhani Express"
seat_number = "B2-B5"
ticket_price = 2450
Journey_date = "25-May-2026"

number_of_passengers = 3
ticket_price = 2450

total_fare = number_of_passengers*ticket_price
print("Total Fare :",total_fare)

gst_percentage = 5
gst_amount = (total_fare*gst_percentage)/100
print("GST Amount :",gst_amount)

final_amount = total_fare+gst_amount
print("Final Payable Amount :",final_amount)

print("----------- Indian Railways Ticket -----------")
print("Passenger Name :",passenger_name)
print("Train Name     :",train_name)
print("Seat Number    :",seat_number)
print("journey Date   :",Journey_date)
print("Passengers     :",number_of_passengers)
print("Ticket Fare    :",total_fare)
print("GST Amount     :",gst_amount)
print("Final Amount   :",final_amount)
print("----------------------------------------------")