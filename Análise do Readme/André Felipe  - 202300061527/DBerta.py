# ============================================================
# Análise de Padrões Arquiteturais com modelo mDeBERTa via Google Collab
# ============================================================

# 📦 1. Instale a biblioteca (roda apenas uma vez no terminal):
# pip install -U transformers torch

# 🧠 2. Importa o pipeline da biblioteca Hugging Face
from transformers import pipeline

# ⚙️ 3. Carrega o modelo de classificação zero-shot multilíngue
classifier = pipeline(
    "zero-shot-classification",
    model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"
)

# 📝 4. Texto para análise
texto_para_analisar = """
A análise combinada das imagens descreve uma arquitetura de sistema onde um 
controlador central, um LLM, gerencia um fluxo de trabalho complexo. O processo 
começa com uma solicitação do usuário. Na Etapa 1, Planejamento da Tarefa, o 
controlador LLM decompõe a solicitação complexa em múltiplas sub-tarefas 
atômicas (como T1, T2, T3) e identifica as dependências entre elas. Na Etapa 2, 
Seleção de Modelo, o controlador consulta ativamente um hub externo (HuggingFace) 
para selecionar dinamicamente os modelos especialistas independentes mais adequados 
para executar cada sub-tarefa individual. Na Etapa 3, Execução da Tarefa, o sistema 
invoca cada modelo especialista selecionado em seu próprio endpoint (seja local ou 
híbrido), passando os argumentos necessários e coletando suas predições. Finalmente, 
na Etapa 4, Geração de Resposta, o controlador LLM agrega os resultados e predições 
de todas as sub-tarefas executadas e os resume em uma resposta final e coerente 
para o usuário. O sistema funciona como um orquestrador central que despacha, 
invoca e compõe os resultados de múltiplos serviços independentes.
"""

# 🏷️ 5. Labels (rótulos) para classificação
meus_labels = [
    'Arquitetura de Orquestração de Serviços (um controlador central que coordena múltiplos serviços independentes)',
    'Sistema Distribuído (componentes rodam em processos ou máquinas separadas e se comunicam pela rede)',
    'Arquitetura baseada em API (comunicação entre componentes feita estritamente por APIs)',
    'Modelo Requisição-Resposta (padrão de comunicação onde um cliente envia um pedido e espera uma resposta)',
    'Arquitetura de Microsserviços (serviços pequenos, independentes e focados em negócio)',
    'Sistema Monolítico Centralizado (uma única aplicação com um único ponto de controle e execução)',
    'Arquitetura Orientada a Eventos (comunicação assíncrona baseada na produção e consumo de mensagens)'
]

# 🚀 6. Executa a análise
resultado = classifier(texto_para_analisar, meus_labels, multi_label=True)

# 📊 7. Exibe os resultados ordenados
print("\n--- Resultados da Análise com o modelo mDeBERTa-v3 ---")
resultados_ordenados = sorted(zip(resultado['labels'], resultado['scores']),
                              key=lambda x: x[1], reverse=True)

for label, score in resultados_ordenados:
    print(f"{label}: {score*100:.1f}%")
