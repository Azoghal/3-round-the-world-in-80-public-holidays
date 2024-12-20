def parse_country_data(filepath):
    """
    Parses a file with date-country data and returns a dictionary and a set.

    Args:
        filepath: The path to the input file.

    Returns:
        A tuple containing:
        - date_country_map: A dictionary where keys are dates (strings) and 
          values are lists of countries (strings).
        - all_countries: A set of all unique countries (strings).
        Returns None, None if there is an error reading the file.
    """

    date_country_map = {}
    all_countries = set()

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                line_parts = line.split(",")
                if len(line_parts) < 2:
                    print(f"Error: bad number of parts: {len(line)}") 
                    return None, None

                date_month = line_parts[0].strip()
                date_day = line_parts[1].strip()

                countries = [country.strip() for country in line_parts[2:] if country != ""]
                if len(countries) == 1 and countries[0]=="":
                    countries = []

                date_country_map[f"{date_month}-{date_day}"] = countries
                all_countries.update(countries)
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

    return date_country_map, all_countries
