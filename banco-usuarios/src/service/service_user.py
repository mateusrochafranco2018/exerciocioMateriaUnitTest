from src.models.store import Store
from src.models.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()

    def check_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None

    ###    adicionar (nulo ou string)
    ###    nome adicionado já existe (nao pode add o mesmo nome com jobs diferents)

    def add_user(self, name, job):
        if name is not None and job is not None:
            if type(name) is str and type(job) is str:
                if self.check_user(name):
                    return "Usuario ja cadastrado"
                else:
                    user = User(name=name, job=job)
                    self.store.bd.append(user)
                    return "Usuario adicionado com sucesso"
            else:
                return "Nome ou Profissao precisa ser um texto"
        else:
            return "Usuario nao adicionado"

    ###    deletar (nao pode deletar quem nao existe)

    def del_user(self, name):
        user_bd = self.check_user(name)
        if user_bd != None:
            self.store.bd.remove(user_bd)
            return "Usuario removido"
        return "Usuario não encontrado"

    ###    update(apenas atualizar o job)
    def update_user(self, name, new_job):
        user_bd = self.check_user(name)
        if user_bd is not None:
            user_bd.job = new_job
            return "Job atualizado com sucesso"
        else:
            return "Usuario não encontrado"

    ### recuperar o trabalho da pessoa dado o nome dela
    def select_user(self, name):
        user_bd = self.check_user(name)
        if user_bd is not None:
            return "Job: " + user_bd.job
        else:
            return "Usuario não encontrado"