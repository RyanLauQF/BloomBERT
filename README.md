# BloomBERT

_BloomBERT_ is a transformer-based NLP task classifier based on the [revised edition of Bloom's Taxonomy](https://en.wikipedia.org/wiki/Bloom%27s_taxonomy). 

Bloom's Taxonomy is a set of hierarchical models used in classifying learning outcomes into levels of complexity and specificity. Although the taxonomy is mostly employed by educators for curriculum and assessment structuring, _BloomBERT_ takes a novel approach in differentiating the difficulty of a task through `classifying productivity related tasks` into the cognitive domain of the taxonomy.

> BloomBERT can be accessed via an API endpoint or a [web application](bloombert.herokuapp.com)

#### Example Outputs:

| Task Description                                                | BloomBERT Classification |
|-----------------------------------------------------------------|--------------------------|
| Programming an automated solution                               | Create                   |
| Preparing for the presentation of findings from market research | Apply                    |
| Reviewing performance metrics for this quarter                  | Evaluate                 |

#### Bloom's Taxonomy:
![Bloom's Taxonomy](images/Revised_Blooms_Taxonomy.png)

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

Developed using [Streamlit](https://streamlit.io/) with Python and hosted on Heroku servers through GitHub. Frontend repository is available [here](https://github.com/RyanLauQF/bloombert-frontend).

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

> The API endpoints are currently deployed on Google Cloud. Note some time may be required for the instance to start up.

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

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Source codes for model development are available under the MIT License. Developed by [Ryan Lau Q. F.](https://github.com/RyanLauQF)

