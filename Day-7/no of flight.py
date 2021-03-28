initial_flight_count = int(input("Enter  no of initial flight: "))
takeoff_flight_count = int(input("Enter no of take off flight: "))
landing_flight_count = int(input("Enter no of landing flight: "))
current_flight_count = initial_flight_count+landing_flight_count-takeoff_flight_count
print("current no of flight = ", current_flight_count)


