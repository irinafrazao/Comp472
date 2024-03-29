# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import math
import copy
import nltk
from nltk.corpus import stopwords  
import string
from sklearn import tree
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_recall_fscore_support
from codecs import open


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


#For decision Trees

# This method returns the feature list and the feature matrix for training reviews
def training_feature_matrix_DT(featureCountMax, dataCleanUp, training_reviews, training_polarity_labels):
    # get the frequencies of words for positive and negative classes
    word_frequencies_in_pos_reviews = Counter()
    word_frequencies_in_neg_review = Counter()
    labelCount = 0
    
    for review in training_reviews:
        if training_polarity_labels[labelCount] == "pos":
            for word in review:
                word_frequencies_in_pos_reviews[word] += 1
        else:
            for word in review:
                word_frequencies_in_neg_review[word] += 1
        labelCount+=1
            

    #create dictinonary with all words in positive reviews paired with the abs value of the difference in of appearances in negative reviews
    #do it for both the positive and negative reviews as some words may appear in one but not the other
    pos_difference_dict ={}
    neg_difference_dict ={}
    
    for word in word_frequencies_in_pos_reviews:
        difference = abs(word_frequencies_in_pos_reviews[word] - word_frequencies_in_neg_review[word])
        pos_difference_dict[word] = abs(difference)
    
    for word in word_frequencies_in_neg_review:
        difference = abs(word_frequencies_in_neg_review[word] - word_frequencies_in_pos_reviews[word])
        neg_difference_dict[word] = abs(difference)
    
    
    #combine dictionaries, removing duplicates with every word and the difference difference in frequency between positive and negative
    pos_difference_dict.update(neg_difference_dict)
    
    #sort the dictionary
    sorted_dict = sorted(pos_difference_dict.items(), key=lambda x: x[1])
    
    # using sorted data, pick 100 words with largest difference in frequency excluding words like "and" "is"....
    #try stopwords after
    featureCounter = 0
    featureList = []
    
    if dataCleanUp :
        data_cleanup_DT(sorted_dict, featureList, featureCounter, featureCountMax)
    else:
        for i in reversed(sorted_dict):
            featureList.append(i[0])
            featureCounter += 1
            if featureCounter == featureCountMax: break
        
        
    feature_existance_per_review = []

    for i in training_reviews:
        row = []
        for j in featureList:
            if j in i:
                row.append(1)
            else:
                row.append(0)
        feature_existance_per_review.append(row) 
      
    return feature_existance_per_review,featureList


# This method is used to cleanup data
def data_cleanup_DT(sorted_dict, featureList, featureCounter, featureCountMax):
    
    # punctuation
    # !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
    wordsWeDoNotWant = list(string.punctuation)
    
    nltk.download('stopwords')
    
    # stop words in english
    # ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll","you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's",
    # 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs','themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am',
    # 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does','did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of',
    # 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before','after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',
    # 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own',
    #'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should',"should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn',
    #"couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven',"haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan',
    #"shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn',"wouldn't"]
    wordsWeDoNotWant.append(stopwords.words('english'))
    
    for i in reversed(sorted_dict):
        if i[0] not in wordsWeDoNotWant:
            featureList.append(i[0])
            featureCounter += 1
        if featureCounter == featureCountMax: break
    
    return featureList
    

# This method trains the base decision tree
def setup_base_decision_tree(training_reviews, training_polarity_labels):
    
    feature_existance_per_review,featureList = training_feature_matrix_DT(100, False, training_reviews, training_polarity_labels)
    
    return feature_existance_per_review,featureList

# This method trains the best decision tree
def setup_best_decision_tree(training_reviews, training_polarity_labels):
    
     feature_existance_per_review,featureList = training_feature_matrix_DT(200, True, training_reviews, training_polarity_labels)
    
     return feature_existance_per_review,featureList
    

#Returns EVALUATION existance matrix        
def setup_evaluation_feature_matrix_decision_tree(featureList,evaluation_reviews):
    feature_existance_per_review =[]
    
    for i in evaluation_reviews:
        row = []
        for j in featureList:
            if j in i:
                row.append(1)
            else:
                row.append(0)
        feature_existance_per_review.append(row)
        
    return feature_existance_per_review, featureList



# TASK 3 : Generate output file with classification and performance evaluation

