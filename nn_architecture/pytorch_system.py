import torch
import numpy as np

class vanderpol(torch.nn.Module):

    def __init__(self):
        
        super(vanderpol, self).__init__()
        self.mu = 2.
        self.state_variables = ['x', 'y']
    
    def forward(self, X, U):
        x, y = torch.split(X[:, 0], split_size_or_sections=1, dim=1)
        xdt = self.mu * (x - 1/3 * x**3 - y)
        ydt = 1/self.mu * x
        return torch.concat((xdt, ydt), dim=1)
            
class lorenz(torch.nn.Module):

    def __init__(self):

        super(lorenz, self).__init__()
        self.sigma = 10
        self.rho = 28 
        self.beta = 8/3
        self.state_variables = ['x', 'y', 'z']
     
    def forward(self, X, U):
        x, y, z  = torch.split(X[:, 0], split_size_or_sections=1, dim=1)
        xdt = self.sigma * (y - x)
        ydt = self.rho * x - y - x * z
        zdt = x * y - self.beta * z
        return torch.concat((xdt, ydt, zdt), dim=1)
    
class coupled_mass(torch.nn.Module):

    def __init__(self):
        super(coupled_mass, self).__init__()
        self.m1 = 1
        self.k1 = 10
        self.c1 = 0.1
        self.a1 = 0.01
        self.m2 = 5
        self.k2 = 20
        self.c2 = 1
        self.a2 = 1
        self.state_variables = ['x1', 'x2', 'x3', 'x4']
     
    def forward(self, X, U):
        x, vx, y, vy = torch.split(X[:, 0], split_size_or_sections=1, dim=1)
        dx__dt = vx
        dvx__dt = -self.k1 / self.m1 * (x - y) - self.c1/self.m1 * vx - self.a1/self.m1 * (x - y)**3
        dy__dt = vy
        dvy__dt = -self.k2 / self.m2 * (y - x) - self.c2/self.m2 * vy - self.a2/self.m2 * (y - x)**3
        return torch.concat((dx__dt, dvx__dt, dy__dt, dvy__dt), dim=1)
      