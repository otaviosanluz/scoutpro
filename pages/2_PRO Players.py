import streamlit as st 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import os
from matplotlib.patches import Rectangle

df_data = st.session_state['data']

clubes = df_data['Team'].value_counts().index
clubes_ordered= clubes.sort_values(ascending=True)
club = st.sidebar.selectbox('Team', clubes_ordered)

df_players = df_data[df_data['Team'] == club]
players_counts = df_players['Player'].value_counts().index
players_ordered= players_counts.sort_values(ascending=True)
player = st.sidebar.selectbox('Player', players_ordered)

st.sidebar.markdown('Developed by [Otavio Santos](https://www.linkedin.com/in/otaviosanluz/)')

player_stats = df_data[df_data['Player'] == player].iloc[0]

#st.title(f"{player_stats['Player']}")

#col1, col2, col3, col4 = st.columns(4)

#col1.markdown(f"**Clube:** {player_stats['Team']}")
#col2.markdown(f"**Posição:** {player_stats['Position']}")  
#col3.markdown(f"**Idade:** {player_stats['Age']}") 
#col4.markdown(f"**Minutagem:** {player_stats['Minutes']}")  

jogador = player_stats['Player']
clube = player_stats['Team']
posicao = player_stats['Position']
idade = player_stats['Age']
minutagem = player_stats['Minutes']
    
# Criar uma nova figura com tamanho mínimo
fig, ax = plt.subplots(figsize=(6, 1))  # Ajuste o tamanho conforme desejado
fig.patch.set_facecolor('#222222')

# Configurar texto do jogador
ax.text(0, 0.95, f'{jogador}', ha='left', va='center', transform=ax.transAxes,
        color='white', fontsize=18, fontweight='bold')  # Ajuste a posição do texto do nome do jogador

# Configurar texto do clube
ax.text(0, 0.65, f'{clube}', ha='left', va='center', transform=ax.transAxes,
        color='white', fontsize=12)

ax.text(0, 0.2, f'Position: {posicao}', ha='left', va='center', transform=ax.transAxes,
            color='white', fontsize=9)
ax.text(0.6, 0.2, f'Age: {idade}', ha='left', va='center', transform=ax.transAxes,
        color='white', fontsize=9)
ax.text(1.0, 0.2, f'Minutes: {minutagem}', ha='left', va='center', transform=ax.transAxes,
        color='white', fontsize=9)

# Definir limites dos eixos
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)

# Remover eixos
ax.axis('off')

# Plotas gráfico
st.pyplot(fig)

colunas_selecionadas = colunas_selecionadas = ['Tackles', 'Aerial',
       'Interception', 'Recuperation', 'Dribble', 'Progressive Carries',
       'Carries for Penalty Area', 'Carries for Final Third',
       'Expected Assists (xA)', 'Key Pass', 'Progressive Pass', 'Short Pass',
       'Medium Pass', 'Long Pass', 'Expected Goals (xG)',
       'Non-penalty expected goals (npxG)', 'Goals']

### PERCENTILE ###

# Criar uma única figura fora do loop
fig_percentile, ax = plt.subplots(figsize=(20, 16))

# Selecionar os dados do jogador escolhido
dados_grafico = player_stats[colunas_selecionadas]

# Calcular a posição da barra destacada
jogador_posicao = dados_grafico[colunas_selecionadas].values

# Desenhar a barra com a mesma saturação de cor para todas as estatísticas
ax.barh(colunas_selecionadas, jogador_posicao, color='#32FF92', alpha=0.5)

# Adicionar quadrado destacado para a porcentagem do jogador
for i, valor in enumerate(jogador_posicao):
    ax.text(valor + 2, i, f'{int(valor)}%', color='white', va='center', fontsize = 24) 
    ax.plot([valor], [i], marker='s', markersize=10, color='orange')  # Quadrado laranja para destacar

# Personalizar o fundo do gráfico
fig_percentile.patch.set_facecolor('#222222')
ax.set_facecolor('#222222')

# Personalizar as cores dos rótulos e da grade
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', labelsize=30, colors='white')

# Remover borda lateral
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Remover ticks no eixo y
ax.tick_params(axis='y', which='both', left=False)

# Definir limites fixos para o eixo x
ax.set_xlim(0, 100)  # Substitua os valores pelos limites desejados

# Remover valores do eixo x
ax.set_xticks([])

# Adicionar título
titulo = 'PERCENTILE'
ax.text(0.25, 1.05, titulo, horizontalalignment='center', verticalalignment='center', fontsize=45, transform=ax.transAxes, color = 'white', fontweight='bold')

# Definir os rótulos do eixo x
ax.set_xticks([20, 50, 80])
ax.set_xticklabels(['Low', 'Average', 'High'], fontsize=30)

# Exibir a figura no Streamlit
st.pyplot(fig_percentile)

### GRÁFICO RADAR ####

# Defina as categorias do gráfico de radar
categorias = ['', '', '', '']

# Ajuste os ângulos para posicionar "Defensive" e "Finishing" mais para cima
angulos = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False)

# Cria o gráfico de radar
fig_radar, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Seleciona as quatro últimas colunas
dados_radar = player_stats[-4:]

ax.set_ylim(0, 100)

# Personalizar o fundo do gráfico
fig_radar.patch.set_facecolor('#222222')
ax.set_facecolor('#222222')

# Valores para a imagem central
ax.fill(angulos, dados_radar, color='#32FF92', alpha=0.5)

# Remover os valores no centro
ax.set_yticklabels([])

# Adicione as legendas e ajuste o layout
ax.set_thetagrids(angulos * 180/np.pi, categorias)

# Adiciona as legendas manualmente
ax.text(angulos[0], 110, "Defensive", color='white', ha='left')
ax.text(angulos[1], 110, "Keeping", color='white', ha='center')
ax.text(angulos[2], 110, "Passing", color='white', ha='right')
ax.text(angulos[3], 110, "Finishing", color='white', ha='center')

# Ajuste os rótulos das categorias para evitar sobreposição
ax.set_rlabel_position(45)  # Ajusta a posição dos rótulos radiais

# Definindo o número desejado de círculos
#num_circulos = 5
#ax.set_yticks(np.linspace(0, ax.get_ylim()[1], num_circulos))

# Exiba o gráfico
plt.title(f'PLAYER STYLE', color='white', y = 1.1, fontsize = 12, fontweight='bold')  # Título em branco
#ax.legend(loc='upper right', bbox_to_anchor=(50, 50), labels=[''], fontsize='small', facecolor='#222222', edgecolor='white')  # Oculta a legenda

# Tornar o círculo mais externo em branco
ax.spines['polar'].set_color('white')
#ax.spines['polar'].set_linewidth(0)

#ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1), labels=[''], fontsize='small', facecolor='#222222', edgecolor='white')  # Oculta a legenda

# Tornar as palavras "passing", "keeping", "finishing" e "defensive" em branco
for label in ax.get_xticklabels():
    if label.get_text() in ["Passing", "Keeping", "Finishing", "Defensive"]:
        label.set_color('white')

# Exibir a figura no Streamlit
st.pyplot(fig_radar)











