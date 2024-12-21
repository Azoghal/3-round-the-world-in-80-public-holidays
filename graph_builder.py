# Build the graph

# the nodes are each:
# - a country on a date
# - e.g. 20-Dec-Spain

# the edges are:
# - between all nodes for adjacent dates
# - i.e. 20-Dec-<CountryA> -> 21-Dec<CountryB> for all available CountryA and CountryB

# the graph is:
# - directed - time moves forwards
# - acyclic - (until we allow moving countries in the same day)

# we have a smaller example to test with that runs from Jan-09 to Jan-17

import networkx as nx
from typing import Dict

class CountryNode:
    """
    A graph node representing the fact that a particular country has a public holiday on the particular date
    """
    
    def __init__(self, country: str, date: str, is_start: bool = False):
        """
        Initializes a Node object.

        Args:
            country (str): The name of the country.
            is_start (bool, optional): Whether this node is the starting node. Defaults to False.
        """
        self.full_name = f"{date}-{country}"
        self.country = country
        self.date = date
        self.is_start = is_start

    def __str__(self):
        """Returns a string representation of the node."""
        return f"{self.full_name}"

    def __repr__(self):
        """Returns a string representation of the node for debugging."""
        return str(self)

def build_graph(countries_by_date: Dict[str, list[str]]) -> nx.Graph:
    start_node = CountryNode("START","STR-00", True)
    G = nx.Graph()
    G.add_node(start_node)
    return G


# Think the easy approach is to:
# - give each node the name MMM-DD-<CountryName>
# - add all those 
