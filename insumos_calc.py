import tensorflow as tf
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def analizeImage(imagePath):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = tf.keras.models.load_model('keras_model.h5')

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(imagePath).convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy arraypyt  
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)

def calcular_area_cultura1(largura, comprimento):
    return largura * comprimento

def calcular_insumos_cultura1(area, insumo_por_metro):
    return area * insumo_por_metro

def dataEntry():
    print("Selecione o tipo de dado")
    while True:
      print("1. Largura do plantio")
      print("2. Comprimento do plantio")
      print("3. Insumo")
      print("4. Deletar dados")
      print("5. Sair do programa")
      escolha = input("Escolha uma opção: ")

def mainMenu():
    while True:
        print("1. Entrada de dados")
        print("2. Saída de dados")
        print("3. Atualizar dados")
        print("4. Deletar dados")
        print("5. Analizar imagem")
        print("6. Sair do programa")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            dataEntry()
            pass
        elif escolha == '2':
            print("Saída de dados")
            # Lógica para saída de dados
            pass
        elif escolha == '3':
            # Lógica para atualizar dados
            pass
        elif escolha == '4':
            # Lógica para deletar dados
            pass
        # elif escolha == '5':
        #     imagePath = input("Insira o caminho da imagem: ")
        #     analizeImage(imagePath)
        #     pass
        elif escolha == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

mainMenu()
