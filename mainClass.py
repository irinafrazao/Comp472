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
util.show_distribution_plot(training_polarity_labels, "Distribution of Training Dataset")
util.show_distribution_plot(evaluation_polarity_labels, "Distribution of Evaluation Dataset")


# TASK 2: Run 3 different ML models (Naive Bayes Classifier, Base-DT and Best-DT)

# Naive Bayes Classifier (TODO: NEED TO ADD SMOOTHING!!)  
# JUST A TEST THAT WAS IN OUR NOTES - TO BE DELETED AFTER
test_labels = ["spam", "spam", "spam", "ham", "ham"]
test_reviews = [["cheap","viagra","sale"], ["best","viagra"], ["book","trip"], ["cheap","book","sale","viagra"], ["book"]]
(prior, conditional) = util.train_naive_bayes_classifier(test_reviews, test_labels)
print(prior)
print(conditional)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

