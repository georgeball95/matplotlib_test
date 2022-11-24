import matplotlib.pyplot as plt
import random

fig, ax = plt.subplots(figsize=(6,6))

for i in range(20):
    
    for m in range(20):
        
        if random.random() < 0.2:
            
            plt.scatter([m],[i],marker="s",s=150,color="orange",alpha=0.9)
            
        else:
            
            plt.scatter([m],[i],marker="s",s=150,color="grey",alpha=0.9)

plt.axis('off')

plt.tight_layout(pad=0.1)

plt.savefig("randomplot.png",dpi=300)

plt.show()