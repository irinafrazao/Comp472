# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370


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


# TASK 2: Run 3 different ML models (Naive Bayes Classifier, Base-DT and Best-DT)

# Naive Bayes Classifier 
# Train the model
(prior, conditional) = util.train_naive_bayes_classifier(training_reviews, training_polarity_labels, 0.5)

# TODO: ADD BASE-DT AND BEST-DT


# TASK 3 : Generate output file with classification and performance evaluation

# Naive Bayes Classifier 
# Evaluate samples and performance of model
util.print_NB_model_output_file_2_classes("NB-" + dataset_filename_with_extension, split_point_index, evaluation_reviews,
                                        evaluation_polarity_labels, prior, conditional)

# TODO: ADD BASE-DT AND BEST-DT (reuse print_evaluation_parameters method)