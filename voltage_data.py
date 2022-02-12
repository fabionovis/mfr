import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline


class VoltageData:

    def __init__(self, t, v):
        t = np.array(t, dtype=np.float64)
        v = np.array(v, dtype=np.float64)
        self._data = np.column_stack((t, v))
        self._spline = InterpolatedUnivariateSpline(t, v, k=3)
        
    def __len__(self):
        return len(self._data[:,0])
        
    def __getitem__(self, index):
        return self._data[index]
        
    @property
    def voltages(self):
        return self._data[:,1]
        
    @property
    def timestamps(self):
        return self._data[:,0]
        
    @classmethod
    def from_file(cls, file_path):
        t, v = np.loadtxt(file_path, unpack=True)
        return cls(t, v)
        
    def __iter__(self):
        return iter(self._data)
        
    def __repr__(self):
        return '\n'.join((f'{line[0]} {line[1]}' for line in self._data))
        
    def __str__(self):
        rows = (f'{index} --> {line[0]} {line[1]}' for index, line in enumerate(self._data))
        return '\n'.join(rows)
        
    def __call__(self, x):
        return self._spline(x)
        
    def plot(self, ax=None, fmt='bo', **plot_options):
        from matplotlib import pyplot as plt
        if ax is not None:
            plt.sca(ax)
        else:
            ax = plt.figure('Voltage data')
        plt.plot(self.timestamps, self.voltages, fmt, **plot_options)
        plt.xlabel('Time [ms]')
        plt.ylabel('Voltages [mV]')
        plt.grid(True)
        return ax
        
      
      
      
      
      
      
      
      
      
    
