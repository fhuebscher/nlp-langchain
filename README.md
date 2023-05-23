# LangChain based Chatbot
Using [LangChain](https://github.com/hwchase17/langchain/) for developing applications powered by language models.

Our proposed project is a ChatBot that enables faster information retrieval in the University of Technology, Sydney's website.
The model leverages only opensource resources (Alpaca 7B + TensorFlow Embedder) and attains impressive results (demo provides some examples about the Master of Data Science webpage).  

### The repository contains:
  - `langchainindexing.ipynb`, which is the main script that implements the ChatBot;
  - `uts_scraper.py`, which is the script that we used to scrape all corpus data from the **entire** UTS website (unused due to computational constraints);
  - `p_text.txt`, which is the output txt file from the above scraper;
  - `ScrapeTextFromUTS.ipynb`, which is the script we used to scrape corpus data from the **MDSI** webpage specifically;
  - `DSMaster.txt`, which is the corpus data scraped from the MDSI webpage and fed into the main script;
  - `assignment3.pdf`, which is the report for the given task.

## External content:
- [Github repository with all the files involved](https://github.com/fhuebscher/nlp-langchain)
- [Ppt of the presentation displayed on May, 15th](https://studentutsedu-my.sharepoint.com/:p:/g/personal/joan_velja_student_uts_edu_au/EQA46W6rGNhBh2qPYu4Gd9YB0cxJ5RpolxwMmSqZ40-K0A?e=BJFVdK)
- [Google Colab document](https://colab.research.google.com/drive/1P1vZn4dKZrM-trgRUrWfopbUmu5Z36BN?usp=sharing)

## For further clarification, please send an email to:
  - Till Schirrmeister (till.schirrmeister@student.uts.edu.au);
  - Joan Velja (joan.velja@student.uts.edu.au);
  - Florian Hübscher (florian.huebscher@student.uts.edu.au);
  - Joshua Banga (joshua.banga@student.uts.edu.au).
