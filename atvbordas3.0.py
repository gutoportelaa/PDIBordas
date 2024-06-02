from PIL import Image

def load_image(caminho_arquivo):
    imagem = Image.open(caminho_arquivo).convert('L')  # Converte para escala de cinza
    largura, altura = imagem.size
    matriz_imagem = []
    for y in range(altura):
        linha = []
        for x in range(largura):
            pixel = imagem.getpixel((x, y))
            linha.append(pixel)
        matriz_imagem.append(linha)
    print(matriz_imagem)
    imagem.show()
    return imagem, matriz_imagem


def adjacencia_4(imagem):
    altura = len(imagem)
    largura = len(imagem[0])
    matriz_adjacencia = [[0] * largura for each in range(altura)]
    #cor de fundo
    cor_fundo = imagem[0][0]
    for y in range(altura):
        for x in range(largura):
            if imagem[y][x] != cor_fundo and (y < altura - 1 and x < largura - 1) and (y > 0 and x > 0) and (imagem[y-1][x] == cor_fundo or imagem[y+1][x] == cor_fundo or imagem[y][x-1] == cor_fundo or imagem[y][x+1] == cor_fundo):
                matriz_adjacencia[y][x] = imagem[y][x]
            else:
                matriz_adjacencia[y][x] = cor_fundo
                    
    return matriz_adjacencia

def adjacencia_8(imagem):
    altura = len(imagem)
    largura = len(imagem[0])
    matriz_adjacencia = [[0] * largura for each in range(altura)]
    cor_fundo = imagem[0][0]
    for y in range(altura):
        for x in range(largura):
            if imagem[y][x] != cor_fundo  and (y < altura - 1 and x < largura - 1) and (y > 0 and x > 0) and (imagem[y-1][x] == cor_fundo or imagem[y+1][x] == cor_fundo or imagem[y][x-1] == cor_fundo or imagem[y][x+1] == cor_fundo or imagem[y-1][x-1] == cor_fundo or imagem[y+1][x+1] == cor_fundo or imagem[y-1][x+1] == cor_fundo or imagem[y+1][x-1] == cor_fundo):
                matriz_adjacencia[y][x] = imagem[y][x]
            else:
                matriz_adjacencia[y][x] = cor_fundo
    return matriz_adjacencia
def m_adjacencia(imagem):               #Se uma diagonal estiver tingida o pixel em questão não pode estar pode estar, pois causaria conflito de adjacências-4
    matriz_temporaria = adjacencia_4(imagem)            #Correção: Basta aplicar a diagonal, apenas quando não houver adjacência-4
    altura = len(imagem)
    largura = len(imagem[0])
    matriz_adjacencia = [[0] * largura for each in range(altura)]
    fundo = imagem[0][0]    
    for y in range(altura):
        for x in range(largura):
            if matriz_temporaria[y][x] != fundo  and (y < altura - 1 and x < largura - 1) and (y > 0 and x > 0) and (imagem[y-1][x] != fundo or imagem[y+1][x] != fundo or imagem[y][x-1] != fundo or imagem[y][x+1] != fundo):
                matriz_adjacencia[y][x] = imagem[y][x]
            elif matriz_temporaria[y][x] != fundo  and (y < altura - 1 and x < largura - 1) and (y > 0 and x > 0) and (imagem[y-1][x-1] != fundo or imagem[y+1][x+1] != fundo or imagem[y-1][x+1] != fundo or imagem[y+1][x-1] != fundo):
                matriz_adjacencia[y][x] = imagem[y][x]
            if matriz_temporaria[y][x] != fundo and (y < altura - 1 and x < largura - 1) and (y > 0 and x > 0) and (matriz_temporaria[y-1][x-1] != fundo and matriz_temporaria[y+1][+1] != fundo and matriz_temporaria[y+1][x-1] != fundo and matriz_temporaria[y-1][x+1] != fundo):
                matriz_adjacencia[y][x] = fundo                
    return matriz_adjacencia

def mostrar_imagem_gerada(matriz):
    altura = len(matriz)
    largura = len(matriz[0])
    nova_imagem = Image.new("L", (largura, altura))  # Escala de cinza
    cor_fundo = matriz[0][0]
    for y in range(altura):
        for x in range(largura):
            if matriz[y][x] != cor_fundo:
                nova_imagem.putpixel((x, y), matriz[y][x])  # Cor do objeto
            else:
                nova_imagem.putpixel((x, y), cor_fundo)  # Cor de fundo
    nova_imagem.show()



def vizinhos_4(matriz):
    altura = len(matriz)
    largura = len(matriz[0])
    matriz_vizinhos_4 = [[0] * largura for each in range(altura)]
    fundo = matriz[0][0]
    for y in range(altura):
        for x in range(largura):
            if matriz[x][y] != fundo and y < altura - 1 and x < largura - 1:
                matriz_vizinhos_4[x][y] = matriz[x][y]
                matriz_vizinhos_4[x+1][y] = matriz[x][y]
                matriz_vizinhos_4[x][y+1] = matriz[x][y]
                matriz_vizinhos_4[x-1][y] = matriz[x][y]
                matriz_vizinhos_4[x][y-1] = matriz[x][y]

    return matriz_vizinhos_4

