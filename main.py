import re
import bs4
from URL_Requests import get_html

html = get_html()

soup = bs4.BeautifulSoup(html, 'html.parser')

table_data = soup.find('table', {'class': 'infobox ib-settlement vcard'})
clean_table_data = table_data.get_text(separator="\n", strip=True)

clean_temp_data = ""
all_tables = soup.find_all('table', class_ = 'Wikitable')
for table in all_tables:
    if "Climate" in table.text or "climate" in table.text:
        temp_table = table
        clean_temp_data = temp_table.get_text(separator="\n", strip=True)
        break


def get_city_name():
    city_name_pattern = r".+"
    city_name_match = re.search(city_name_pattern, clean_table_data).group(0)
    return city_name_match

def get_municipality_population():
    municipality_population_pattern = r"Population[\s\S]*?(\d+,[\d+,]+)"
    municipality_population_match = re.search(municipality_population_pattern, clean_table_data).group(1)
    return municipality_population_match

def get_urban_population():
    urban_population_pattern = r"Population[\s\S]*?Urban[\s\S]*?(\d+,[\d+,]+)"
    urban_population_match = re.search(urban_population_pattern, clean_table_data)
    if urban_population_match == None:
        urban_population_match = "-"
        return urban_population_match
    return urban_population_match.group(1)

def get_metro_population():
    metro_population_pattern =r"Population[\s\S]*?Metro[\s\S]*?(\d+,[\d+,]+)"
    metro_population_match = re.search(metro_population_pattern, clean_table_data)
    if metro_population_match == None:
        metro_population_match = "-"
        return metro_population_match
    return metro_population_match.group(1)

def get_municipality_area():
    municipality_area_pattern = r"Area[\s\S]*?(\d+[\d+,.]+\s*km)"
    municipality_area_match = re.search(municipality_area_pattern, clean_table_data).group(1)
    return municipality_area_match

def get_urban_area():
    urban_area_pattern = r"Area[\s\S]*?Urban[\s\S]*?(\d+[\d+,.]+\s*km)"
    urban_area_match = re.search(urban_area_pattern, clean_table_data)
    if urban_area_match == None:
        urban_area_match = "-"
        return urban_area_match
    return urban_area_match.group(1)

def get_metro_area():
    metro_area_pattern = r"Area[\s\S]*?Metro[\s\S]*?(\d+[\d+,.]+\s*km)"
    metro_area_match = re.search(metro_area_pattern, clean_table_data)
    if metro_area_match == None:
        metro_area_match = "-"
        return metro_area_match
    return metro_area_match.group(1)

def get_country():
    country_pattern = r"Country[\s\S]*?(\w+[\w ]+)"
    country_match = re.search(country_pattern, clean_table_data).group(1)
    return country_match

def get_elevation():
    elev_pattern = r"Elevation|elevation[\s\S]*?([\d]+)\s*m"
    elev_match = re.search(elev_pattern, clean_table_data).group(1)
    return elev_match

def get_coords():
    coords_pattern = r"Coordinates[\s\S]*?([\d\.\"°′″NESW \n]+)"
    coords_match = re.search(coords_pattern, clean_table_data).group(1)
    return coords_match

def get_timezone():
    timezone_pattern = r"\nTime zone[\s\S]*?(\w+[\w \d–\+:]+)"
    stimezone_pattern = r"DST[\s\S]*?(\w+[\w \d\-\+:]+)"
    timezone_match = re.search(timezone_pattern, clean_table_data).group(1)
    stimezone_match = re.search(stimezone_pattern, clean_table_data)
    if stimezone_match == None:
        stimezone_match = "-"
    return timezone_match + "\n     Summer: " + stimezone_match.group(1)

print("Name: " + get_city_name())
print("Population: " + get_municipality_population())
print("     Urban: " + get_urban_population())
print("     Metro: " + get_metro_population())
print("Area (km2): " + get_municipality_area())
print("     Urban: " + get_urban_area())
print("     Metro: " + get_metro_area())
print("Country: " + get_country())
print("Coordinates:" + get_coords().replace("\n", " "))
print("Elevation: " + get_elevation() + "m")
print("Timezone: " + get_timezone())

print(clean_temp_data)
