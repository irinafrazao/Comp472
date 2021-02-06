# Team Members:
# PLEASE ADD NAME AND ID
# Irina Patrocinio-Frazao 40024714
# PLEASE ADD NAME AND ID

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

# TASK 1: Plot the distribution of the number of the instances in each class

