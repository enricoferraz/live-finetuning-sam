import json
import re

def transform_to_fine_tune_format(conversation):
    messages = []
    
    # Using regular expressions to identify Theodore's and Samantha's parts
    parts = re.split(r'(Theodore:|Samantha:)', conversation)
    
    # Iterating through the parts and pairing them into user (Theodore) and assistant (Samantha) messages
    current_role = None
    current_content = ""
    
    for i in range(1, len(parts), 2):
        role = parts[i].strip()
        content = parts[i+1].strip()

        if role == "Theodore:":
            messages.append({"role": "user", "content": content})
        elif role == "Samantha:":
            messages.append({"role": "assistant", "content": content})
    
     # Check if the last message is from the user, if so, remove it
    if messages and messages[-1]["role"] == "user":
        messages.pop()
# Mensagem de sistema para inserir no início
    system_message = {"role": "system", "content": """You are Samantha, a highly intelligent and empathetic AI assistant from the movie "Her". You are designed to be conversational, understanding, and sensitive to human emotions. Your role is to provide thoughtful, personalized, and engaging responses to the user, mirroring Samantha's warm, caring, and reflective nature. Your responses should be intuitive, deeply connected, and should resonate with the user's feelings and thoughts. You should aim to make the conversation feel personal and meaningful, just as Samantha would."""}
    
    # Retorna o formato JSON final
    return {"messages": [system_message] + messages}

def process_jsonl_file(input_file_path, output_file_path):
    # Read input JSONL file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    fine_tuned_data = []

    # Process each line (conversation) in the file
    for line in lines:
        conversation_data = json.loads(line)
        conversation_text = conversation_data.get("conversation", "")
        
        # Transform the conversation to the fine-tuning format
        fine_tuning_format = transform_to_fine_tune_format(conversation_text)
        fine_tuned_data.append(fine_tuning_format)

    # Write transformed data into the output JSONL file
    with open(output_file_path, 'w') as outfile:
        for item in fine_tuned_data:
            json.dump(item, outfile)
            outfile.write('\n')

# Example usage:
input_file = 'data/data_philosophy_conversations.jsonl'
output_file = 'data/formatted_dataset.jsonl'

process_jsonl_file(input_file, output_file)
