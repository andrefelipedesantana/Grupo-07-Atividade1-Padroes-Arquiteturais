import os
import sys
import torch
from transformers import pipeline
from sklearn.metrics.pairwise import cosine_similarity


def obter_estrutura_projeto(caminho):
    estrutura = []
    for raiz, diretorios, arquivos in os.walk(caminho):
        nivel = raiz.replace(caminho, "").count(os.sep)
        recuo = "  " * nivel
        estrutura.append(f"{recuo}{os.path.basename(raiz)}/")
        for arquivo in arquivos:
            estrutura.append(f"{recuo}  {arquivo}")
    return "\n".join(estrutura)


def dividir_em_blocos(texto, max_linhas=30):
    linhas = texto.split("\n")
    for i in range(0, len(linhas), max_linhas):
        yield "\n".join(linhas[i:i + max_linhas])


def principal():
    if len(sys.argv) < 2:
        print("Uso: python ia.py <caminho_do_projeto>")
        sys.exit(1)

    caminho_projeto = sys.argv[1]

    if not os.path.exists(caminho_projeto):
        print("Caminho inválido:", caminho_projeto)
        sys.exit(1)

    estrutura_texto = obter_estrutura_projeto(caminho_projeto)
    print(estrutura_texto)

    extrator = pipeline(
        task="feature-extraction",
        model="microsoft/codebert-base"
    )

    estrutura_filtrada = "\n".join([
        linha for linha in estrutura_texto.split("\n")
        if not any(ignorar in linha for ignorar in [
            ".git", "__pycache__", "node_modules", "build", "dist"
        ])
    ])

    embeddings = []
    for bloco in dividir_em_blocos(estrutura_filtrada):
        vetores = extrator(bloco)
        embedding = torch.tensor(vetores).mean(dim=1).squeeze()
        embeddings.append(embedding)

    embedding_projeto = torch.stack(embeddings).mean(dim=0)

    padroes = {
        "MVC": """
            controller/
            service/
            repository/
            views/
        """,
        "Layered": """
            presentation/
            application/
            domain/
            infrastructure/
        """,
        "Microservices": """
            user-service/
            order-service/
            api-gateway/
            config-server/
            discovery-server/
        """,
        "Event-Driven": """
            events/
            consumers/
            producers/
            broker/
        """,
        "Hexagonal": """
            core/
            domain/
            application/
            adapters/
            inbound/
            outbound/
        """,
        "Clean Architecture": """
            entities/
            usecases/
            interface_adapters/
            frameworks/
        """,
        "CQRS": """
            commands/
            queries/
            read_model/
            write_model/
        """,
        "Microkernel": """
            core/
            plugins/
            extensions/
        """,
        "Pipe-and-Filter": """
            pipes/
            filters/
        """,
        "Service-Oriented": """
            services/
            registry/
            gateway/
            client/
        """,
        "Client-Server": """
            client/
            server/
        """,
        "Peer-to-Peer": """
            peers/
            network/
            discovery/
        """,
        "Space-Based": """
            processing-units/
            data-grid/
            feeder/
            replicator/
        """
    }

    embeddings_padroes = {}
    for nome, estrutura in padroes.items():
        vetores = extrator(estrutura)
        embeddings_padroes[nome] = torch.tensor(vetores).mean(dim=1).squeeze()

    melhor_padrao = None
    melhor_valor = -1.0

    for nome, emb_padrao in embeddings_padroes.items():
        similaridade = cosine_similarity(
            embedding_projeto.unsqueeze(0),
            emb_padrao.unsqueeze(0)
        )[0][0]

        print(f"{nome}: {similaridade:.3f}")

        if similaridade > melhor_valor:
            melhor_valor = similaridade
            melhor_padrao = nome

    print("Padrão mais provável:", melhor_padrao, f"({melhor_valor:.3f})")


if __name__ == "__main__":
    principal()
