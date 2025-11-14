import os
import sys
import torch
from transformers import pipeline
from sklearn.metrics.pairwise import cosine_similarity


def localizar_arquivos_dependencias(caminho):
    candidatos = [
        "requirements.txt",
        "pyproject.toml",
        "Pipfile",
        "Pipfile.lock",
        "setup.py"
    ]

    encontrados = []

    for raiz, diretorios, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            if arquivo in candidatos:
                encontrados.append(os.path.join(raiz, arquivo))

    return encontrados


def ler_arquivos(lista_arquivos):
    conteudo_total = ""
    for arquivo in lista_arquivos:
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                conteudo = f.read()
                conteudo_total += conteudo + "\n"
        except:
            pass
    return conteudo_total


def dividir_texto(texto, max_tokens=300):
    linhas = texto.split("\n")
    blocos = []
    bloco_atual = []
    tamanho_atual = 0

    for linha in linhas:
        tokens = len(linha.split())
        if tamanho_atual + tokens > max_tokens:
            blocos.append("\n".join(bloco_atual))
            bloco_atual = []
            tamanho_atual = 0

        bloco_atual.append(linha)
        tamanho_atual += tokens

    if bloco_atual:
        blocos.append("\n".join(bloco_atual))

    return blocos


def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    caminho_projeto = sys.argv[1]

    if not os.path.exists(caminho_projeto):
        sys.exit(1)

    arquivos_dep = localizar_arquivos_dependencias(caminho_projeto)

    if not arquivos_dep:
        sys.exit(0)

    texto_dependencias = ler_arquivos(arquivos_dep)

    blocos = dividir_texto(texto_dependencias, max_tokens=30)

    extrator = pipeline(
        task="feature-extraction",
        model="microsoft/codebert-base"
    )

    embeddings = []
    for bloco in blocos:
        features = extrator(bloco)
        emb = torch.tensor(features).mean(dim=1).squeeze()
        embeddings.append(emb)

    embedding_dependencias = torch.stack(embeddings).mean(dim=0)

    padroes = {
        "MVC": """
            django
            flask
            fastapi
            jinja2
        """,
        "Camadas": """
            dependency-injector
            sqlalchemy
            pydantic
            marshmallow
        """,
        "Microsservicos": """
            fastapi
            flask
            uvicorn
            docker
            grpcio
            redis
            aiohttp
        """,
        "Direcionado-a-Eventos": """
            kafka
            confluent-kafka
            pika
            celery
            redis
            rq
        """,
        "Hexagonal": """
            dependency-injector
            sqlalchemy
            pydantic
            injector
        """,
        "Clean-Architecture": """
            fastapi
            pydantic
            dependency-injector
            sqlalchemy
        """,
        "CQRS": """
            pydantic
            eventsourcing
            celery
            kafka
        """,
        "Microkernel": """
            importlib
            pluggy
            stevedore
        """,
        "Pipe-and-Filter": """
            pandas
            numpy
            airflow
            prefect
        """,
        "Orientado-a-Servicos": """
            zeep
            fastapi
            flask
            grpcio
        """,
        "Peer-to-Peer": """
            asyncio
            websockets
            libp2p
        """,
        "Space-Based": """
            redis
            hazelcast-python-client
            celery
        """
    }

    embeddings_padroes = {}
    for nome, deps in padroes.items():
        features = extrator(deps)
        embeddings_padroes[nome] = torch.tensor(features).mean(dim=1).squeeze()

    melhor_padrao = None
    melhor_score = -1

    for nome, emb_padrao in embeddings_padroes.items():
        similaridade = cosine_similarity(
            embedding_dependencias.unsqueeze(0),
            emb_padrao.unsqueeze(0)
        )[0][0]

        if similaridade > melhor_score:
            melhor_score = similaridade
            melhor_padrao = nome

    print(melhor_padrao, f"{melhor_score:.3f}")


if __name__ == "__main__":
    main()
