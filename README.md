# LSH for neural networks validation
This project is a personal research endeavor that remains a work in progress. I extend my apologies for any errors you may come across during your exploration.

## Idea
We present a novel method for validating generative models of temporal series. Our approach involves representing the data using a combination of a CUMSUM filter and a Piecewise Aggregate Approximation (PAA), which allows us to capture the different shapes of the data while retaining its essential features.

- Our proposed method draws inspiration from SAX and combines a CUMSUM filter with Piecewise Aggregate Approximation. This represents a unique and novel approach in this field.
- Leveraging this representation and local sensitive hashing, we can identify recurrent items in our database, regardless of their temporal or spatial dilation. This results in a visual representation of diverse patterns and their associated probabilities.
- We demonstrate the effectiveness of our approach by implementing it with a variational autoencoder.

## Results 
We consider a dataset D = {X1, . . . , XN } consisting of N i.i.d. samples from a continuous random vector. In our experiment, we choose Xi to be a random walk of size n with normally-distributed increments.
We have examined our dataset D for all possible k-mers. Several examples of these k-mers are shown in the following plots.

We observe that we can identify recurrent items in our database, regardless of their temporal or spatial dilation:
![Alt Text](https://github.com/c1adrien/LSH_for_neural_networks_validation/blob/main/LSH/results/area_of_interest_two_trajectory.png)



![Alt Text](https://github.com/c1adrien/LSH_for_neural_networks_validation/blob/main/LSH/results/second%20pattern.png)


Feel free to explore our code and documentation to learn more about this approach and its practical implications.
