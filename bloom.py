import regex as re
import tensorflow as tf
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
from transformers import logging as hf_logging

hf_logging.set_verbosity_error()

# Blooms taxonomy categories
categories = ['Analyse', 'Apply', 'Create', 'Evaluate', 'Remember', 'Understand']
category_dict = {0: 'Analyse', 1: 'Apply', 2: 'Create', 3: 'Evaluate', 4: 'Remember', 5: 'Understand'}

# Change this directory as required to model file path
LOAD_DIRECTORY = 'BloomBERT_model'

# Load model
MODEL_TOKENIZER = DistilBertTokenizer.from_pretrained(LOAD_DIRECTORY)
LOADED_MODEL = TFDistilBertForSequenceClassification.from_pretrained(LOAD_DIRECTORY)


def predict_blooms(text):
    # process text input
    # remove numbers and punctuations
    processed = re.sub('[^a-zA-Z ]+', '', text)
    # remove spaces and lower case
    processed = (re.sub(' +', ' ', (processed.replace('\n', ' ')))).strip().lower()

    predict_input = MODEL_TOKENIZER.encode(processed,
                                           truncation=True,
                                           padding=True,
                                           return_tensors="tf")

    prediction = LOADED_MODEL(predict_input)

    # get probabilities
    probabilities = tf.nn.softmax(prediction.logits, axis=1).numpy()
    print("Probabilities:")
    print(dict(zip(categories, list(probabilities[0]))))

    # predicted category
    prediction_value = tf.argmax(prediction[0], axis=1).numpy()[0]

    return category_dict[prediction_value]


def main():
    print("\nHello! I'm BloomBERT.\nI will do my best to classify your tasks into Blooms Taxonomy.\n"
          "Enter '-1' to quit at any time.\n")

    while True:
        user_query = input("Enter Text: ")

        if user_query == '-1':
            break

        print("Prediction:", predict_blooms(user_query), "\n")


if __name__ == "__main__":
    main()
