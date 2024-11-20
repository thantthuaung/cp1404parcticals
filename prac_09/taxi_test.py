from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
distance = my_taxi.drive(40)
price = my_taxi.get_fare()
print(f"{my_taxi} and ${price}")

my_taxi.start_fare()
distance_2 = my_taxi.drive(100)
price_2 = my_taxi.get_fare()
print(f"{my_taxi} and ${price_2}")
