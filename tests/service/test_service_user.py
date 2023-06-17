from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_com_sucesso(self):
        # Setup
        name_add = 'Felipe'
        job_add = 'PO'
        resultado_esperado = 'Usuario adicionado com sucesso'
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_add, job=job_add)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_validate_existing_user(self):
        # Setup
        name_rep = 'Mateus'
        job_rep = 'QA'
        resultado_esperado = 'Usuario ja cadastrado'
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_rep, job=job_rep)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_validate_null_user(self):
        # Setup
        name_null = None
        job_null = 'QA'
        resultado_esperado = 'Usuario nao adicionado'
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_null, job=job_null)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_validate_null_job(self):
        # Setup
        name_null = 'Andrea'
        job_null = None
        resultado_esperado = 'Usuario nao adicionado'
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_null, job=job_null)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_validate_invalid_user(self):
        # Setup
        name_inv = 100
        job_inv = 'UI'
        resultado_esperado = 'Nome ou Profissao precisa ser um texto'
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_inv, job=job_inv)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_validate_invalid_job(self):
        # Setup
        name_inv = 'Fidelis'
        job_inv = 100
        resultado_esperado = 'Nome ou Profissao precisa ser um texto'
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_inv, job=job_inv)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_delete_user_with_success(self):
        #Setup
        name = 'Mateus'
        resultado_esperado = 'Usuario removido'
        service = ServiceUser()

        #Chamada
        resultado = service.del_user(name=name)

        #Avaliacao
        assert resultado_esperado == resultado

    def test_validate_delete_invalid_user(self):
        #Setup
        name = 'Mieth'
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        #Chamada
        resultado = service.del_user(name=name)

        #Avaliacao
        assert resultado_esperado == resultado

    def test_validate_delete_null_user(self):
        #Setup
        name = None
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        #Chamada
        resultado = service.del_user(name=name)

        #Avaliacao
        assert resultado_esperado == resultado

    def test_update_job_with_success(self):
        #Setup
        name = 'Mateus'
        job = 'SM'
        resultado_esperado = 'Job atualizado com sucesso'
        service = ServiceUser()

        #Chamada
        resultado = service.update_user(name=name, new_job=job)

        #Avaliação
        assert resultado_esperado == resultado

    def test_validate_update_job_invalid_user(self):
        #Setup
        name = 'Baiano'
        job = 'TechLead'
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        #Chamada
        resultado = service.update_user(name=name, new_job=job)

        #Avaliação
        assert resultado_esperado == resultado

    def test_validate_update_job_null_user(self):
        #Setup
        name = None
        job = 'UX'
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        #Chamada
        resultado = service.update_user(name=name, new_job=job)

        #Avaliação
        assert resultado_esperado == resultado

    def test_select_user_success(self):
        #Setup
        name = 'Mateus'
        resultado_esperado = 'Job: QA'
        service = ServiceUser()

        #Chamada
        resultado = service.select_user(name=name)

        #Avaliação
        assert resultado_esperado == resultado

    def test_validate_select_invalid_user(self):
        #Setup
        name = 'Baiano'
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        #Chamada
        resultado = service.select_user(name=name)

        #Avaliação
        assert resultado_esperado == resultado

    def test_validate_select_null_user(self):
        #Setup
        name = None
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        #Chamada
        resultado = service.select_user(name=name)

        #Avaliação
        assert resultado_esperado == resultado