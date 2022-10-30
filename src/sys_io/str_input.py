def StringInput(message: str = "", mandatory: bool = False, margin: int = 0):
    """Permite obtener un input de tipo string"""
    while True:
        inputValue = input(" " * margin + message)
        if (not mandatory or (mandatory and inputValue != "")):
            return inputValue
        else:
            print('[ERROR]: Este input es obligatorio')
            print()
