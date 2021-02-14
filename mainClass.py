# Team Members:
# Zach Eichler 40018021
# Irina Patrocinio-Frazao 40024714
# Emilie Mines 40045370

from sklearn import tree
from codecs import open
from collections import Counter

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


#Decision Tree classifier

pos = Counter()
neg = Counter()
total = Counter()
labelCount = 0

for doc in training_reviews:
    if training_polarity_labels[labelCount] == "pos":
        for w in doc:
            pos[w] += 1
    else:
        for w in doc:
            neg[w] += 1
    labelCount+=1


for doc in training_polarity_labels:
    for w in doc:
        total[w] +=1
        
        
#print(labelCount)
        
   
        
#create dictinonary with all words in positive reviews paired with the abs value of the difference in of appearances in negative reviews
#do it for both the positive and negative reviews as some words may appear in one but not the other


pos_difference_dict ={}
neg_difference_dict ={}

for word in pos:
    difference = abs(pos[word] - neg[word])
    pos_difference_dict[word] = abs(difference)

for word in neg:
    difference = abs(neg[word] - pos[word])
    neg_difference_dict[word] = abs(difference)





#combine dictionaries, removing duplicates with every word and the difference difference in frequency between positive and negative
pos_difference_dict.update(neg_difference_dict)

#sort the dictionary


sorted_dict = sorted(pos_difference_dict.items(), key=lambda x: x[1])



#using sorted data, pick words with highest values, excluding words like "and", "the", etc...

#Choosing 10 words

# "not" -> 1829, 
# "n't" -> 1305, 
# "great" -> 1184
# "no" -> 603
# "best" -> 600
# "love" -> 544
# "easy" -> 501


featureCounter = 0
featureMax = 100
featureList = []


#adding 100 words with largest difference in frequency excluding words like "and" "is" ....
#try stopwords after
for i in reversed(sorted_dict):
    if (i[0] != "and" 
        and i[0] != "i" 
        and i[0] != "the" 
        and i[0] != "is" 
        and i[0] != "a" 
        and i[0] != ','
        and i[0] != "to" 
        and i[0] != '.' 
        and i[0] != '(' 
        and i[0] != ')' 
        and i[0] != "it"
        and i[0] != "as" 
        and i[0] != "or" 
        and i[0] != '"'
        and i[0] != "his"
        and i[0] != ';'
        ):
        featureList.append(i[0])
        featureCounter += 1
    if featureCounter == featureMax: break
  


#Make 2D array with data from training set with flags representing the presence of each of the chosen words
X = []

for i in training_reviews:
    row = []
    for j in featureList:
        if j in i:
            row.append(1)
        else:
            row.append(0)
    X.append(row)   
    

#array with classifiers

Y = []

print(len(featureList))

for i in training_polarity_labels:
    Y.append(i)

X2 =[]
for i in evaluation_reviews:
    row = []
    for j in featureList:
        if j in i:
            row.append(1)
        else:
            row.append(0)
    X2.append(row)
    




clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X,Y)
guesses = clf.predict(X2)


counterCheck = 0
numCorrect = 0
for i in guesses:
    if i == evaluation_polarity_labels[counterCheck]:
        numCorrect += 1
    counterCheck+=1
    
print("correct: ", numCorrect)
print("total: ", len(evaluation_polarity_labels))
print("score: ", numCorrect/len(evaluation_polarity_labels))










# TODO: ADD BASE-DT AND BEST-DT


# TASK 3 : Generate output file with classification and performance evaluation

# Naive Bayes Classifier 
# Evaluate samples and performance of model
util.print_NB_model_output_file_2_classes("NB-" + dataset_filename_with_extension, split_point_index, evaluation_reviews,
                                        evaluation_polarity_labels, prior, conditional)

# TODO: ADD BASE-DT AND BEST-DT (reuse print_evaluation_parameters method)