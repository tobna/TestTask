import matplotlib as mpl
from matplotlib import pyplot as plt
import os
import json

mpl.use('pgf')

mpl.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False
})

def plot_logs(logs, name):
  fig, axs = plt.subplots(1, 2, figsize=(8, 4))
  fig.subplots_adjust(wspace=.35)
  axs[0].plot(list(range(len(logs))), [log['train_loss'] for log in logs])

  axs[0].set_title('training loss')
  axs[0].set_xlabel('epoch')
  axs[0].set_ylabel('loss')
  axs[1].plot(list(range(len(logs))), [log['train_acc'] for log in logs])
  axs[1].set_title('training accuracy')
  axs[1].set_xlabel('epoch')
  axs[1].set_ylabel('accuracy')
  plt.savefig(f'{name}.pgf', format='pgf')

for f in os.listdir('.'):
  if not f.endswith('.logs'):
    continue
  with open(f, 'r') as file:
    data = json.load(file)
  name = f[:-5]
  print(name)
  plot_logs(data, name)
