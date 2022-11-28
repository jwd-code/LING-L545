# Suicidal Ideation Detection in Italian Tweets

Progress:
- Created the script/pipeline to scrape Tweets from Twitter API
- Collected list of phrases/keywords to use as queries for the API
- Contacted Italian mental health professional/doctor to double check the list of phrases
- Collected over 1000 Tweets by using the keyword phrase list evaluated by the Italian mental health professional

To Do:
- Development criteria to annotate Tweets as either 'suicidal' or 'not-suicidal'
- Annotate Tweets
- Create models







Description of the project:

According to the World Health Organization (2022), there is an estimated number of 700,000 deaths by suicide each year. As people tend to use social media to express their thoughts and feelings in real time, some online posts can include content related to depression, suicide, and self-harm. The aim of this project is to develop a machine learning classifier to detect suicidal ideation in Tweets in Italian, a language for which, to my current knowledge, no suicidal ideation detectors have been created. This has potential use cases as being implemented into social media platforms to allow for suicide prevention or intervention.  

The data collection process includes carefully curating a list of keyword phrases that are often used in the expression of depression or suicidal ideation, and then inputting these phrases into a Twitter scraper that I have already created to automatically download, preprocess and store tweets that contain these phrases. These phrases will be created by translating the most common phrases used to express depression or suicidal ideation in English and other romance languages. Ideally, these phrases will be double checked by Italian domain specialist to ensure that they are accurate representations of how native speakers would express suicidal ideation. Examples of such phrases in English would be: “kill myself”, “I hate my life”, “ready to die”, “don’t want to exist” etc. (Valdez 2020). 

After the data collection has been completed, the data will be manually annotated as either “suicidal” or “not suicidal.” A concrete set of criteria for the data annotation has not yet been established for this project. In the literature, some studies (Diniz et al. 2022) have had psychologists annotate their data, while others (Valdez 2020) indicate that non-suicide criteria would include no evidence of suicidal ideation but also include sarcasm, news, song parts, etc. Some examples of non-suicidal sentences that contain suicidal keywords but would not indicate suicidal ideation are the following: “one day without drinking coca-cola, I don’t want to live” or “my life without headphones is meaningless” (Valdez 2020). Upon completion of the annotation process, the data will be preprocessed by removing stop words, URLs, punctuation, emojis, and links. The features that will be extracted from the preprocessed data are the term frequency-inverse document frequency and bigrams. The classification model of choice for this project will be a Support Vector Machine (SVM). The model will be evaluated by examining the standard metrics of evaluation for classification algorithms: precision, recall, F1 score, and accuracy.  

 

 

 

Bibliography 

Aldhyani, T. H., Alsubari, S. N., Alshebami, A. S., Alkahtani, H., & Ahmed, Z. A. (2022). Detecting and analyzing suicidal ideation on social media using deep learning and machine learning models. International journal of environmental research and public health, 19(19), 12635. 

Beriwal, M., & Agrawal, S. (2021). Techniques for Suicidal Ideation Prediction: a Qualitative Systematic Review. In 2021 International Conference on INnovations in Intelligent SysTems and Applications (INISTA) (pp. 1-8). IEEE. 

Diniz, E. J., Fontenele, J. E., de Oliveira, A. C., Bastos, V. H., Teixeira, S., Rabêlo, R. L., ... & Teles, A. S. (2022). Boamente: A Natural Language Processing-Based Digital Phenotyping Tool for Smart Monitoring of Suicidal Ideation. In Healthcare (Vol. 10, No. 4, p. 698). MDPI. 

Huang, X., Zhang, L., Chiu, D., Liu, T., Li, X., & Zhu, T. (2014, December). Detecting suicidal ideation in Chinese microblogs with psychological lexicons. In 2014 IEEE 11th Intl Conf on Ubiquitous Intelligence and Computing and 2014 IEEE 11th Intl Conf on Autonomic and Trusted Computing and 2014 IEEE 14th Intl Conf on Scalable Computing and Communications and Its Associated Workshops (pp. 844-849). IEEE. 

Ji, S., Pan, S., Li, X., Cambria, E., Long, G., & Huang, Z. (2020). Suicidal ideation detection: A review of machine learning methods and applications. IEEE Transactions on Computational Social Systems, 8(1), 214-226. 

Navarro Alvarado, P. E. (2021). Diseño de un prototipo de aprendizaje automático que clasifique comportamientos tendientes al suicidio en Twitter, en un contexto Latinoamericano. Pontificia Universidad Javeriana. 

Valeriano Valdez, Kid & Condori-Larico, Alexia & Sulla-Torres, Jose. (2020). Detection of Suicidal Intent in Spanish Language Social Networks using Machine Learning. International Journal of Advanced Computer Science and Applications. 11. 10.14569/IJACSA.2020.0110489. 

World Health Organization. (‎2022)‎. World health statistics 2022: monitoring health for the SDGs, sustainable development goals. World Health Organization. https://apps.who.int/iris/handle/10665/356584. License: CC BY-NC-SA 3.0 IGO 

Yeskuatov E, Chua S-L, Foo LK. (2022). Leveraging Reddit for Suicidal Ideation Detection: A Review of Machine Learning and Natural Language Processing Techniques. International Journal of Environmental Research and Public Health. 19(16):10347. https://doi.org/10.3390/ijerph191610347 
