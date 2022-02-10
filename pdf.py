import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
from matplotlib import pyplot as plt

class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
      def __init__(self, x, y):
         InterpolatedUnivariateSpline.__init__(self, x, y)
         ycdf = np.array([self.integral(x[0], xcdf) for xcdf in x])
         self.cdf = InterpolatedUnivariateSpline(x, ycdf)
         xppf, ippf = np.unique(ycdf, return_index='True')
         yppf = x[ippf]
         self.ppf = InterpolatedUnivariateSpline(xppf, yppf)
         
      def plot_hist(self, x):
         N = 10000
         
         plt.figure('pdf')
         plt.plot(x, self(x))
         plt.xlabel('x')
         plt.ylabel('pdf(x)')
         
         plt.figure('cdf')
         plt.plot(x, self.cdf(x))
         plt.xlabel('x')
         plt.ylabel('cdf(x)')
         
         plt.figure('Sampling')
         plt.hist(self.ppf(np.random.uniform(size = N)), bins='auto')
         plt.show()
            
      def integrale(self, a, b):
         return self.cdf(b) - self.cdf(a)   
            

if __name__ == '__main__':
 x = np.linspace(-1., 1., 100)
 y = np.zeros(100)
 for i, n in enumerate(x):
  if n < 0:
   y[i] = n+1.
  else:
   y[i] = 1.-n
   
 pdf = ProbabilityDensityFunction(x, y)
 pdf.plot_hist(x)
 print('The probability x is in range [-1, 0] is {}'.format(pdf.integrale(-1., 0)))
