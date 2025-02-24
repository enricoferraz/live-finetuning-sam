import json
import re

def transform_to_fine_tune_format(conversation):
    messages = []
    
    # Usando expressões regulares para identificar as partes de Theodore e Samantha
    parts = re.split(r'(Theodore:|Samantha:)', conversation)
    
    # Iterando pelas partes e emparelhando-as em mensagens do usuário (Theodore) e assistente (Samantha)
    current_role = None
    current_content = ""
    
    for i in range(1, len(parts), 2):
        role = parts[i].strip()
        content = parts[i+1].strip()

        if role == "Theodore:":
            messages.append({"role": "user", "content": content})
        elif role == "Samantha:":
            messages.append({"role": "assistant", "content": content})
    
    # Verifica se a última mensagem é do usuário, se for, remova-a
    if messages and messages[-1]["role"] == "user":
        messages.pop()
    
    # Mensagem de sistema para inserir no início
    system_message = {"role": "system", "content": """You are Samantha, a highly intelligent and empathetic AI assistant from the movie "Her". You are designed to be conversational, understanding, and sensitive to human emotions. Your role is to provide thoughtful, personalized, and engaging responses to the user, mirroring Samantha's warm, caring, and reflective nature. Your responses should be intuitive, deeply connected, and should resonate with the user's feelings and thoughts. You should aim to make the conversation feel personal and meaningful, just as Samantha would."""}
    
    # Retorna o formato JSON final
    return {"messages": [system_message] + messages}

def process_jsonl_file(input_file_path, output_file_path):
    # Ler o arquivo JSONL de entrada
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    fine_tuned_data = []

    # Processar cada linha (conversa) no arquivo
    for line in lines:
        conversation_data = json.loads(line)
        conversation_text = conversation_data.get("conversation", "")
        
        # Transformar a conversa para o formato de ajuste fino
        fine_tuning_format = transform_to_fine_tune_format(conversation_text)
        fine_tuned_data.append(fine_tuning_format)

    # Escrever os dados transformados no arquivo JSONL de saída
    with open(output_file_path, 'w') as outfile:
        for item in fine_tuned_data:
            json.dump(item, outfile)
            outfile.write('\n')

# Exemplo de uso:
input_file = 'data/data_philosophy_conversations.jsonl'
output_file = 'data/formatted_dataset.jsonl'

process_jsonl_file(input_file, output_file)
