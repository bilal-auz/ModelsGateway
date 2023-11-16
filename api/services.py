import os
import requests

# import env variables
from decouple import config

#import torch to use its multi-dim data strcuters (tensors)
from transformers import BertForQuestionAnswering #import pre-trained BERT QA model
from transformers import BertTokenizer #import BERT tokenizer
from .utlize import QA

def bert_large_service(context, question):
    #Init the Model: bert-large-uncased-whole-word-masking-finetuned-squad
    model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

    #Init thee model's Tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

    # Test the QA function with the questions
    answer = QA(model, tokenizer, question, context)

    return answer

def bert_large_service_huggingFace_API(context, question):
    HUGGING_FACE_API_TOKEN = os.environ.get('HUGGING_FACE_API_TOKEN', config("HUGGING_FACE_API_TOKEN"))
    
    API_URL = "https://api-inference.huggingface.co/models/bert-large-uncased-whole-word-masking-finetuned-squad"
    headers = {"Authorization": f'Bearer {HUGGING_FACE_API_TOKEN}'}

    try:
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
    
        output = query({
            "inputs": {
                "question": question,
                "context": context
            },
        })

        if(not output['answer']): 
            return "ERROR: No Answer"
        else: 
            return output['answer']
    except Exception as error:
        return f'Error: {output["error"]}'

