from PIL import Image
def carregar_imagem(caminho_imagem):
    return Image.open(caminho_imagem)

# Exemplo de uso:
imagem = carregar_imagem(r"C:\Users\USUARIO\simple-package-template-master\package_name\transferir1.jpeg")

imagem.show()
