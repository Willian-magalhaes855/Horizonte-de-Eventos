import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib 
matplotlib.use('Agg')  # Evita que o codigo abra uma janela

# --- CONFIGURAÇÕES DO UNIVERSO ---
N_PARTICULAS = 100
RAIO_event_horizon = 0.4
FORCA_GRAVIDADE = 0.008
TEMPO_LIMITE_BUFFER = 15  # Esforço necessário para processar a massa

# Inicialização técnica
posicoes = np.random.uniform(-4, 4, (N_PARTICULAS, 2))
velocidades = np.random.uniform(-0.02, 0.02, (N_PARTICULAS, 2))
# Massas variadas: Influenciam inércia e tempo de buffer
massas = np.random.uniform(0.5, 2.5, N_PARTICULAS)
buffer_processamento = np.zeros(N_PARTICULAS)

# Métrica individual
tempos_de_exilio = []
particulas_ativas = np.ones(N_PARTICULAS, dtype=bool)

fig, ax = plt.subplots(figsize=(6, 6), facecolor='#1a1a1a')
ax.set_facecolor('#1a1a1a')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# O event_horizon (Horizonte de Eventos)
event_horizon = plt.Circle((0, 0), RAIO_event_horizon, color='red', fill=False, ls='--', lw=2)
ax.add_patch(event_horizon)

# O tamanho do ponto no gráfico agora depende da massa (s=massas*20)
scat = ax.scatter(posicoes[:, 0], posicoes[:, 1], s=massas*20, c='cyan', edgecolors='white', alpha=0.8)
texto_info = ax.text(-4.5, 4.5, '', color='white', fontweight='bold')

def update(frame):
    global posicoes, velocidades, particulas_ativas, buffer_processamento
    
    if not np.any(particulas_ativas):
        return scat, texto_info

    # 1. Cálculo da Física (Aceleração inversamente proporcional à massa)
    direcoes = -posicoes
    distancias = np.linalg.norm(direcoes, axis=1, keepdims=True)
    distancias = np.maximum(distancias, 0.1) 
    direcoes_norm = direcoes / distancias

    # f = m * a  => a = f / m
    aceleracao = (direcoes_norm * FORCA_GRAVIDADE) / massas[:, np.newaxis]
    velocidades += aceleracao
    posicoes += velocidades

    # 2. Lógica de Buffer (Processamento no event_horizon)
    dist_centro = np.linalg.norm(posicoes, axis=1)
    no_raio = (dist_centro < RAIO_event_horizon) & particulas_ativas
    
    # Partículas no event_horizon acumulam progresso de saída baseado na sua massa
    # Quanto mais massa, menos progresso por frame (demora mais)
    buffer_processamento[no_raio] += (1 / massas[no_raio])
    
    # 3. Identificar quem terminou o processamento
    quem_sumiu = (buffer_processamento >= TEMPO_LIMITE_BUFFER / 10) & particulas_ativas
    
    for _ in range(np.sum(quem_sumiu)):
        tempos_de_exilio.append(frame / 30) # Registra o tempo individual
    
    particulas_ativas[quem_sumiu] = False
    
    # Atualiza visual (move as inativas para longe)
    pos_visiveis = posicoes.copy()
    pos_visiveis[~particulas_ativas] = [100, 100]
    scat.set_offsets(pos_visiveis)
    
    texto_info.set_text(f"Processadas: {np.sum(~particulas_ativas)} | Ativas: {np.sum(particulas_ativas)}")
    return scat, texto_info

# Frames aumentados para 300 para dar tempo de processar as pesadas
ani = FuncAnimation(fig, update, frames=300, interval=30, blit=True)

print(" Iniciando motor com Massa, Buffer e Cronometragem Individual...")
try:
    ani.save('experimento_massa.gif', writer='pillow', fps=30)
    
    print("\n" + "="*40)
    print(" RELATÓRIO TÉCNICO FINAL")
    print("="*40)
    
    if tempos_de_exilio:
        tempos_de_exilio.sort()
        print(f" Partículas Ejetadas: {len(tempos_de_exilio)} de {N_PARTICULAS}")
        print(f" Timeline de Exílio (segundos):")
        
        # Mostra a lista completa de 5 em 5
        for i in range(0, len(tempos_de_exilio), 5):
            print(f"   {tempos_de_exilio[i:i+5]}")
            
        media = sum(tempos_de_exilio) / len(tempos_de_exilio)
        print(f"\n  Tempo Médio: {media:.2f}s")
        print(f" Tempo da Última: {max(tempos_de_exilio):.2f}s")
    
    # Checagem de Órbitas
    sobras = np.sum(particulas_ativas)
    if sobras > 0:
        print(f"\n ALERTA: {sobras} partículas resistiram ao event_horizon.")
        print("Causa: Órbita estável ou massa elevada para o tempo de simulação.")
    else:
        print(f"\n SUCESSO: Todas as informações foram processadas.")
    print("="*40)

except Exception as e:
    print(f" Erro ao salvar: {e}")

#atualizando essa prra