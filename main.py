from controlador.validations import validarLogin

# Login
intentos = 1
print("Sistema Los Monitos de la Nona")
while intentos <= 3:
    try:
        resu = validarLogin()
        if resu is not None:
            break
        else:
            print("Usuario o contraseña incorrecta")
            intentos += 1
    except:
        print("Vuelve a intentarlo")
if intentos == 4:
    print("Se han excedido los intentos")