# Information Extraction

To build an RDF, we extract useful data from the soccer news. We extract 
two entity "Player" and "Team". This will establish the relationship like
 
"News" mentions "Player" 

or 

"News" mentions "Team".

More sophisciated relation extraction is under development. 

**soccer_ner.crfsuite**
This is pre-trained CRF model. We train this model with 100 soccer news with manually annotated using [CRFsuite](https://github.com/scrapinghub/python-crfsuite). 

**ner.py**

This code reads the json files containing soocer news obtained from wrapper (in data collection section) 
and extract name of the team and player from news title. This codes requires pre-trained model, dictionary of soocer player names and soocer teams.
The output is json files with extracted soccer players and soccer teams related to soccer news.

**crf_util.py**

This code includes utility function used for ner.py. It is developed by [this](https://github.com/scrapinghub/python-crfsuite).