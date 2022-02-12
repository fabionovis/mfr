import math

class Particle:
    '''class describing a generic particle
    '''
    def __init__(self, mass, charge, name, momentum = 0.):
        '''class constructor'''
        self.mass = mass   # in MeV
        self.charge = charge   # in units of e
        self.name = name 
        self.momentum = momentum   # in MeV/c^2
        
    def stampa(self):
        '''prints informations about the particle
        '''
        print(f'The particle is a {self.name} with mass {self.mass} MeV/c^2, charge = {self.charge}e and momentum = {self.momentum} MeV/c')
     
    @property    
    def energy(self):
        return math.sqrt(self.momentum**2 + self.mass**2)
        
    @energy.setter
    def energy(self, energy):
        if energy < self.mass:
            print(f'Particle cannot have energy less than its mass ({self.mass} MeV/c^2)')
        else:
            self.momentum = math.sqrt(energy**2 - self.mass**2)
        
    @property    
    def beta(self):
        return self._momentum/self.energy
        
    @beta.setter
    def beta(self, beta):
        if (beta < 0.) or (beta > 1.):
            print('The value of beta must be in the range [0,1]')
            return
        if (not (beta < 1.)) and (self.mass > 0.):
            print('Only massless particles can travel at the speed of light!')
            return
        else:
            self.momentum = self.mass*beta/math.sqrt(1.-beta**2)
        
    @property
    def gamma(self):
        return self.energy/self.mass
        
        
    @property
    def momentum(self):
        return self._momentum
        
    @momentum.setter
    def momentum(self, momentum):
        if momentum<0:
            print('Cannot set the module of the momentum to negative values \n Momentum has been set to 0')
            self._momentum = 0.
        else:
            self._momentum = momentum
    
        
class Proton(Particle):
    '''Class describing the Proton
    '''
    NAME = 'Proton'
    MASS = 938.
    CHARGE = +1
    def __init__(self, momentum = 0.):
        Particle.__init__(self, self.MASS, self.CHARGE, self.NAME, momentum)
        
class Alpha(Particle):
    '''Class describing Alpha particle
    '''
    NAME = 'Alpha particle'
    MASS = 3727.
    CHARGE = +2
    def __init__(self, momentum = 0.):
        Particle.__init__(self, self.MASS, self.CHARGE, self.NAME, momentum)
        
pr = Proton(momentum = 100.)
alpha = Alpha(momentum = 200.)

print(pr.beta)
pr.beta = 1
print(pr.beta)
print(f'la nuova energia è {pr.energy:.2f} MeV e il nuovo impulso è {pr.momentum:.2f} MeV/c')
#pr.stampa()
#alpha.stampa()