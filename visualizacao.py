import datetime

def registrar_experimento():
    print("--- ASSISTENTE DE REGISTRO DA TEORIA DO event_horizon ---")
    
    # Coletando o que você fez
    alteracoes = input("Quais alterações você fez no código?: ")
    observacao = input("O que aconteceu no GIF?: ")
    
    # Criando o texto do relatório
    data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    relatorio = f"""
---
### Experimento ""  - {data_hora}
**Alterações Técnicas:** - {alteracoes}

**Observação do event_horizon:**
- {observacao}

**Lógica do Python aplicada:**
- O código usou filtros de matriz (NumPy) para identificar partículas menores que o Raio do event_horizon e as moveu para a variável de exílio 'NADA'.
---
"""

    # O Pulo do Gato: Ele abre o seu arquivo NOTAS.md e "anexa" (append) o texto no final
    with open("NOTAS.md", "a", encoding="utf-8") as arquivo:
        arquivo.write(relatorio)
    
    print("\n✅ O relatório foi gravado automaticamente no seu arquivo NOTAS.md!")

if __name__ == "__main__":
    registrar_experimento()