# This method is used to classify new data using a decision tree
# As input it needs: the feature matrix and labels of the training reviews and the feature matrix of the evaluation reviews
def classify_decision_tree(feature_existance_per_training_review,feature_existance_per_evaluation_review,training_polarity_labels):

    # build decision tree and fit it with training data
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    clf = clf.fit(feature_existance_per_training_review,training_polarity_labels)
    
    # evaluate new samples with tree
    guesses = clf.predict(feature_existance_per_evaluation_review[0])
    
    return guesses
    
# This method prints the output classification file and performance evaluation of a NB model
# Assumes the there is only 2 classes: NEG and POS
def print_NB_model_output_file_2_classes(filename_with_ext, index_evaluation_samples_start, evaluation_reviews,
                                      evaluation_polarity_labels, prior, conditional):
    bayes_output_file = open(filename_with_ext, "w")
    bayes_output_file.write("Naive Bayes Classifier\n")
    bayes_output_file.write("\n")
    
    sample_row_number = index_evaluation_samples_start
    classified_labels = []
    for test_review in evaluation_reviews:
        classified_label = classify_naive_bayes(test_review, prior, conditional)   
        classified_labels.append(classified_label)
        bayes_output_file.write(str(sample_row_number) + ", " + classified_label + "\n")
        sample_row_number += 1
    
    print_evaluation_parameters_2_classes(bayes_output_file, evaluation_polarity_labels, classified_labels)
    
    bayes_output_file.close()

# This method is used to print the evaluation file of the base decision tree
def print_base_model_output_file_2_classes(file_name_with_ext, base_guesses, evaluation_polarity_labels, split_point_index):
    base_tree_file = open(file_name_with_ext, "w")
    base_tree_file.write("Base Decision Tree Model\n")
    base_tree_file.write("\n")
    counterCheck = 0
    numCorrect = 0
    for i in base_guesses:
        
        if i == evaluation_polarity_labels[counterCheck]:
            numCorrect += 1
        counterCheck+=1
    
    
    y_true = evaluation_polarity_labels
    y_pred = base_guesses
    cm = confusion_matrix(y_true, y_pred, labels=["pos","neg"])
    
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["pos","neg"])
    disp.plot()
    
    scores = precision_recall_fscore_support(y_true,y_pred,average=None, labels=['pos','neg'])
    precision_POS = scores[0][0]
    precision_NEG = scores[0][1]
    recall_POS = scores[1][0]
    recall_NEG = scores[1][1]
    f1_measure_POS = scores[2][0]
    f1_measure_NEG = scores[2][1]
    
    tp = cm[0][0]
    fp = cm[0][1]
    fn = cm[1][0]
    tn = cm[1][1]
    
    accuracy = numCorrect/len(evaluation_polarity_labels)
    
    row = split_point_index
  
    for i in base_guesses:
        base_tree_file.write(str(row) + ", "+i+"\n")
        row+=1
    
    write_confusion_matrix_and_performance_measures(base_tree_file, accuracy, precision_NEG, recall_NEG, f1_measure_NEG, precision_POS, recall_POS, f1_measure_POS, fn, fp, tn, tp)

    base_tree_file.close()
   
    
# This method is used to print the evaluation file of the best decision tree
def print_best_model_output_file_2_classes(file_name_with_ext, best_guesses, evaluation_polarity_labels, split_point_index):
    best_tree_file = open(file_name_with_ext, "w")
    best_tree_file.write("Best Decision Tree Model\n")
    best_tree_file.write("\n")
    counterCheck = 0
    numCorrect = 0
    for i in best_guesses:
        
        if i == evaluation_polarity_labels[counterCheck]:
            numCorrect += 1
        counterCheck+=1
    
    
    y_true = evaluation_polarity_labels
    y_pred = best_guesses
    cm = confusion_matrix(y_true, y_pred, labels=["pos","neg"])
    
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["pos","neg"])
    disp.plot()
    
    scores = precision_recall_fscore_support(y_true,y_pred,average=None, labels=['pos','neg'])
    precision_POS = scores[0][0]
    precision_NEG = scores[0][1]
    recall_POS = scores[1][0]
    recall_NEG = scores[1][1]
    f1_measure_POS = scores[2][0]
    f1_measure_NEG = scores[2][1]
    
    
    tp = cm[0][0]
    fp = cm[0][1]
    fn = cm[1][0]
    tn = cm[1][1]
    
    accuracy = numCorrect/len(evaluation_polarity_labels)
  
    
    row = split_point_index
    for i in best_guesses:
        best_tree_file.write(str(row) + ", "+i+"\n")
        row+=1
        
    write_confusion_matrix_and_performance_measures(best_tree_file, accuracy, precision_NEG, recall_NEG, f1_measure_NEG, precision_POS, recall_POS, f1_measure_POS, fn, fp, tn, tp)    

    best_tree_file.close()
    
    
