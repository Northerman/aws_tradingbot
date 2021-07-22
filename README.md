# AWS Trading Bot using Alpaca API: Project Overview
* Scraped around 10,000 job postings from jobsdb using python and BeautifulSoup. :  [Data Scraping Notebook](https://colab.research.google.com/drive/1CxPKttPc71m3fAs-ZbRyHzjzmzwEeQ-_?usp=sharing)
* Perform multiple text data cleaning such as salary & working experience extraction from text using regex. 
* Perform exploratory data analysis to gain insights for jobs using plotly & seaborn. : [Data Cleaning & EDA Notebook](https://colab.research.google.com/drive/1Ipjt0Be_ZJM1BhYPNchVwGvKjPOqco4V?usp=sharing)
* Create a tree-based model to predict job salary given experience year & job function.
* Built two salary prediction chatbot & models. (1.Using local database 2.Using Firebase)
* Built a flask API endpoint hosted locally and use ngrok to communicate with dialogflow to identify user’s intent.
![](/trade_bot.jpg)
# Code and Resources Used
**Base requirements:** requirements.txt

**Packages used for EDA:** Plotly,matplotlib,seaborn,statistics,wordcloud

**Packages used for data scraping:** bs4,requests, time

**ngrok:** https://ngrok.com/download

**Flask Tutorial:** https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH (By Corey Schafer)

**Python Chatbot Tutorial:** https://www.youtube.com/watch?v=UVKSrj7cxak (By Professional Cipher)


# Webpage Structure
The webpage contain 2 chatbots, one from python and the other from dialogflow. The python chatbot contains training data from jobsdb while dialogflow chatbot training data comes from user input. Pictures below show what can the chatbot do!

**Idle Chat & Salary Prediction**
![](/images/idle_chat.png)


**Showing Data**
![](/images/show_data.png)

**Insert Data**
![](/images/insert_data.png)

# Web Scraping [Data Scraping Notebook](https://colab.research.google.com/drive/1CxPKttPc71m3fAs-ZbRyHzjzmzwEeQ-_?usp=sharing)
Wrote a jupyter notebook scraping data from jobsdb using BeautifulSoup. For each job posting we got the following data: 
* Job Title	
* Job Category
* Career Level	
* Years of Experience
* Salary
* Employment type
* Job Responsibility
* Job Qualifications
* Job Description




# Data Cleaning [Data Cleaning & EDA Notebook](https://colab.research.google.com/drive/1Ipjt0Be_ZJM1BhYPNchVwGvKjPOqco4V?usp=sharing)
* Using regex to extract salary & expereince year from text (e.g. THB70,000 - 120,000 /month --> min salary = 70,000 & max salary = 120,000)
* Using multiple preprocessing steps to extract salary from job description or job title (more details on the extraction method can be found in the notebook [Data Cleaning & EDA Notebook](https://colab.research.google.com/drive/1Ipjt0Be_ZJM1BhYPNchVwGvKjPOqco4V?usp=sharing))
* Clean redundant data e.g. (Middle, Middle Level) = Middle Level
* Fill missing experience year by grouped by career level
* and more!


# Exploratory Data Analysis
Here are some of the highlights of the EDA notebook
![](/images/pie_chart.png)  
![](/images/wordcloud.png)  
![](/images/salary_experience.png) 
![](/images/salary_jobfunction.png)



# Modelling
* The purpose of this project is to understand the data science project pipeline, and thus modelling is not emphasized in this particular project.
* Two model has been created based on 2 data location one in local databaase and the other in firebase. The local database contains data scraped from jobsdb and the firebase database contains user input data inserted through dialogflow chatbot.
* A simple decision tree model is used to train on the whole dataset and the categorical feature (job function) is label encoded.
 
# Model Deployment
* After the model is trained it is pickle saved into a .pkl file which will be loaded when running flask endpoint hosted locally.
* Used ngrok to deploy the web online so that it can communicate with dialogflow through webhook.
* The chatbot can idle chat/insert data/show data/predict salary based on user's intent.
* Why 2 chatbots? : So that I could connect to 2 database types (SQL & NOSQL) for practicing purposes.

