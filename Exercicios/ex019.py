import math

ang = float(input("Digite o ângulo que você deseja: "))

seno = math.sin(math.radians(ang))
cose = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print("O ângulo de {} tem o seno de {:.2f}".format(ang, seno))
print("O ângulo de {} tem o cosseno de {:.2f}".format(ang, cose))
print("O ângulo de {} tem a tangente de {:.2f}".format(ang, tang))
