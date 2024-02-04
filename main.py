import networkx as nx
import matplotlib.pyplot as plt

def main():
    # Generate a random graph
    # n = number of nodes, p = probability of edge creation
    G = nx.erdos_renyi_graph(n=20, p=0.2)

    # Draw the graph
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15)

    # Display the graph
    plt.show()

if __name__ == "__main__":
    main()
