.

# Live Fine-tuning com Dados do Hugging Face

Este projeto demonstra como realizar fine-tuning de modelos de linguagem grandes usando dados do Hugging Face em tempo real, inspirado pela inteligência artificial Samantha do filme Her.

## Visão Geral

Este repositório contém o código-fonte para um sistema que permite realizar fine-tuning de modelos de linguagem grandes utilizando dados do Hugging Face em tempo real. O objetivo é fornecer uma solução rápida e eficiente para treinar modelos personalizados diretamente no navegador do usuário, explorando as possibilidades de interação entre humanos e inteligência artificial, similar à relação entre Theodore e Samantha em Her.

## Funcionamento

O sistema funciona da seguinte forma:

1. Os dados de treinamento são carregados do Hub do Hugging Face.
2. O modelo base é baixado e inicializado.
3. O sistema realiza o fine-tuning incrementalmente, atualizando o modelo com base nos dados do usuário.
4. O modelo treinado é usado para responder perguntas ou realizar tarefas específicas.

## Dependências

Para executar este projeto, você precisará instalar as dependências listadas no arquivo `requirements.txt`. Você pode fazer isso usando pip:

```
pip install -r requirements.txt
```

## Como Usar

1. Clone o repositório:

   ```
   git clone https://github.com/enricoferraz/live-finetuning-hf.git
   cd live-finetuning-hf
   ```

2. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

3. Execute o script principal:

   ```
   python hf_finetuning.py
   ```

## Arquivos Principais

- `finetuning-gpt.py`: Contém o código principal para o processo de fine-tuning.
- `process-data.py`: Trata e prepara os dados do Hugging Face para o treinamento.
- `hf_finetuning.py`: Gerencia o processo de fine-tuning em tempo real usando dados do Hub do Hugging Face.
- `test.py`: Contém testes para verificar a funcionalidade do sistema.

## Configurações

As configurações do projeto estão armazenadas no arquivo `.env`. Certifique-se de ajustar essas configurações conforme necessário, incluindo as informações de acesso ao Hub do Hugging Face.

## Contribuições

Contribuações são bem-vindas! Por favor, lembre-se de seguir as convenções de codificação e adicionar testes adequados para qualquer nova funcionalidade ou correção de bugs.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE). Veja o arquivo LICENSE para mais detalhes.

## Créditos

Este projeto foi inspirado pela inteligência artificial Samantha do filme Her, dirigido por Spike Jonze. Agradecemos ao trabalho de muitos contribuintes para o ecossistema do Hugging Face e ao filme que inspirou este projeto.
