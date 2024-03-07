import random
import time

# Listas de características para os personagens
nomes = ["Aragorn", "Gandalf", "Frodo", "Legolas", "Gimli", "Bilbo", "Samwise", "Gollum", "Saruman", "Galadriel"]
racas = ["Humano", "Elfo", "Anão", "Hobbit", "Orc", "Ent", "Meio-Elfo", "Meio-Orc"]
classes = ["Guerreiro", "Mago", "Ladrão", "Clérigo", "Bardo", "Paladino", "Ranger"]
atributos = {
    "Força": (8, 18),
    "Destreza": (8, 18),
    "Constituição": (8, 18),
    "Inteligência": (8, 18),
    "Sabedoria": (8, 18),
    "Carisma": (8, 18)
}


# Função para gerar um personagem aleatório
def gerar_personagem():
    nome = random.choice(nomes)
    raca = random.choice(racas)
    classe = random.choice(classes)
    atributos_rolados = {atributo: random.randint(min_value, max_value) for atributo, (min_value, max_value) in
                         atributos.items()}

    personagem = {
        "Nome": nome,
        "Raça": raca,
        "Classe": classe,
        "Atributos": atributos_rolados
    }

    return personagem


# Função para imprimir um personagem
def imprimir_personagem(personagem):
    print("Nome:", personagem["Nome"])
    print("Raça:", personagem["Raça"])
    print("Classe:", personagem["Classe"])
    print("Atributos:")
    for atributo, valor in personagem["Atributos"].items():
        print(f" - {atributo}: {valor}")


# Gerar e imprimir um personagem aleatório
if __name__ == "__main__":
    personagem_aleatorio = gerar_personagem()
    print('=-'*16)
    print("GERANDO PERSONAGEM ALEATÓRIO...")
    print('=-' * 16)
    time.sleep(1)
    imprimir_personagem(personagem_aleatorio)
