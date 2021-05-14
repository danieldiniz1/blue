def func (x):
    print("x é: ",x)
    x=2
    print("Valor local alterado de x para",x)
x=50
func (x)
print("x ainda é: ",x)


def func():
    global x
    x = 9 # aqui está sendo alterado o objeto x global
    y = x*2
    print("x global existe dentro da função: valor= {0}".format(x)) 
    print("y local existe dentro da função: valor= {0}".format(y)) 

print("inicio do programa")
x=10
print("x global existe fora da função: valor= {0}".format(x))
func()
print("x global alterado dentro da função: valor= {0}".format(x))
print("fim do programa")

print()

def maior(x,y):
    if x>y:
        return x
    else:
        return y
print(maior(47,88))