# En este nuevo codigo se generaliza la exception
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se pudo localizar el archivo config.txt!")
    except IsADirectoryError:
        print("Se localizo un config.txt, pero es un directorio!")


if __name__ == '__main__':
    main()