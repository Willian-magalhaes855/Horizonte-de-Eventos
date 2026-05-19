# Horizonte-De-Eventos: Simulação Gravitacional e Performance

Motor de simulação em Python utilizando cálculos vetoriais e processamento matricial com **NumPy**. O foco do projeto é a análise de performance em larga escala e a estabilidade de sistemas dinâmicos.

## Experimentos de Performance

### 1. Processamento Massivo (Teste de Estresse)
* **Objetivo:** Validar a latência do sistema com alta densidade de informação.
* **Carga:** 500 partículas geradas simultaneamente.
* **Resultado:** Tempo médio de processamento de **0.30s**. A última unidade foi processada em 1.08s, demonstrando a eficiência dos filtros de matriz do NumPy em impedir gargalos de CPU.

### 2. Estabilidade Orbital (Teste de Disco)
* **Objetivo:** Calibração do equilíbrio entre força central e velocidade inercial.
* **Parâmetros:** Gravidade ajustada para 0.5 com velocidade inicial de 0.9.
* **Resultado:** Obtenção de órbita estável (configuração de disco de acreção). O teste valida a precisão da matemática de vetores aplicada para manter um sistema em equilíbrio sem colapso informativo.

## Stack Técnica
* **Linguagem:** Python
* **Processamento:** NumPy (Operações vetorizadas)
* **Interface:** Visual Studio Code / WSL Ubuntu
