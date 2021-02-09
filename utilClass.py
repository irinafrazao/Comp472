# Team Members:
# PLEASE ADD NAME AND ID
# Irina Patrocinio-Frazao 40024714
# PLEASE ADD NAME AND ID

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import math
import copy

# TASK 0: Split data set in a training and an evaluation part (80/20)

# This method reads a dataset and returns 2 arrays:
# polarity_labels is an array of all the sentiment polarity labels
# reviews is an array where each element is an array of the words in a review
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
    
    
# TASK 2: Run 3 different ML models (Naive Bayes Classifier, Base-DT and Best-DT)

# Naive Bayes Classifier

# This method is used to get the probabilities from the training set
# log_prior_probabilities is a dictionary with each label associated with a log probability
# log_conditional_probabilities is a dictionary with a label key and a value being another dictionary
# where the key is the word and the value is the associated log probability P(word|class)
def train_naive_bayes_classifier(reviews, labels, smoothing_alpha):
    
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
       
    # get complete vocabulary (no duplicates, assuming that all the words in the docs are in vocabulary)
    complete_vocabulary = set()
    for label,frequencies in total_word_frequencies_by_class.items():
        for word in frequencies:
            if word not in complete_vocabulary:
                complete_vocabulary.add(word)

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
            smoothed_word_frequency = value + smoothing_alpha
            smoothed_total_word_in_label = total_words_by_class[category] + (len(complete_vocabulary) * smoothing_alpha)
            temp_counter[key] = math.log(smoothed_word_frequency / smoothed_total_word_in_label, 10)
        log_conditional_probabilities[category] = temp_counter
        
    return log_prior_probabilities, log_conditional_probabilities

# This method is used to get the score of a review for a certain label using the training probabilities
def score_review_label_naive_bayes(review, label, log_prior_probabilities, log_conditional_probabilities):
    score = log_prior_probabilities[label]
    for word in review:
        score += log_conditional_probabilities[label][word]
        
    return float(score)
        
        
# This method is used to classify a specific review in one of the possible labels using the training probabilities
# Returns the label this new review is most likely to be of
def classify_naive_bayes(review, log_prior_probabilities, log_conditional_probabilities):
    scores = {}
    possible_labels = get_distribution_data_from_dataset(log_prior_probabilities.keys());
    
    for label in possible_labels:
        scores[label] = score_review_label_naive_bayes(review, label, log_prior_probabilities, log_conditional_probabilities)
     
    highest_score = max(scores.values())
    
    for key,value in scores.items():
         if value == highest_score:
             classified_label = key
    
    return classified_label

            