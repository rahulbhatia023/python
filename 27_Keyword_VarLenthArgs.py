def person(name, **data):
    print(name)

    for x, y in data.items():
        print(x, y)


person('rahul', age=28, city='Pune', mobile=8149165759)
