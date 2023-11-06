import torch


# Method to obtain an answer to a question from the provided context.
# Parameters: model (the model to be used for question answering),
#             tokenizer (the tokenizer for the model),
#             question (the question to be answered),
#             context (the text in which the answer can be found).
def QA(model, tokenizer, question, context):
    inputs, sentence_embedding, tokens = encoder(tokenizer, question, context)

    outputs = model(input_ids=torch.tensor([inputs]), token_type_ids=torch.tensor([sentence_embedding]))

    answer = getAnswer(outputs, tokens)

    print("Q:",question, "\nA:", answer, "\n")
    
    return answer


#The encoder of the input
def encoder(tokenizer, question, context):
    encoding = tokenizer.encode_plus(text=question,text_pair=context)
    inputs = encoding['input_ids']  #Token embeddings
    sentence_embedding = encoding['token_type_ids']  #Segment embeddings
    tokens = tokenizer.convert_ids_to_tokens(inputs) #input tokens

    return inputs, sentence_embedding, tokens

#Extract the answer from the tensors
def getAnswer(outputs, tokens):
    start_scores, end_scores = outputs[:2]

    start_index = torch.argmax(start_scores)

    end_index = torch.argmax(end_scores)

    answer = ' '.join(tokens[start_index:end_index+1])

    return answer