from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {
            "name": "NISSAN",
            "description": "Great cars. Japanese technology",
            "country": "Japan",
            "year": 1950,
        },
        {
            "name": "Mercedes",
            "description": "Great cars. German technology",
            "country": "Germany",
            "year": 1932,
        },
        {
            "name": "Audi",
            "description": "Great cars. German technology",
            "country": "Germany",
            "year": 1940,
        },
        {
            "name": "Kia",
            "description": "Great cars. Korean technology",
            "country": "Japan",
            "year": 1972,
        },
        {
            "name": "Toyota",
            "description": "Great cars. Japanese technology",
            "country": "Japan",
            "year": 1948,
        },
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data["name"],
                description=data["description"],
                country=data["country"],
                year=data["year"],
            )
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {
            "name": "Pathfinder",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
            "price": 32000,
        },
        {
            "name": "Qashqai",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
            "price": 47000,
        },
        {
            "name": "XTRAIL",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
            "price": 22000,
        },
        {
            "name": "A-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
            "price": 35000,
        },
        {
            "name": "C-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
            "price": 40000,
        },
        {
            "name": "E-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
            "price": 80000,
        },
        {
            "name": "A4",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2],
            "price": 60000,
        },
        {
            "name": "A5",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2],
            "price": 80000,
        },
        {
            "name": "A6",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2],
            "price": 120000,
        },
        {
            "name": "Sorrento",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[3],
            "price": 25000,
        },
        {
            "name": "Carnival",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[3],
            "price": 36000,
        },
        {
            "name": "Cerato",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[3],
            "price": 64000,
        },
        {
            "name": "Corolla",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[4],
            "price": 12000,
        },
        {
            "name": "Camry",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[4],
            "price": 35000,
        },
        {
            "name": "Kluger",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[4],
            "price": 68000,
        },
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data["name"],
            car_make=data["car_make"],
            type=data["type"],
            year=data["year"],
            price=data["price"],
        )
