# Hello old friend, it's been a while since i wrote any python

# Things we need to do:
# 
# Parse the public holiday files
#   - remove any countries I don't believe in (a joke, but we'll try to keep out of micronations and unrecognised places if possible)
#   - eventually producing a graph with a node for each country for each day of the year that is a public holiday
#   - and at first with edges between all nodes in adjacent dates
#   

import parse

def main():
    # Example usage:
    filepath = "public_holidays.txt"  # Replace with your file path
    date_map, country_set = parse.parse_country_data(filepath)

    # sanity check that the map is sensible
    query_date=input("What date would you like to check? (MMM-DD) ")
    print(f"Holidays: {date_map[query_date.lower()]}")

    # do what we actually want to do

if __name__ == "__main__":
    main()