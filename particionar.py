import pandas as pd
import os

def particionar_csv(arquivo, tamanho_particao, diretorio_saida):
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    # Lendo o arquivo CSV em pedaços (chunks)
    chunk_iterator = pd.read_csv(arquivo, chunksize=tamanho_particao)

    # Salvando cada pedaço como um novo arquivo CSV
    for i, chunk in enumerate(chunk_iterator):
        arquivo_saida = os.path.join(diretorio_saida, f"particao_{i+1}.csv")
        chunk.to_csv(arquivo_saida, index=False)
        print(f"Partição {i+1} salva como {arquivo_saida}")

if __name__ == "__main__":
    arquivo = "" # Substitua pelo caminho do seu arquivo CSV
    tamanho_particao = 500000 # Defina o número de linhas por partição
    diretorio_saida = "" # Substitua pelo diretório onde deseja salvar os arquivos particionados

    particionar_csv(arquivo, tamanho_particao, diretorio_saida)
