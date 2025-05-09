# Aspect-Based Sentiment Analysis for MOOC Reviews

## Overview
This repository contains the implementation of an **Aspect-Based Sentiment Analysis (ABSA)** system for analyzing reviews of Massive Open Online Courses (MOOCs). Developed as part of the **CS4082 Machine Learning** course under the supervision of **Dr. Naila Marir**, this project aims to extract and classify sentiments related to specific aspects of MOOCs using a dataset of 1.45 million Coursera reviews. The system leverages traditional machine learning models (e.g., Logistic Regression, SVM, Decision Tree) and natural language processing (NLP) techniques, with results visualized through an interactive **Streamlit dashboard**.

## Features
- **Data Preprocessing**: Cleaning, tokenization, and lemmatization of review text using SpaCy.
- **Aspect Extraction**: Identification of key themes using Dependency Parsing, RAKE, and Word2Vec.
- **Sentiment Classification**: Rule-based (TextBlob) and supervised classification (Logistic Regression, SVM, BERT, etc.).
- **Visualization**: Interactive Streamlit dashboard featuring aspect filters, pie charts, bar charts, and sample comments.
- **Model Performance**: High accuracy (Decision Tree: 94.28%, F1-Score: 94.40%) and AUC-ROC (Logistic Regression: 98.45%).

## Dataset
The project utilizes a publicly available dataset of **1.45 million Coursera course reviews**, containing:
- **Reviews**: Textual feedback from learners.
- **Reviewers**: Names of reviewers.
- **Date_reviews**: Submission dates of reviews.
- **Rating**: Numeric ratings provided by reviewers.
- **Course_id**: Unique identifiers for courses.


## Repository Structure
```
├── data/
│   └── Coursera_Reviews.csv    # Link to Dataset
├── src/
│   ├── preprocessing.py        # Data cleaning and preprocessing script
│   ├── aspect_extraction.py    # Aspect extraction using SpaCy, RAKE, Word2Vec
│   ├── sentiment_analysis.py   # Sentiment classification (rule-based and supervised)
│   └── dashboard.py            # Streamlit dashboard implementation
├
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── LICENSE                     # License file

```

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/mooc-absa.git
    cd mooc-absa
    ```

2. **Create a Virtual Environment and Install Dependencies**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Prepare the Dataset**:  
    Ensure `cleaned_reviews.csv` is placed in the `data/` directory.

---

## Usage

Run the following commands to use the system:

1. **Preprocess the Data**  
   Clean and prepare the dataset:

    ```bash
    python src/preprocessing.py
    ```

2. **Extract Aspects**  
   Identify key aspects from the reviews:

    ```bash
    python src/aspect_extraction.py
    ```

3. **Perform Sentiment Analysis**  
   Classify sentiments for extracted aspects:

    ```bash
    python src/sentiment_analysis.py
    ```

4. **Launch the Streamlit Dashboard**  
   Visualize results interactively:

    ```bash
    streamlit run src/dashboard.py
    ```

   The dashboard provides:
   - Aspect filtering.
   - Sentiment distribution (pie chart).
   - Aspect frequency (bar chart).
   - Sample comments for each sentiment category.

## Model Performance
The table below summarizes the performance of the evaluated models:

| Model                 | Accuracy (%) | F1-Score (%) | AUC-ROC (%) |
|-----------------------|--------------|--------------|-------------|
| Decision Tree         | 94.28        | 94.40        | 93.22       |
| Logistic Regression   | 92.47        | 92.90        | 98.45       |
| SVM                   | 91.91        | 92.30        | N/A         |
| Naive Bayes           | 80.24        | 83.12        | 93.04       |
| Linear Discriminant   | 70.63        | 75.20        | 85.40       |
| Quadratic Discriminant| 48.07        | 60.05        | 69.53       |

## Requirements
- **Python**: 3.8 or higher
- **Key Libraries**: `spacy`, `textblob`, `sklearn`, `gensim`, `streamlit`, `pandas`, `numpy`, `matplotlib`, `transformers`
- Full list available in `requirements.txt`

## Future Work
- Integrate live feedback processing for real-time analysis.
- Utilize contextual embeddings (e.g., BERT) for enhanced feature extraction.
- Expand dashboard with additional interactive visualizations.
- Support non-English reviews for broader applicability.

## Limitations
- High computational cost due to the large dataset.
- Potential bias in reviews (e.g., skewed toward strongly positive/negative sentiments).
- Limited to English reviews, reducing generalizability.

## Contributors
- **Araa Almarhabi** (S20106395)
- **Albatool Moathen** (S21107416)
- **Howyna Ahmed** (S20106603)
- **Fahad Dubush** (S22107768)

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
We express gratitude to **Dr. Naila Marir** for her guidance and the **Coursera platform** for providing the dataset used in this project.
