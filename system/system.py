def vanderpol(X, mu = 2):
    x, y = X[0], X[1]
    dx__dt = mu * (x - 1/3 * x**3 - y)
    dy__dt = 1/mu * x
    return [dx__dt, dy__dt]

def lorenz(X, beta = 8/3, sigma = 10, rho = 28):
    x, y, z = X[0], X[1], X[2]
    dx__dt = sigma * (y - x)
    dy__dt = rho * x - y - x * z
    dz__dt = x * y - beta * z
    return [dx__dt, dy__dt, dz__dt]