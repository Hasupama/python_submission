class Cities:
    def __init__(self):
        # Names of cities in Sweden

        self.city_names = ['Stockholm', 'Uppsala', 'Gävle', 'Luleå', 'Jönköping',
                           'Malmö', 'Gothenburg', 'Västerås', 'Umeå', 'Örebro']

        # Distance matrix for 10 cities. Distances are symmetric.
        self.distances = [
            [0, 69, 172, 904, 325, 614, 472, 105, 636, 199],  # Distances from City 0
            [69, 0, 107, 839, 390, 678, 453, 77, 571, 174],  # Distances from City 1
            [172, 107, 0, 738, 493, 782, 518, 144, 470, 239],  # Distances from City 2
            [904, 839, 738, 0, 1225, 1513, 1251, 877, 270, 969],  # Distances from City 3
            [325, 390, 493, 1225, 0, 291, 147, 308, 956, 213],  # Distances from City 4
            [614, 678, 782, 1513, 291, 0, 274, 597, 1245, 502],  # Distances from City 5
            [472, 453, 518, 1251, 147, 274, 0, 377, 983, 282],  # Distances from City 6
            [105, 77, 144, 877, 308, 597, 377, 0, 608, 95],  # Distances from City 7
            [636, 571, 470, 270, 956, 1245, 983, 608, 0, 704],  # Distances from City 8
            [199, 174, 239, 969, 213, 502, 282, 95, 704, 0]   # Distances from City 9
        ]

    # To get city name by index
    def get_city_name(self, index):
        return self.city_names[index]

    # To get the distances between two cities
    def get_distance(self, city1, city2):
        return self.distances[city1][city2]