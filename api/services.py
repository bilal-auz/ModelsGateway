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
