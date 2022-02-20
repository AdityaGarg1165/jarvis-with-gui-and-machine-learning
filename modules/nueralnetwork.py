import os
from pathlib import Path
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn
import tensorflow
import json
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
data = ""

BASE_DIR = Path(__file__).parent.parent


with open(os.path.join(BASE_DIR,"files\intents.json")) as file:
    data = json.load(file)


# try:
#     with open("data.pickle", "rb") as f:
#         words, labels, training, output = pickle.load(f)

words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)


training = numpy.array(training)
output = numpy.array(output)

# with open("data.pickle", "wb") as f:
#     pickle.dump((words, labels, training, output), f)

tensorflow.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

def train(epochs):
    model.fit(training, output, n_epoch=epochs, batch_size=8, show_metric=True)
    model.save(os.path.join(BASE_DIR,"model\model.pth"))


def bag_of_words(inp, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(inp)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)


