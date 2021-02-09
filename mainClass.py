# Team Members:
# PLEASE ADD NAME AND ID
# Irina Patrocinio-Frazao 40024714
# PLEASE ADD NAME AND ID

import utilClass as util


# TASK 0: Split data set in a training and an evaluation part (80/20)
all_polarity_labels, all_reviews = util.read_document("dataset1.txt")

split_point_index = int(0.80 * len(all_reviews))
training_reviews = all_reviews[:split_point_index]
training_polarity_labels = all_polarity_labels[:split_point_index]
evaluation_reviews = all_reviews[split_point_index:]
evaluation_polarity_labels = all_polarity_labels[split_point_index:]


# TASK 1: Plot the distribution of the number of the instances in each class (polarity label)
util.show_distribution_plot(all_polarity_labels, "Distribution of Complete Dataset (Training and Evaluation)")


# TASK 2: Run 3 different ML models (Naive Bayes Classifier, Base-DT and Best-DT)

# Naive Bayes Classifier 
# Train the model
(prior, conditional) = util.train_naive_bayes_classifier(training_reviews, training_polarity_labels, 0.5)
print(prior)
print(conditional)

# Use the model to evaluate new data (just a test for now until task 3)
classified_label = util.classify_naive_bayes(["a","top-quality","performance"], prior, conditional)    
print(classified_label) 
print(evaluation_polarity_labels[0])

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

