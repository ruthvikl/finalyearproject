# finalyearproject

## Title: AI Based Sentiment Analysis & Conversation Management System
Reviews are the integral part that helps an organization improve a certain product. Sentences in reviews are taken and analyzed for the full context and then, the ML Model predicts the sentiment of the review. This is Sentiment Analysis. 
In this project, we have built a Machine Learning Model to analyze a text, either extracted from audio or just as plain text and determine whether it is positive or negative with its rating.

The application was built using:
* Django for web application.
* HTML, CSS, JavaScript for frontend design and audio to text module respectively.
* TensorFlow for training and sentiment extraction.
* Model Used - small_bert/bert_en_uncased_L-4_H-512_A-8 (Smaller version of the BERT Model).
* You can download the model [here](https://drive.google.com/drive/folders/1VmrrjT0pPmisSJkU0_AtgT1V2bxGQBv2?usp=sharing).

To Run the Project follow the following commands:
```
git clone https://github.com/ruthvikl/finalyearproject.git
Download model_py folder from above link and paste it inside finalyearproject folder.
cd finalyearproject
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
