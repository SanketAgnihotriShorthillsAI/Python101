def dict1(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

dict1(Name="Sanket", Age=21)