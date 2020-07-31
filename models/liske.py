class liske:

    def __init__(self, id, liskeName, liske = None):
        self.id = id
        self.liskeName = liskeName
        self.liske = liske if liske != None else []

    
    def add_task(self, new_task):
        # TODO: Verificar que la task es un objeto task y ademas está completo
        self.liske.append(new_task)