# Team Members:
# PLEASE ADD NAME AND ID
# Irina Patrocinio-Frazao 40024714
# PLEASE ADD NAME AND ID

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import copy
import math

# TASK 0: Split data set in a training and an evaluation part (80/20)

# This method reads a dataset and returns 2 arrays:
# polarity_labels is an array of all the sentiment polarity labels
# reviews is an array where each element is an array of the words in the review
def read_document(dataset_filename_with_extension):
    reviews = []
    polarity_labels = []
    
    with open(dataset_filename_with_extension, encoding='utf-8') as file:
        for line in file:
            #We are not interested in the topic label (0) or document identifier (2)
            wordsArray = line.strip().split()
            polarity_labels.append(wordsArray[1])
            reviews.append(wordsArray[3:])
            
    return polarity_labels, reviews


all_polarity_labels, all_reviews = read_document("dataset1.txt")

split_point_index = int(0.80 * len(all_reviews))
training_reviews = all_reviews[:split_point_index]
training_polarity_labels = all_polarity_labels[:split_point_index]
evaluation_reviews = all_reviews[split_point_index:]
evaluation_polarity_labels = all_polarity_labels[split_point_index:]


# TASK 1: Plot the distribution of the number of the instances in each class (polarity label)

# This methods takes a data set of labels and returns the frequency of those labels
# classes_and_distribution_dict is a dictionary of labels and associated frequencies
def get_distribution_data_from_dataset(dataset):
    classes_and_distribution_dict = Counter()
    for label in dataset:
        classes_and_distribution_dict[label] += 1
        
    return classes_and_distribution_dict
    
# This method shows a distribution plot using a data set of labels
def show_distribution_plot(dataset, title):
    dataset_distribution = get_distribution_data_from_dataset(dataset);

    y_values = np.arange(len(dataset_distribution))
    plt.bar(y_values, dataset_distribution.values())
    plt.xticks(y_values, dataset_distribution.keys())
    plt.title(title)
    for index,data in enumerate(dataset_distribution.values()):
        plt.text(x=index , y=data-(data/2) , s=f"{data}" , fontdict=dict(fontsize=20))
        
    plt.show()
    
show_distribution_plot(training_polarity_labels, "Distribution of Training Dataset")
show_distribution_plot(evaluation_polarity_labels, "Distribution of Evaluation Dataset")


# TASK 2: Run 3 different ML models (Naive Bayes Classifier, Base-DT and Best-DT)

# Naive Bayes Classifier (TODO: NEED TO ADD SMOOTHING!!)

# This method is used to get the probabilities from the training set
def train_naive_bayes_classifier(reviews, labels):
    
    # get prior probabilities P(neg) and P(pos)
    distribution = get_distribution_data_from_dataset(labels)
    log_prior_probabilities = {};
    for index, (key, val) in enumerate(distribution.items()):
        log_prior_probabilities[key] = math.log((int(val)/len(labels)), 10)
        
    # getting the frequency of existing words in the class
    total_word_frequencies_by_class = {}
    for category in log_prior_probabilities.keys():
       word_frequencies_by_class = Counter()
       
       for index,label in enumerate(labels):
           if label == category:
                for word in reviews[index]:
                    word_frequencies_by_class[word] += 1
       total_word_frequencies_by_class[category] = word_frequencies_by_class
       

    # getting total words in the classes
    total_words_by_class = {}
    for category,frequency_counter in total_word_frequencies_by_class.items():
        total_words_by_class[category] = sum(frequency_counter.values())
    
   
    # get conditional probabilities for every word in vocabulary example P(the|neg)
    #(assuming vocabulary are all the words in the dataset)
    log_conditional_probabilities = {};
    for category,frequency_counter in total_word_frequencies_by_class.items():
        temp_counter = copy.deepcopy(frequency_counter)
        for key,value in frequency_counter.items():
            temp_counter[key] = math.log(value / total_words_by_class[category], 10)
        log_conditional_probabilities[category] = temp_counter
        
    return log_prior_probabilities, log_conditional_probabilities
    
        
# JUST A TEST THAT WAS IN OUR NOTES - TO BE DELETED AFTER
test_labels = ["spam", "spam", "spam", "ham", "ham"]
test_reviews = [["cheap","viagra","sale"], ["best","viagra"], ["book","trip"], ["cheap","book","sale","viagra"], ["book"]]
(prior, conditional) = train_naive_bayes_classifier(test_reviews, test_labels)
print(prior)
print(conditional)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

