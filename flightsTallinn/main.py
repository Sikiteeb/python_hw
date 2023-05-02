from csv import reader
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# I also did a version with using cartopy, but in my opinion, this Basemap version is slightly
# better looking. Even though lakes remain uncoloured as Basemap does not do that.


def draw_map():
    fig, ax = plt.subplots(figsize=(15, 12))
    eu_map = Basemap(
        projection="merc",
        llcrnrlat=20,
        urcrnrlat=70,
        llcrnrlon=-45,
        urcrnrlon=50,
        resolution="l",
    )

    eu_map.drawcoastlines()
    eu_map.fillcontinents(color='#054C0D')
    eu_map.drawcountries()
    eu_map.drawlsmask(land_color='#054C0D', ocean_color='#050F4C')  # does not have lake_color attribute
    eu_map.drawrivers(linewidth=0.5, linestyle='solid', color='#050F4C', zorder=5)
    eu_map.drawmapboundary(fill_color='#05284C')

    pre_covid_data = process_csv("otselennud20.csv")
    post_covid_data = process_csv("otselennud23.csv")

    draw_connections(pre_covid_data, post_covid_data, eu_map)
    # Add legend
    pre_covid_marker = plt.Line2D([0], [0], marker='o', color='w', label='Before COVID-19',
                                  markerfacecolor='white', markersize=8)
    post_covid_marker = plt.Line2D([0], [0], marker='o', color='w', label='After COVID-19',
                                   markerfacecolor='red', markersize=8)
    ax.legend(handles=[pre_covid_marker, post_covid_marker], loc='upper right')

    ax.set_title("Direct flights from Tallinn, before and after COVID-19, by Sigrid Hanni")
    plt.savefig("flightMap.png")
    plt.show()


def draw_connections(pre_covid_data, post_covid_data, eu_map):
    tallinn = [24.832799911499997, 59.41329956049999]

    for airport in pre_covid_data:
        if airport == "TLL":
            continue
        longitude = float(pre_covid_data[airport]["Longitude"])
        latitude = float(pre_covid_data[airport]["Latitude"])
        # airport labels
        plt.annotate(airport, xy=eu_map(longitude, latitude), verticalalignment="center", color="white")

        x, y = eu_map(longitude, latitude)

        eu_map.plot(x, y, marker=".", color="white", markersize=8)

        # covid flights
        eu_map.drawgreatcircle(longitude, latitude, tallinn[0], tallinn[1], linewidth=1, color="white")

    for airport in post_covid_data:
        if airport == "TLL":
            continue
        longitude = float(post_covid_data[airport]["Longitude"])
        latitude = float(post_covid_data[airport]["Latitude"])
        # airport labels
        plt.annotate(airport, xy=eu_map(longitude, latitude), verticalalignment="center", color="white")

        x, y = eu_map(longitude, latitude)

        eu_map.plot(x, y, marker=".", color="red", markersize=8)

        # after covid flights
        eu_map.drawgreatcircle(longitude, latitude, tallinn[0], tallinn[1], linewidth=1, color="red")


def get_airports_data(flight):
    airports_data = []
    file = r"HW3/" + flight
    with open(file, "r", encoding="utf-8") as read_file:
        csv_reader = reader(read_file)
        for row in csv_reader:
            airports_data.append(row[0].split(";")[1])

    return airports_data


def process_csv(flight):
    airports = get_airports_data(flight)
    headers = [
        "ID",
        "Name",
        "City",
        "Country",
        "IATA",
        "ICAO",
        "Latitude",
        "Longitude",
        "Altitude",
        "Timezone",
        "DST",
        "DZ",
        "Type",
        "Source",
    ]

    airports_dict = {}
    file = r"HW3/airports.dat"
    with open(file, "r", encoding="utf-8") as read_obj:
        csv_reader = reader(read_obj)
        # Skip the header row
        next(csv_reader)
        for row in csv_reader:

            iata = row[4]
            if iata in airports:
                airports_dict[iata] = {}
                for counter, header in enumerate(headers):
                    airports_dict[iata][header] = row[counter]

    return airports_dict


def main():
    draw_map()


if __name__ == "__main__":
    main()
