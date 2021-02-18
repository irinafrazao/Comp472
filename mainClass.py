# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

#from sklearn.metrics import confusion_matrix

import utilClass as util

# TASK 0: Split data set in a training and an evaluation part (80/20)
dataset_filename_with_extension = "dataset1.txt"
all_polarity_labels, all_reviews = util.read_document(dataset_filename_with_extension)

split_point_index = int(0.80 * len(all_reviews))
training_reviews = all_reviews[:split_point_index]
training_polarity_labels = all_polarity_labels[:split_point_index]
evaluation_reviews = all_reviews[split_point_index:]
evaluation_polarity_labels = all_polarity_labels[split_point_index:]


# TASK 1: Plot the distribution of the number of the instances in each class (polarity label)
util.show_distribution_plot(all_polarity_labels, "Distribution of Complete Dataset (Training and Evaluation)")


# TASK 2: Run 3 different ML models, train them (Naive Bayes Classifier, Base-DT and Best-DT)

# Naive Bayes Classifier 
# Train the model
(prior, conditional) = util.train_naive_bayes_classifier(training_reviews, training_polarity_labels, 0.5)


# Base Decision Tree classifier
# training matrix generation + feature list
feature_existance_per_training_review_base, featureList_base = util.setup_training_feature_matrix_base_decision_tree(training_reviews, training_polarity_labels)
feature_existance_per_evaluation_review_base = util.setup_evaluation_feature_matrix_decision_tree(featureList_base, evaluation_reviews)


# Best decision tree classifier
# training matrix generation + feature list
feature_existance_per_training_review_best, featureList_best = util.setup_training_feature_matrix_best_decision_tree(training_reviews, training_polarity_labels)
feature_existance_per_evaluation_review_best = util.setup_evaluation_feature_matrix_decision_tree(featureList_best, evaluation_reviews)


# TASK 3 : Generate output file with classification and performance evaluation

# Naive Bayes Classifier 
util.print_NB_model_output_file_2_classes("NB-" + dataset_filename_with_extension, split_point_index, evaluation_reviews, evaluation_polarity_labels, prior, conditional)

# Base Decision Tree classifier
base_guesses = util.classify_decision_tree(feature_existance_per_training_review_base, feature_existance_per_evaluation_review_base, training_polarity_labels)
util.print_base_model_output_file_2_classes("Base_Tree-" + dataset_filename_with_extension, base_guesses, evaluation_polarity_labels, split_point_index)

# Best decision tree classifier
best_guesses = util.classify_decision_tree(feature_existance_per_training_review_best, feature_existance_per_evaluation_review_best, training_polarity_labels)
util.print_best_model_output_file_2_classes("Best_Tree-" + dataset_filename_with_extension, best_guesses, evaluation_polarity_labels, split_point_index)