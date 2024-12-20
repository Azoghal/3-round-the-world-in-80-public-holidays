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
    filepath = "public_holidays_non_regional_cleaned.txt"  # Replace with your file path

    parse.reformat(filepath)

    # date_map, country_set = parse.parse_country_data(filepath)
    
    # manual_filter_countries(country_set)

    # wr

def manual_filter_countries(country_set):
    yes = set()
    no = set()
    if country_set is not None:
        print(f"\n{len(country_set)} Unique Countries:")
        # for country in country_set:
        #     resp = input(f"Real country? {country} ")
        #     if resp in ["y", "Y"]:
        #         yes.update(country)
        #     else:
        #         no.update(country)
        print("\n".join(country_set))

    # print("the ones i don't believe in")
    # print(no)

if __name__ == "__main__":
    main()