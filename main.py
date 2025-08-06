from sistema_voo import (
    CompanhiaAerea,
    Voo,
    Passageiro,
    Bagagem,
    Funcionario,
    Auditor,
    MiniAeronave
)

companhias = []
auditor = Auditor('Auditor chefe')

def menu():
    print('/n ======= MENU DO SISTEMA DE VOOS ====')
    print('1 - Listar companhias')
    print('2 - Criar nova companhia')
    print('3 - Criar novo voo')
    print('4 - Adicionar passageiro a voo')
    print('5 - Adicionar tripulante a voo')
    print('7 - Listar voos de uma companhia')
    print('8 - sair')
