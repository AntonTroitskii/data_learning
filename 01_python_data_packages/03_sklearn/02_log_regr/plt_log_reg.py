from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt

def simple_plot(c):
    
    colors = ListedColormap(['red', 'yellow'])
    
    data = list(zip(*c[0]))
    data_x = data[0]
    data_y = c[1]
    print(len(data_x), len(data_y))
    plt.scatter(data_x, data_y, c=c[1], cmap=colors)
    
c = datasets.make_classification(n_features = 1, 
                                  n_informative = 1, 
                                  n_redundant = 0, 
                                  n_clusters_per_class = 1, 
                                  class_sep=1, 
                                  random_state=0)
