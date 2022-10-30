def NumberInput(message: str = "", margin: int = 0):
    """Permite obtener un input de tipo numérico"""
    while True:
        try:
            inputValue = input(" " * margin + message)
            intValue = int(inputValue)
            return intValue
        except ValueError:
            print('[ERROR]: Este input debe ser numérico')
            print()
