-
---
### Primeiro Experimento - 17/05/2026 20:20
**Alterações Técnicas:** - N_PARTICULAS = 40, RAIO_event_horizon = 0.4, FORCA_GRAVIDADE = 0.008

**Observação do event_horizon:**
- Todas as particulas foram sugadas para o event_horizon em aproximadamente 1 segundo. O contador do nada foi para 40 como esperado. O espaço ficou vazio.

**Lógica do Python aplicada:**
- O código usou filtros de matriz (NumPy) para identificar partículas menores que o raio do event_horizon e as moveu para a variável de exílio 'NADA'.
---

---
### Experimento 02  - 17/05/2026 21:35
**Alterações Técnicas:** - Apenas adicionei um marcador de tempo, que falhou devido à motivos que estaram na observação abaixo.

**Observação do event_horizon:**
- 3 partículas atingiram órbita estável e resistiram ao exílio.
- O cronômetro marcou 0.00s pois o universo nunca ficou 100% vazio.
- Isso prova que a informação pode entrar em loop eterno se a velocidade lateral equilibrar a gravidade.

**Lógica do Python aplicada:**
- O código usou filtros de matriz (NumPy) para identificar partículas menores que o Raio do event_horizon e as moveu para a variável de exílio 'NADA'.
---

---
### Experimento 03  - 17/05/2026 22:35
**Alterações Técnicas:** - -Adição de Variável de Massa: Inércia individual para cada partícul (0.5 a 2.5). -Implementação de Buffer de Processamentos: Remoção gradual no event_horizon baseada no "peso" da informação. -Sistema de Cronometragem individual: Registro exato de cada evento de exílio.

**Observação do event_horizon:**
- O relatório mostrou uma curva de 0.03s até 3.60s. Isso confirma que massas diferentes criam gargalos de processamento diferentes. 
- 3 partículas atingiram órbita estável. A massa elevada combinada com a velocidade lateral impediu que o buffer de processamento concluído a tempo.
- O universo levou em média 0.98s para processar cada unidade de informação.

**Lógica do Python aplicada:**
- O código usou filtros de matriz (NumPy) para identificar partículas menores que o Raio do event_horizon e as moveu para a variável de exílio 'NADA'.
---

---
### Experimento 04  - 18/05/2026 00:40
**Alterações Técnicas:** - Aumentei o número de partículas de 50 para 100.

**Observação do event_horizon:**
- O tempo de exílio saltou de quase 0s para 8.87s, provando que massa elevada gera latência no processamento. 
- 6 partículas (6%) criaram órbitas estáveis e não foram engolidas, confirmando o limite de saturação do event_horizon.
- O fluxo médio subiu para 1.20s, indicando um sistema de alta densidade informativa.

**Lógica do Python aplicada:**
- O código usou filtros de matriz (NumPy) para identificar partículas menores que o Raio do event_horizon e as moveu para a variável de exílio 'NADA'.
---

---
### Experimento 05  - 18/05/2026 01:05
[Gif perdido]

**Alterações Técnicas:** - Aumentei o fator de escala/atração de 0.4 para 1.0 e as partículas diminui de 100 para 50.

**Observação do event_horizon:**
- O aumento na intensidade fez com que a "zona de escape" praticamente sumisse. Partículas que antes orbitariam agora são puxadas com força bruta.
- Com o valor em 1.0, o fluxo de informações se torna mais agressivo. A latência diminui porque a "vontade" do event_horizon de processar matéria vence a inércia das partículas mais rápido.
- Em 0.4 existia um equilíbrio (as partículas orbitvam na borda). Em 1.0, existe uma execução. É o limite onde a física vira apenas processamento puro.

**Lógica do Python aplicada:**
- O código usou filtros de matriz (NumPy) para identificar partículas menores que o Raio do event_horizon e as moveu para a variável de exílio 'NADA'.
---

---
### Experimento 06  - 18/05/2026 01:44
**Alterações Técnicas:** - Aumentei para 500 partículas simultâneas, mantendo a força de 0.4, mas com o nascimento concentrado próximo ao centro (-1, 1).

**Observação do event_horizon:**
- O sistema foi inundado instantaneamente. A timeline mostra dezenas de exílios em   0.0s, provando que o buffer suporta alta densidade sem travar.
- Mesmo com 10x mais partículas, o tempo médio foi de apenas 0.30s. O sistema limpou o universo de forma extremamente rápida devido à densidade inicial.
- Todas as 500 partículas foram processadas com sucesso. A última levou 1.08s, provando que o event_horizon não perde eficiência mesmo sob alta carga de dados.

**Lógica do Python aplicada:**
- O código usou filtros de matriz (NumPy) para identificar partículas menores que o Raio do event_horizon e as moveu para a variável de exílio 'NADA'.
---

---
### Experimento 07  - 18/05/2026 20:33
**Alterações Técnicas:** - Gravidade Absoluta (Colapso): O event_horizon foi mantido em 1.0, e teve um aumento na força de atração de 0.008 para 0.08. A velocidade das partículas foi aumentada de 0.02 para 0.1, porém não foi o suficiente para vencer a atração.

Velocidade Alta (Grande Fugitiva): Mantivemos as alterações na gravidade, mas injetamos uma velocidade inicial de 0.9 nas partículas. Isso permitiu que 165 partículas resistissem ao Horizonte de Eventos, aumentando o tempo médio para 1.48s.

O Equilibrado (Teste do Disco): Foi o ajuste do "Número Mágico". Reduzimos a força do event_horizon para a faixa de 0.5, permitindo que as partículas não fossem engolidas nem fugissem, mas ficassem presas em uma órbita estável.

**Observação do event_horizon:**
- 01 (Colapso): Mostra um "vácuo" visual rápido. As partículas surgem e somem quase no mesmo frame, provando que o sistema de limpeza de buffer ('NADA') está funcionando a todo vapor.

- 02 (Resistência): É possível ver as partículas lutando contra o centro. Elas descrevem trajetórias mais longas e espalhadas antes de serem capturadas, mostrando o cabo de guerra entre a velocidade e o event_horizon.

- 03 (Equilíbrio): O mais estável. As partículas formam um padrão circular (disco de acreção) ao redor do ponto vermelho, validando a matemática de vetores. Está precisa o suficiente para manter um sistema solar ou uma galáxia.

**Lógica do Python aplicada:**
- O código usou filtros de matriz (NumPy) para identificar partículas menores que o Raio do event_horizon e as moveu para a variável de exílio 'NADA'.
---
-----atualizando essa prr