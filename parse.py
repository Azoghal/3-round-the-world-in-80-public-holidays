def parse_country_data(filepath):
    """
    Parses a file with date-country data and returns a dictionary and a set.

    Expected format of file:
    MMM-DD, <Countries>

    For example:
    Jun-03, Thailand, Uganda
    
    Args:
        filepath: The path to the input file.

    Returns:
        A tuple containing:
        - date_country_map: A dictionary where keys are dates in format
            MMM-DD, all lower case and values are lists of countries 
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

                day_of_year = line_parts[0].strip()

                countries_part = line_parts[1]
                countries = countries_part.split(",")
                countries_stripped = [country.strip() for country in countries]

                date_country_map[day_of_year.lower()] = countries_stripped
                all_countries.update(countries_stripped)
            
            print(f"Number of days read: {len(date_country_map)}")
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

    return date_country_map, all_countries