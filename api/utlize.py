import torch


# Method to obtain an answer to a question from the provided context.
# Parameters: model (the model to be used for question answering),
#             tokenizer (the tokenizer for the model),
#             question (the question to be answered),
#             context (the text in which the answer can be found).
def QA(model, tokenizer, question, context):
    inputs, sentence_embedding = encoder(tokenizer, question, context)

    outputs = model(input_ids=inputs, token_type_ids=sentence_embedding)

    answer = getAnswer(outputs, inputs, tokenizer)

    print("Q:",question, "\nA:", answer, "\n")
    
    return answer

#The encoder of the input
def encoder(tokenizer, question, context):
    encoding = tokenizer(text=question, text_pair=context, return_tensors="pt")
    inputs = encoding['input_ids']  # Token embeddings
    sentence_embedding = encoding['token_type_ids']  # Segment embeddings

    question_tokens = tokenizer.tokenize(question)
    context_tokens = tokenizer.tokenize(context)

    print("Number of input Tokens:"
          " total=" + str(len(question_tokens) + len(context_tokens)) +
          " question=" + str(len(question_tokens)) +
          " context=" + str(len(context_tokens)))
    
    return inputs, sentence_embedding

#Extract the answer from the tensors
def getAnswer(outputs, input_ids, tokenizer):
    start_logits, end_logits = outputs[:2]

    answer_start_index = torch.argmax(start_logits)

    answer_end_index = torch.argmax(end_logits)

    predict_answer_tokens = input_ids[0, answer_start_index, answer_end_index + 1]

    answer = tokenizer.decode(predict_answer_tokens, skip_special_tokens=False)

    return answer