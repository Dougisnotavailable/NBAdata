# %%
import matplotlib.pylab as plt
import pandas as pd
import seaborn as sns

#data = pd.read_csv(r"C:\Users\User\Desktop\Temp\Python\Projetos\NBA PLAYERS\all_seasons.csv")

#print(data.head())
#data.info()

# %%
import pandas as pd
import matplotlib.pylab as plt
data = pd.read_csv(r"C:\Users\User\Desktop\Temp\Python\Projetos\NBA PLAYERS\all_seasons.csv")
data.hist('player_height', bins=20, rwidth=0.9,
                   color='#607c8e')
plt.title('Height of NBA Players')
plt.xlabel('Height (cm)')
plt.ylabel('Number of Players')
plt.grid(axis='y', alpha=0.75)    
