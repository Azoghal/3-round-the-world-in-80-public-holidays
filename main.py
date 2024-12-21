# Hello old friend, it's been a while since i wrote any python

# Things we need to do:
# 
# Parse the public holiday files
#   - remove any countries I don't believe in (a joke, but we'll try to keep out of micronations and unrecognised places if possible)
#   - eventually producing a graph with a node for each country for each day of the year that is a public holiday
#   - and at first with edges between all nodes in adjacent dates
#   

# %%

import parse
import graph_builder
import graph_drawer

# %%

def main():
    # Example usage:
    filepath = "public_holidays.txt"  # Replace with your file path
    countries_by_date, country_set = parse.parse_country_data(filepath)

    # sanity check that the map is sensible
    # query_date=input("What date would you like to check? (MMM-DD) ")
    # if query_date != "" and query_date != "n":
    #     print(f"Holidays: {countries_by_date[query_date.lower()]}")

    # do what we actually want to do
    graph = graph_builder.build_graph(countries_by_date)

    print(f"node count: {graph.number_of_nodes()}")
    print(f"edge count: {graph.number_of_edges()}")

    graph_drawer.draw_graph_simple(graph)

if __name__ == "__main__":
    main()

# %%
