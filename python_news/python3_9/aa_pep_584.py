# PEP 584 – Add Union Operators To dict

if __name__ == '__main__':
    d = {'spam': 1, 'eggs': 2, 'cheese': 3}
    e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}
    print(d | e)  # {'spam': 1, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'}
