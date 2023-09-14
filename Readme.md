# Document embedding and semantic search retrieval

<div style="text-align: justify">
This is a simple document embedding project which demonstrates how to utilise a Huggingface pre-trained model and use 
it to retrieve the documents back. As of writing this software, BAAI's (Zhiyuan Institute) BGE is a very good text
embedding tool.

To run this project, you have to first install the requirements. I highly recommend creating a new virtual environment.

To create a new virtual environment:

```commandline
python -m venv my_virtual_env
```

Activate the environment
```commandline
source ./my_virtual_env/bin/activate
```

Install the requirements:
```commandline
pip install -r requirements.txt
```
I am using Python 3.10. Please use this for maximum compatibility.

To add documents to the vectorDB:
```commandline
python make_knowledge_DB.py --dir "<directory with pdf books>" 
```

To enquire or retrieve information from the database:
```commandline
python get_data_from_database.py
```

Ask questions to retrieve documents semantically related to your question.
Or enter `q` to quit.

</div>