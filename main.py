colors = ["black", "white"]
sizes = ["S", "M", "L"]

for tshirts in ((color, size) for color in colors for size in sizes):
    print(tshirts)
