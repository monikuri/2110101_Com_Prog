infile = open("hotels.txt", "r")
hotels = []
for line in infile:
    [hotel, stars, review] = line.split(";")
    hotels.append([hotel, int(stars), float(review)])
infile.close()
# print(hotels)
star = int(input())
found_hotels = []
for h in hotels:
    if h[1] >= star:
        found_hotels.append([h[2], h[1], h[0]])
found_hotels.sort(reverse=True)
for h in found_hotels:
    print(h[2], h[1], h[0])
if len(found_hotels) == 0:
    print("Not Found")