# This method is used to print to a file the confusion matrix, accuracy, precision, recall and f1-measure of a model
# Assumes the there is only 2 classes: NEG and POS
def print_evaluation_parameters_2_classes(output_file, evaluation_polarity_labels, classified_labels):
    counter = 0
    true_positive_count = 0
    true_negative_count = 0
    false_negative_count = 0
    false_positive_count = 0
    
    while(len(evaluation_polarity_labels) > counter):
        if (evaluation_polarity_labels[counter] == classified_labels[counter]) and classified_labels[counter] == "pos":
            true_positive_count += 1
        elif (evaluation_polarity_labels[counter] == classified_labels[counter]) and classified_labels[counter] == "neg":
            true_negative_count += 1
        elif (evaluation_polarity_labels[counter] != classified_labels[counter]) and classified_labels[counter] == "neg":
            false_negative_count += 1
        elif (evaluation_polarity_labels[counter] != classified_labels[counter]) and classified_labels[counter] == "pos":
            false_positive_count += 1
            
        counter += 1
    
    accuracy = (true_negative_count + true_positive_count) / (true_positive_count + true_negative_count + false_negative_count + false_positive_count)
    
    precision_NEG = true_negative_count / (true_negative_count + false_negative_count)
    recall_NEG = true_negative_count / (true_negative_count + false_positive_count)
    
    # bug found during demo. trying to divide by zero exception
    x1 = (precision_NEG + recall_NEG)
    if x1 == 0:
        f1_measure_NEG = 0;
    else:
        f1_measure_NEG = (2 * precision_NEG * recall_NEG) / (precision_NEG + recall_NEG)
    
    precision_POS = true_positive_count / (true_positive_count + false_positive_count)
    recall_POS = true_positive_count / (true_positive_count + false_negative_count)
    
    # bug found during demo. trying to divide by zero exception
    x2 = (precision_POS + recall_POS)
    if x2 == 0: 
        f1_measure_POS = 0;
    else:
        f1_measure_POS = (2 * precision_POS * recall_POS) / (precision_POS + recall_POS)
    
    write_confusion_matrix_and_performance_measures(output_file, accuracy, precision_NEG, recall_NEG, f1_measure_NEG, precision_POS, recall_POS, f1_measure_POS, false_negative_count, false_positive_count, true_negative_count, true_positive_count)
    
    output_file.close()
      
def write_confusion_matrix_and_performance_measures(output_file, accuracy, precision_NEG, recall_NEG, f1_measure_NEG, precision_POS, recall_POS, f1_measure_POS, false_negative_count, false_positive_count, true_negative_count, true_positive_count):
    
    output_file.write("\n")
    output_file.write("\n")
    output_file.write("Confusion Matrix\n")
    output_file.write("\n")
    output_file.write("_________________________\n")
    output_file.write("|TP: "+ str(true_positive_count)+ "|   FP: "+ str(false_positive_count)+" |\n")
    output_file.write("-----------------------------\n")
    output_file.write("|FN: "+ str(false_negative_count)+ "|   TN: "+ str(true_negative_count)+" |\n")
    output_file.write("-------------------------\n")
    output_file.write("\n")
    output_file.write("\n\n")
    output_file.write("Accuracy: " + str(round((accuracy * 100),2)) + "% \n")

    
    output_file.write("\n\n")
    output_file.write("Precision POS: " + str(round((precision_POS * 100),2)) + "% \n")
    output_file.write("Recall POS: " + str(round((recall_POS * 100),2)) + "% \n")
    output_file.write("F1 Measure POS: " + str(round((f1_measure_POS * 100),2)) + "% \n")
    
    output_file.write("\n")
    output_file.write("Precision NEG: " + str(round((precision_NEG * 100),2)) + "% \n")
    output_file.write("Recall NEG: " + str(round((recall_NEG * 100),2)) + "% \n")
    output_file.write("F1 Measure NEG: " + str(round((f1_measure_NEG * 100),2)) + "% \n")
    