def vizinhos_8(matriz):
    altura = len(matriz)
    largura = len(matriz[0])
    matriz_vizinhos_8 = [[0] * largura for each in range(altura)]
    fundo = matriz[0][0]
    for y in range(altura):
        for x in range(largura):
           if matriz[x][y] != fundo  and y < altura - 1 and x < largura - 1:
                matriz_vizinhos_8[x][y] = matriz[x][y]
                matriz_vizinhos_8[x+1][y] = matriz[x][y]
                matriz_vizinhos_8[x][y+1] = matriz[x][y]
                matriz_vizinhos_8[x-1][y] = matriz[x][y]
                matriz_vizinhos_8[x][y-1] = matriz[x][y]
                matriz_vizinhos_8[x+1][y+1] = matriz[x][y]
                matriz_vizinhos_8[x-1][y-1] = matriz[x][y]
                matriz_vizinhos_8[x-1][y+1] = matriz[x][y]
                matriz_vizinhos_8[x+1][y-1] = matriz[x][y]
    return matriz_vizinhos_8

def vizinhos_d(matriz):
    altura = len(matriz)
    largura = len(matriz[0])
    matriz_vizinhos_d = [[0] * largura for each in range(altura)]
    fundo = matriz[0][0]
    for y in range(altura):
        for x in range(largura):
            if matriz[x][y] != fundo and y < altura - 1 and x < largura - 1:
                matriz_vizinhos_d[x][y] = matriz[x][y]
                matriz_vizinhos_d[x+1][y+1] = matriz[x][y]
                matriz_vizinhos_d[x-1][y-1] = matriz[x][y]
                matriz_vizinhos_d[x-1][y+1] = matriz[x][y]
                matriz_vizinhos_d[x+1][y-1] = matriz[x][y]
    return matriz_vizinhos_d








def selecionar_imagem():        # Menu para selecionar a imagem a ser processada
    print("Selecione a imagem que deseja processar:")
    print("1. Imagem do avião")
    print("2. Imagem da folha")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        caminho = "C:\\Users\\gutop\\Downloads\\Ativ.Pratica.00\\aviao.png"
    elif opcao == "2":
        caminho = "C:\\Users\\gutop\\Downloads\\Ativ.Pratica.00\\folha.png"
    else:
        print("Opção inválida. Por favor, selecione 1 ou 2.")
        return selecionar_imagem()

    return caminho

caminho_imagem = selecionar_imagem()
imagem_selecionada, matriz_imagem = load_image(caminho_imagem)

matriz_adjacencia_4 = adjacencia_4(matriz_imagem)
matriz_adjacencia_8 = adjacencia_8(matriz_imagem)
matriz_m_adjacencia = m_adjacencia(matriz_imagem)  

print("Imagem gerada pela 4-Adjacência:")
mostrar_imagem_gerada(matriz_adjacencia_4)
print("\nImagem gerada pela 8-Adjacência:")
mostrar_imagem_gerada(matriz_adjacencia_8)
print("\nImagem gerada pela M-Adjacência:")
mostrar_imagem_gerada(matriz_m_adjacencia)




print("\nImagens geradas(3) pela matriz de vizinhos 4:")
print("\n Adjacencia 4 + vizinhos 4")
mostrar_imagem_gerada(vizinhos_4(matriz_adjacencia_4))
print("\n Adjacencia 8 + vizinhos 4")
mostrar_imagem_gerada(vizinhos_4(matriz_adjacencia_8))
print("\n Adjacencia-M + vizinhos 4")
mostrar_imagem_gerada(vizinhos_4(matriz_m_adjacencia))


print("\nImagens geradas(3) pela matriz de vizinhos 8:")
print("\n Adjacencia 4 + vizinhos 8")
mostrar_imagem_gerada(vizinhos_8(matriz_adjacencia_4))
print("\n Adjacencia 8 + vizinhos 8")
mostrar_imagem_gerada(vizinhos_8(matriz_adjacencia_8))
print("\n Adjacencia-M + vizinhos 8")
mostrar_imagem_gerada(vizinhos_8(matriz_m_adjacencia))


print("\nImagens geradas(3) pela matriz de vizinhos diagonais:")
print("\n Adjacencia 4 + diagonais")
mostrar_imagem_gerada(vizinhos_d(matriz_adjacencia_4))
print("\n Adjacencia 8 + diagonais")
mostrar_imagem_gerada(vizinhos_d(matriz_adjacencia_8))
print("\n Adjacencia-M + diagonais")
mostrar_imagem_gerada(vizinhos_d(matriz_m_adjacencia))
