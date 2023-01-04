# BloomBERT: A Task Complexity Classifier

BloomBERT is a transformer-based NLP task classifier based on the [revised edition of Bloom's Taxonomy](https://en.wikipedia.org/wiki/Bloom%27s_taxonomy). 

Bloom's Taxonomy is a set of hierarchical models used in classifying learning outcomes into levels of complexity and specificity. Although mostly employed by educators for curriculum and assessment structuring, BloomBERT takes a novel approach in differentiating the difficulty of a task through `classifying productivity related tasks` into the cognitive domain of the taxonomy.

> BloomBERT can be accessed via an API endpoint or a [web application](bloombert.herokuapp.com)

#### Example Outputs:

| Task Description                                                | BloomBERT Classification |
|-----------------------------------------------------------------|--------------------------|
| Programming an automated solution                               | Create                   |
| Preparing for the presentation of findings from market research | Apply                    |
| Reviewing performance metrics for this quarter                  | Evaluate                 |

#### Bloom's Taxonomy:
<img src="images/Revised_Blooms_Taxonomy.png" width="650">

###### Description of Bloom's Taxonomy Levels [^1]
[^1]: [Bloom's Taxonomy Graphic](https://citt.ufl.edu/resources/the-learning-process/designing-the-learning-experience/blooms-taxonomy/blooms-taxonomy-graphic-description/)

## Model Overview

BloomBERT was built by fine-tuning a [DistilBERT](https://arxiv.org/abs/1910.01108) model, a lighter version of the original BERT transformer language model
developed by Google. It was developed using `Tensorflow` and the `Hugging Face Transformers library`, 
incorporating a sequence classification head (linear layer) on top of the DistilBERT pooled outputs.
Utilising the pre-trained DistilBERT model, BloomBERT was trained with a labelled data set curated for the specific task classification on `Google Colab`.


#### Training Data Distribution:
| Bloom's Level | Count |
|---------------|-------|
| Create        | 430   |
| Evaluate      | 634   |
| Analyse       | 560   |
| Apply         | 671   |
| Understand    | 2348  |
| Remember      | 1532  |
| Total         | 6175  |

```text
Training Results:
    EPOCH: 40 
    training accuracy: 0.9820
    validation accuracy: 0.9109
```

## Deployment Architecture

### Overview:
![BloomBERT Deployment Architecture](images/Deployment_Architecture.jpg)


### Frontend:

<img align="left" width="35px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/heroku/heroku-original.svg" style="padding-right:10px;" />
<img align="left" width="35px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" style="padding-right:10px;" />
<img align="left" width="35px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original-wordmark.svg" style="padding-right:10px;" />

<br />
<br />

Developed using [Streamlit](https://streamlit.io/) with Python and hosted on Heroku servers through GitHub. <br> Frontend repository is available [here](https://github.com/RyanLauQF/bloombert-frontend).

### Backend:

<img align="left" width="35px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" style="padding-right:10px;" />
<img align="left" width="35px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-plain.svg" style="padding-right:10px;" />
<img align="left" width="35px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" style="padding-right:10px;" />
<img align="left" width="35px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" style="padding-right:10px;" />
<img align="left" width="35px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" style="padding-right:10px;" />
<img align="left" width="35px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" style="padding-right:10px;" />

<br />
<br />

Developed using Python to implement FastAPI endpoints. Model was trained using Jupyter Notebook and Tensorflow libraries. Docker used to containerise the application for deployment onto Google Cloud Run.

## FastAPI Endpoints

> The API endpoints are currently deployed on Google Cloud.<br>Note some time may be required for the instance to start up.

#### Request:
`GET` https://bloom-bert-api-dmkyqqzsta-as.a.run.app

#### Response:
```json
{
  "health_check": "OK", 
  "model_version": "1.0"
}
```

#### Request:
`POST` https://bloom-bert-api-dmkyqqzsta-as.a.run.app/predict
```json
{
  "text": "Annotating key points in meeting minutes"
}
```

#### Response:
```json
{
  "blooms_level": "Understand",
  "probabilities": {
    "Analyse": 0.00078,
    "Apply": 0.00075,
    "Create": 0.00054,
    "Evaluate": 0.00051,
    "Remember": 0.00261,
    "Understand": 0.99481
    }
}
```

## Development Journey

- [ ] Naive-Bayes (TF-IDF Vectorizer)
- [ ] Naive-Bayes (TF-IDF Vectorizer + SMOTE)
- [ ] SVC (TF-IDF Vectorizer)
- [ ] SVC (TF-IDF Vectorizer + SMOTE)
- [ ] SVC (word2vec, spaCy)
- [X] DistilBERT Transformer model

### Model Performance Comparison:

| Model                    | NB (TF) | NB (TF+SM) | SVC (TF) | SVC (TF+SM) | SVC (w2v+sp) | DistilBERT | 
|--------------------------|:-------:|:----------:|:--------:|:-----------:|:------------:|:----------:|
| Validation <br> Accuracy | 0.77328 |  0.81538   | 0.86721  |   0.88421   |   0.81296    |  0.91090   |

### 1. Naive-Bayes (TF-IDF Vectorizer)
* Starting with the Naive-Bayes algorithm that is often employed for multiclass classification problems, 
this model was used as a performance benchmark against other models.
```text
Validation Accuracy: 0.77328
```

### 2. Naive-Bayes (TF-IDF Vectorizer + SMOTE)
* After observing the presence of data imbalance, Synthetic Minority Oversampling Technique (SMOTE) was implemented
in attempts to oversample minority data points to create a balanced dataset and achieve better classification results.
* Using SMOTE successfully improved classification accuracy of the Naive-Bayes Model
```text
Validation Accuracy: 0.81538
```

### 3. SVC (TF-IDF Vectorizer)
* To improve model accuracy, I looked into using a Linear Support Vector Classifier (SVC) for the multi-classification problem.
* SVCs were determined to outperform Naive-Bayes in this specific classification problem with a much higher validation accuracy observed. 
* However, the model still fails to generalise well when given inputs of similar semantics.
```text
Validation Accuracy: 0.86721
```

### 4. SVC (TF-IDF Vectorizer + SMOTE)
* Applying SMOTE to this model showed slight improvements in classification accuracy.
* However, it still suffers from the same problems as the above few models.
```text
Validation Accuracy: 0.88421
```


### 5. SVC (word2vec, spaCy)
* To address the problem, I looked into using word2vec (word2vec-google-news-300) in replacement of TF-IDF Vectorizers to extract semantic relations from words within the sentences.
* This model uses spaCy models to tokenise the inputs before feeding the tokens into the word2vec model.
* Each word vector generated from the tokens are then averaged to form a sentence vector input for the SVC model.
* Unexpectedly, there was a significant drop in accuracy compare to the previous model using TF-IDF.
```text
Validation Accuracy: 0.81296
```

### 6. DistilBERT Transformer model
* After doing more research, I approached the problem from another angle using deep learning.
* Transformer models had demonstrated significant improvements over traditional NLP systems, excelling in processing sequential data and understanding language semantics.
* DistilBERT was chosen as the transformer model of choice due to its smaller size and greater speed compared to the original BERT model.
* The pre-trained model was then fine-tuned using the data set that I had developed using the taxonomy.
* It achieved the best accuracy compared to previous models and generalised well to unseen data with similar semantics, providing satisfactory predictions that fit within the taxonomy.
* This was the model chosen for `BloomBERT`. 
```text
Validation Accuracy: 0.91090
```


## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Source codes for model development are available under the MIT License. Developed by [Ryan Lau Q. F.](https://github.com/RyanLauQF)

