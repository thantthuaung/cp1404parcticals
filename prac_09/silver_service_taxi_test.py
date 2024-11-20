from prac_09.silver_service_taxi import SilverServiceTaxi
my_taxi = SilverServiceTaxi("hummer", 200, 2)
my_taxi.drive(18)
print(f"{my_taxi} plus flagfall of ${my_taxi.get_fare()}")