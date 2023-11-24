import os
import requests

# import env variables
from decouple import config

#import torch to use its multi-dim data strcuters (tensors)
from transformers import AutoModelForQuestionAnswering, AutoModelForCausalLM 
from transformers import AutoTokenizer #import BERT tokenizer
from .utlize import QA

def bert_large_service(context, question, model_name):
    try:
        model = AutoModelForQuestionAnswering.from_pretrained(model_name)

        # Init the model's Tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Test the QA function with the questions
        answer = QA(model, tokenizer, question, context)

        return answer
    except Exception as error:
        return f'Error: {error}'

def falcon_service(question, model_name, max_length):
    try:
        model = AutoModelForCausalLM.from_pretrained(model_name)

        tokenizer = AutoTokenizer.from_pretrained(model_name)

        inputs = tokenizer(question, return_tensors="pt")


        outputs = model.generate(**inputs, labels=inputs["input_ids"], max_length=max_length, pad_token_id=tokenizer.eos_token_id)


        # Decode the generated sequence
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return generated_text
    except Exception as error:
        return f'Error: {error}'
  

def bert_large_service_huggingFace_API(context, question, model_name):
    HUGGING_FACE_API_TOKEN = os.environ.get('HUGGING_FACE_API_TOKEN', config("HUGGING_FACE_API_TOKEN"))
    
    API_URL = "https://api-inference.huggingface.co/models/"+model_name
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
            "options":{
                "wait_for_model":True
            }
        })

        if(not output['answer']): 
            return "ERROR: No Answer"
        else: 
            return output['answer']
    except Exception as error:
        return f'Error: {output["error"]}'

