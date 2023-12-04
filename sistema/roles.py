from rolepermissions.roles import AbstractUserRole


class Doutor(AbstractUserRole):
    available_permissions = {'listar_paciente': True, 'alterar_dados': True, 'atender_paciente':True}

class Recepcionista(AbstractUserRole):
    available_permissions = {'atender_paciente': True, 'listar_paciente': True}