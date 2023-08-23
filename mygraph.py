import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,20,100)
plt.plot(x,np.sin(x))
plt.show()

#create environment-end all terminals, create new terminal, in terminal put: python3 -m venv (environment name)
#activate environment- in terminal put: source (environment name)/bin/activate
#install plugin - interminal put: pip install plotlib
