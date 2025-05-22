import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do CSV em DataFrame
df1 = pd.read_csv('min_operacionais_sbrf.csv')

# Certificar-se de que os valores das colunas 'pf' e 'rvrf' são numéricos
df1['pf'] = pd.to_numeric(df1['pf'], errors='coerce')
df1['rvrf'] = pd.to_numeric(df1['rvrf'], errors='coerce')

# Ordenar o DataFrame pelos valores de 'rvrf' em ordem decrescente
df1 = df1.sort_values('rvrf', ascending=False)

# Função para plotar e adicionar anotações
def plot_and_annotate(df, label, color, marker):
    plt.plot(df['rvrf'], df['METARF'], label=label, color=color, marker=marker)
    for i in range(len(df)):
        plt.annotate(f"{df['pf'].iloc[i]:.3%}",  
                     (df['rvrf'].iloc[i], df['METARF'].iloc[i]), 
                     textcoords="offset points", 
                     xytext=(0,5), fontsize=12, 
                     ha='center')

# Criar a figura
plt.figure(figsize=(12, 8))
plot_and_annotate(df1, 'SBRF - FALS', '#e8f25e', 's')

# Ajustar o fontsize para os valores do eixo y
plt.yticks(fontsize=15)

# Ajustar manualmente os ticks do eixo X para os valores exatos da coluna 'rvrf'
plt.xticks(df1['rvrf'], fontsize=13)

# Inverter a ordem dos valores no eixo x para decrescente
plt.gca().invert_xaxis()

# Aumentar o tamanho da legenda
plt.legend(fontsize=15)

# Definir xlabel e ylabel
plt.xlabel('', fontsize=15, ha='right', va='bottom')
plt.ylabel('', fontsize=15, ha='left', va='top')

# Adicionar título ao gráfico
plt.title('')

plt.show()
