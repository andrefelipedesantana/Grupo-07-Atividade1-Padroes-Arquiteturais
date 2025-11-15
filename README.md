# 🧠 Atividade 1 – Padrões Arquiteturais de Software (Engenharia de Software II)

Este repositório contém todos os artefatos (códigos, prompts, scripts, resultados, imagens etc.) utilizados na **Atividade 01** da disciplina de **Engenharia de Software II**.

O objetivo foi **analisar os padrões arquiteturais** de um projeto de software, o **microsoft/JARVIS (HuggingGPT)**.

---

## 💡 Sobre o Projeto Analisado (JARVIS)

O **JARVIS** é um sistema que funciona como uma **LLM (Modelo de Linguagem Amplo)** central.  
Ele recebe uma tarefa, a divide em subtarefas e as encaminha para outras **LLMs especializadas**, disponíveis na plataforma **Hugging Face**.

---

## 👥 Equipe

| Nº | Nome                              | Matrícula      |
|----|-----------------------------------|----------------|
| 01 | André Felipe de Santana Conceição | 202300061527   |
| 02 | David Vieira Reis                 | 202100011299   |
| 03 | Adailton Moura da Silva           | 202100011154   |
| 04 | Enzo Emanuel Maia Costa           | 202300061901   |
| 05 | Rafael Souza Prata                | 202300061750   |
| 06 | João Filipe de Araújo Santos      | 202100011548   |
| 07 | Vinicius Morais Souza             | 202200060106   |
| 08 | Felipe Ferreira da Silva          | 202100113360   |

---


## 🗂️ Estrutura deste Repositório

Este repositório está organizado em pastas correspondentes aos **tipos de dados analisados** (Readme, Código-Fonte e Estrutura).
Dentro de cada pasta, há subpastas para cada aluno responsável, contendo seus artefatos de análise (códigos-fonte, prompts, notebooks, etc.).

```text
📦 Engenharia_SoftwareII_2025-2_T04_JARVIS
│
├── 📂 Análise da Estrutura do Projeto/
│   ├── 📂 Adailton Moura da Silva - 2021.../
│   ├── 📂 David Vieira Reis - 2021.../
│   └── 📂 Vinicius Morais Souza - 2022.../
│
├── 📂 Análise do Código-Fonte/
│   ├── 📂 Enzo Emanuel - 2023.../
│   ├── 📂 Rafael Souza Prata - 2023.../ 
│
├── 📂 Análise do Readme/
│   ├── 📂 André Felipe - 2023.../
│   └── 📂 Felipe Ferreira - 2021.../
│
└── 📄 README.md ← (Este arquivo)
```

# 🛠️ Reprodutibilidade e Ambiente de Execução

Esta seção descreve a infraestrutura utilizada e as instruções necessárias para replicar as análises de IA.

---

## 🔧 Infraestrutura (Ambiente de Execução)

As análises foram realizadas em **dois tipos de ambiente**: nuvem (para a maioria dos modelos) e local (para o `codebert-base`).

---

## ☁️ Ambiente de Nuvem — Google Colab

A maior parte das análises foi executada no **Google Colab** (serviço gratuito).

**Especificações:**

- **Serviço:** Google Colab (back-end Google Compute Engine)  
- **GPU:** 15.0 GB de memória  
- **RAM do Sistema:** 12.7 GB  
- **Disco:** 112.6 GB disponíveis  

---

## 💻 Ambiente Local — VS Code

A análise vetorial com **codebert-base** foi executada localmente.

**Requisitos Mínimos:**

- **Hardware:**  
  - CPU (funciona, porém lento)  
  - GPU com **4 GB+ de VRAM** (recomendado)  
- **RAM do Sistema:** 16 GB recomendados  
- **Software:**  
  - VS Code com extensão Python  
  - Python **3.8+**

---

## 📌 Instruções para Execução (Como Replicar)

A replicação das análises pode ser feita de duas maneiras, dependendo da abordagem utilizada pelo membro da equipe.

---

### 1. 🟦 Análise via Interface Web (Hugging Face)

Algumas análises (ex.: Rafael e Vinícius) utilizaram a interface de widget disponível na própria página do modelo no Hugging Face.

**Como executar:**

1. Acesse o link do modelo de IA (ex.: `meta-llama/Llama-3.1-8B-Instruct`).  
2. Na interface **Inference**, cole o prompt e os dados de entrada (como os arquivos `.txt`).  
3. Os tutoriais detalhados e os prompts utilizados estão nas pastas dos respectivos alunos e, também, no link do tutorial escrito que está disponpivel ao final do Readme.

---

### 2. 🟩 Análise via Código (Google Colab)

Outras análises (ex.: André, Felipe e Enzo) utilizaram código Python para executar os modelos.

**Como executar:**

1. Acesse a pasta do aluno neste repositório  
   (ex.: `/Análise do Readme/André Felipe - 2023.../`).  
2. Localize o script (`.py`) da análise e copie-o.  
3. Abra o arquivo no **Google Colab**.
4. Adicione um novo bloco de código e cole o script copiado.
5. Clique em **"Executar tudo"** (`Runtime > Run all`).  

O código já inclui:
- instalação de dependências (como *transformers*),  
- carregamento do modelo,  
- execução completa da análise.

---

## 3. 🖥️ Análise via Execução Local (VS Code)

A análise com **codebert-base** (David, Adailton, João Felipe) foi executada localmente.

### ✔️ Como executar:

### 🔹 Pré-requisitos

Tenha os arquivos:

- `diretorios.py`
- `dependencias.py`
- `requirements.txt`

(localizados na pasta `Análise da Estrutura do Projeto/`)

E um **clone do projeto JARVIS** na sua máquina.

---

### 🔹 Crie um Ambiente Virtual

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 🔹 Instale as dependências

```bash
pip install -r requirements.txt
```

### 🔹 Execute a análise
Passe o caminho do seu clone local do JARVIS como argumento para os scripts.

```bash
python diretorios.py "C:\caminho\para\o\projeto\JARVIS"
python dependencias.py "C:\caminho\para\o\projeto\JARVIS"
```

---

## 📚 Tutoriais e Relatório Final

O material escrito e audiovisual contendo os tutoriais da elaboração e execução das atividades de forma detalhada para cada membro está disponível nos links a seguir:

- 📄 **Tutorial Escrito (Relatório Completo):** [Acesse aqui](https://docs.google.com/document/d/1LzsOySSWbhy81r3u3X7ldHWZYF_D6ev-isXvMyRwxqQ/edit?usp=sharing)
- 🎥 **Tutorial Gravado (Vídeo):** [Acesse aqui](https://drive.google.com/file/d/1nwgLRhP7H86so4XC7LhvmYyNlCcLmOYX/view?usp=drive_link)


---

