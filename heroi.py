# Desafio Dio - Bootcamp 

print("Seja bem vindo(a) a mais uma aventura! Se você é um  aspirante a herói ou heroina, está no lugar certo. Vamos começar nossa jornada!\n\n")

first_attempt = True

while True:
    if first_attempt:
        gender = input("Informe seu gênero (M/F): ")[0].upper()
        first_attempt = False
    else:
        gender = input("Inválido. Informe novamente (M/F): ")[0].upper()
    
    if gender == 'M':
        gender_str = "O herói"
        break
    elif gender == 'F':
        gender_str = "A heroína"
        break


nickname = input("Informe seu nome: ")
xp = int(input("Informe sua experiência: "))


def get_level(xp):
    if xp < 1000:
        return "Ferro"
    elif xp > 1001 and xp < 2000:
        return "Bronze"
    elif xp > 2001 and xp < 5000:
        return "Prata"
    elif xp > 5001 and xp < 7000:
        return "Ouro"
    elif xp > 7001 and xp < 8000:
        return "Platina"
    elif xp > 8001 and xp < 9000:
        return "Ascendente"
    elif xp > 9001 and xp < 10000:
        return "Imortal"
    else:
        return "Radiante"
    
 
level = get_level(xp)

print(f"{gender_str} de nome {nickname}, está no nível {level}")
        