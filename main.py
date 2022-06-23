# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting = "Hello, <name>!"):
    output = greeting.replace("<name>", name)
    return output

print(greet("Eric"))
print(greet("Eric", "What's up, <name>!"))

planets_dict = {"sun": 274, 
    "jupiter": 24.9, 
    "neptune": 11.2, 
    "saturn": 10.4, 
    "earth": 9.8, 
    "uranus": 8.9,
    "venus": 8.9,
    "mars": 3.7,
    "mercury": 3.7,
    "moon": 1.6,
    "pluto": 0.6}

def force(mass, body = "earth"):
    mass = float(mass)
    exerted_force = mass * planets_dict[body]
    return exerted_force

print(force(2, "jupiter"))

def pull(m1, m2, d):
    m1 = float(m1)
    m2 = float(m2)
    d = float(d)
    gravitational_constant = 6.674*10**-11
    gravitational_pull = gravitational_constant * ((m1 * m2)/d**2)
    return gravitational_pull

print(pull(800,1500,3))