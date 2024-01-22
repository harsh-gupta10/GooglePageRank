import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def personalized_pagerank(adjacency_matrix, personalization_vector, damping_factor=0.85, max_iterations=100, epsilon=1e-6):
    normalized_matrix = adjacency_matrix / np.sum(adjacency_matrix, axis=0)
    num_nodes = len(adjacency_matrix)
    pagerank_vector = np.ones(num_nodes) / num_nodes
    for _ in range(max_iterations):
        new_pagerank_vector = (1 - damping_factor) / num_nodes + damping_factor * np.dot(normalized_matrix, pagerank_vector)
        if np.linalg.norm(new_pagerank_vector - pagerank_vector) < epsilon:
            break
        pagerank_vector = new_pagerank_vector
    personalized_pagerank_vector = np.multiply(pagerank_vector, personalization_vector)
    personalized_pagerank_vector /= np.sum(personalized_pagerank_vector)
    return personalized_pagerank_vector



def check_and_modify_stochastic(matrix):
    if np.any(np.all(matrix == 0, axis=0)):
        n = matrix.shape[1]  # Number of columns
        col_index = np.where(np.all(matrix == 0, axis=0))[0][0]
        correction = []
        for i in range(0, n):
            correction.append([]);
            for j in range(0, n):
                correction[i].append(0);
        for i in range(0, n):
            if(i!=col_index):
                for j in range(0, n):
                    correction[j][i] = 0;
            else:
                for j in range(0, n):
                    correction[j][i] = 1/n;
        correction = np.array(correction)
        matrix = matrix + correction
        return matrix
    else:
        return



adjacency_matrix = []
num_nodes = int(input("Enter the number of nodes: "))
print("Enter the adjacency matrix:")
for _ in range(num_nodes):
    row = list(map(int, input().split()))
    adjacency_matrix.append(row)
adjacency_matrix = np.array(adjacency_matrix)

personalization_vector = list(map(float, input("Enter the personalization vector: ").split()))
personalization_vector = np.array(personalization_vector)

adjacency_matrix2=adjacency_matrix.copy()



num_nodes1 = len(adjacency_matrix)
while num_nodes1>0:
    if np.any(np.all(adjacency_matrix == 0, axis=0)):
        adjacency_matrix=check_and_modify_stochastic(adjacency_matrix)
    num_nodes1=num_nodes1-1


pagerank = personalized_pagerank(adjacency_matrix, personalization_vector)
print("Final probabality of each:-",pagerank)
num_nodes = len(adjacency_matrix)
i=0
sum=0
while i<num_nodes:
    sum=sum+pagerank[i]
    i=i+1
    
print("Total Probabality:-",sum)


pagerank2=pagerank.copy()




pagerank=np.concatenate((pagerank, np.full(17-num_nodes, -1)))
WebPages = {
    "https://www.wikipedia.org/": pagerank[0],
    "https://www.apple.com" : pagerank[1],
    "https://www.youtube.com": pagerank[2],
    "https://www.facebook.com": pagerank[3],
    "https://www.amazon.com": pagerank[4],
    "https://www.twitter.com" : pagerank[5],
    "https://www.instagram.com" : pagerank[6],
    "https://www.linkedin.com" : pagerank[7],
    "https://www.pinterest.com" : pagerank[8],
    "https://www.snapchat.com" : pagerank[9],
    "https://www.reddit.com" : pagerank[10],
    "https://www.netflix.com" : pagerank[11],
    "https://www.spotify.com" : pagerank[12],
    "https://www.github.com" : pagerank[13],
    "https://www.microsoft.com" : pagerank[14],
    "https://www.google.com": pagerank[15],
    " https://www.cnn.com" : pagerank[16],
}
num_nodes = len(adjacency_matrix)
sorted_webpages = dict(sorted(WebPages.items(), key=lambda x: x[1], reverse=True))


print("Webpage order:-")
i=0
for key, value in sorted_webpages.items():
    if i<num_nodes:
        print(i+1,key, value)
    i=i+1



adjacency_matrix_Trans = np.transpose(adjacency_matrix2)
graph = nx.DiGraph(adjacency_matrix_Trans)
labels = {i: f"{i}\n{pagerank[i]}" for i in range(len(pagerank2))}
nx.draw(graph, with_labels=True, labels=labels, node_color='lightblue', node_size=500, font_size=12, edge_color='gray', arrows=True)
plt.show()
plt.savefig("figure.png")