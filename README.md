# NEAT-Flappy-Bird
This project runs the NEAT algorithm to train an ai agent to play flappy bird (in flappybird.py).  NEAT stands for neuro-evolution of augmenting topologies, and this algorithm essentially creates a pool of genomes corresponding to a different ai model.  In each generation, each model is ranked based on its fitness score and models with similar enough genomic distances have the opportunity to mate, or aggregate the parent models to create a unique child model.  Additionally, between generations, there is a probability for mutation as defined by the config-feedforward.txt file for traits such as adding/removing connections, connection weights, adding/removing nodes, activation functions, etc.

# Best Model Demo
The best model here took 4 generations to successfully pass the score threshold, meaning it can successfully play flappy bird indefinitely without losing.  The best model has the following architecture:  
![](https://github.com/nick-pellegrin/NEAT-Flappy-Bird/blob/main/model.png)  
where the gray squares are the input nodes, the blue circle is the output node, green connections have positive weights and red connections have negative weights.  As flappy bird is a very easy game to play, the model required to play it successfully is minimal.  The goal of the NEAT algorithm is to create the most efficient model architecture necessary to accomplich a task. So rather than using a needlessly large model to play flappy bird, NEAT has managed to create a model using only one hidden node.  

Here is a video of all the models in the gene pool going through the evolution process over a few generations in order to produce the best model pictured above:
![]()

