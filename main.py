from abc import ABC, abstractmethod
import uuid

class Logavel(ABC):
    """Qualquer classe logável DEVE implementar logar_entrada()."""
    @abstractmethod
    def logar_entrada(self):
        pass

class IdentificavelMixin:
    """Gera um ID único; combine-o com outras classes."""
    def __init__(self) -> None:
        self.id = uuid.uuid4()
        
    def get_id(self) -> uuid.UUID:
        return self.id

class AuditavelMixin:
    """Fornece logs simples ao console."""
    def log_evento(self, evento: str):
        print(f"[LOG] {evento}")

class Pessoa:
    """Classe base para pessoas do sistema."""
    def __init__(self, nome: str, cpf: str) -> None:
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self) -> str:
        return self._nome
    
    def __str__(self) -> str:
        return f"{self._nome} ({self._cpf})"

class Bagagem:
    """Classe para bagagens de passageiros."""
    def __init__(self, descricao: str, peso: float) -> None:
        self.descricao = descricao
        self.peso = peso
    def __str__(self) -> str:
        return f"{self.descricao} – {self.peso} kg"

class Passageiro(Pessoa):
    """Herda de Pessoa e possui bagagens."""
    def __init__(self, nome: str, cpf: str) -> None:
        super().__init__(nome, cpf)
        self._bagagens = []

    def adicionar_bagagem(self, bagagem: Bagagem) -> None:
        if isinstance(bagagem, Bagagem):
            self._bagagens.append(bagagem)
        else:
            raise ValueError("Bagagem deve ser uma instância da classe Bagagem.")

    def listar_bagagens(self) -> None:
        if not self._bagagens:
            print(f"{self.nome} não possui bagagens.")
        else:
            print(f"Bagagens de {self.nome}:")
            for bagagem in self._bagagens:
                print(f"- {bagagem}")

class Funcionario(Logavel, Pessoa, IdentificavelMixin, AuditavelMixin):
    """Classe para funcionários do sistema."""
    def __init__(self, nome: str, cpf: str, cargo: str, matricula: str) -> None:
        Pessoa.__init__(self, nome, cpf)
        IdentificavelMixin.__init__(self)
        self._cargo = cargo
        self._matricula = matricula

    def exibir_dados(self) -> None:
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Matrícula: {self.matricula}, ID: {self.get_id()}")

    def logar_entrada(self) -> None:
        self.log_evento(f"{self.nome} logou no sistema.")

class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int):
        self.modelo = modelo
        self.capacidade = capacidade
    def resumo_voo(self):
        return f"{self.modelo} (Capacidade: {self.capacidade})"


class Voo:
    '''Classe para representar um voo'''
    def __init__(self, numero_voo: str, origem: str, destino: str, aeronave: MiniAeronave):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        if isinstance(aeronave, MiniAeronave):
            self.aeronave = aeronave
        else:
            raise ValueError("Aeronave deve ser uma instância da classe MiniAeronave.")
        self.passageiros = []
        self.tripulacao = []
        
    def adicionar_passageiro(self, passageiro: Passageiro):
        if isinstance(passageiro, Passageiro):
            if passageiro in self.passageiros:
                print(f"Passageiro {passageiro.nome} já está no voo {self.numero_voo}.")
                return
            if len(self.passageiros) < self.aeronave.capacidade:
                self.passageiros.append(passageiro)
            else:
                print(f"Voo {self.numero_voo} está cheio. Não é possível adicionar {passageiro.nome}.")
        else:
            raise ValueError("Passageiro deve ser uma instância da classe Passageiro.")
    
    def adicionar_tripulante(self, funcionario: Funcionario):
        if isinstance(funcionario, Funcionario):
            self.tripulacao.append(funcionario)
        else:
            raise ValueError("Tripulante deve ser uma instância da classe Funcionario.")
        
    def listar_passageiros(self):
        if not self.passageiros:
            print(f"Voo {self.numero_voo} não possui passageiros.")
        else:
            print(f"Passageiros do voo {self.numero_voo}, de {self.origem} para {self.destino}:")
            for passageiro in self.passageiros:
                print(f"- {passageiro}")
    
    def listar_tripulacao(self):
        if not self.tripulacao:
            print(f"Voo {self.numero_voo} não possui tripulação.")
        else:
            print(f"Tripulação do voo {self.numero_voo}, de {self.origem} para {self.destino}:")
            for tripulante in self.tripulacao:
                print(f"- {tripulante}")    
    

class CompanhiaAerea:
    """Agrupa seus voos (has-a)."""
    def __init__(self, nome: str):
        if len(nome) <= 3:
            raise ValueError("Nome da companhia aérea deve ter mais de 3 caracteres.")
        self._nome = nome
        self.voos = []
        
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome: str):
        if len(novo_nome) <= 3:
            raise ValueError("Nome da companhia aérea deve ter mais de 3 caracteres.")
        self._nome = novo_nome
        
    def adicionar_voo(self, voo):
        if isinstance(voo, Voo):
            if voo in self.voos:
                print(f"Voo {voo.numero_voo} já está cadastrado na companhia {self.nome}.")
                return
            self.voos.append(voo)
        else:
            raise ValueError("Voo deve ser uma instância da classe Voo.")
    def buscar_voo(self, numero: str):
        for voo in self.voos:
            if voo.numero_voo == numero:
                return voo
        print(f"Voo {numero} não encontrado na companhia {self.nome}.")
    def listar_voos(self):
        for voo in self.voos:
            print(f" Voo {voo.numero_voo} de {voo.origem} para {voo.destino} - Aeronave: {voo.aeronave.resumo_voo()}")


class Auditor(IdentificavelMixin, Logavel):
    def __init__(self, nome: str):
        super().__init__()
        self.nome = nome
    def logar_entrada(self):
        print(f"[LOG] Auditor {self.nome} logou no sistema.")
    def auditar_voo(self, voo: Voo):
        if isinstance(voo, Voo):
            print(f"Auditoria: {voo.numero_voo}:")
            conformidade = True
            if len(voo.passageiros) > voo.aeronave.capacidade:
                print(f"  - Passageiros excedem a capacidade ({len(voo.passageiros)} > {voo.aeronave.capacidade})")
                conformidade = False
            if len(voo.tripulacao) == 0:
                print("  - Nenhum tripulante registrado.")
                conformidade = False
            if conformidade == True:
                print("  - Voo em conformidade.")
            else:
                print("  - Voo NÃO está em conformidade.")
    def __str__(self):
        return f"Auditor {self.nome} (ID: {self.get_id()})"
            
        
# -------------------------------------------------
# 10) Auditor (Identificável + Logável)          🡇
# -------------------------------------------------
# TODO: Implementar a classe Auditor
# - Herda de IdentificavelMixin e Logavel
# - Atributo: nome
# - Métodos:
#   • logar_entrada() → registra entrada no sistema
#   • auditar_voo(voo) → verifica:
#       ▸ passageiros ≤ capacidade
#       ▸ existe ao menos 1 tripulante
#     imprime relatório de conformidade
#   • __str__() → "Auditor <nome> (ID: ...)"


# -------------------------------------------------
# 11) Bloco de teste                             🡇
# -------------------------------------------------
if __name__ == "__main__":
    """
    TODO:
      • Criar 2 companhias, 2 voos cada, passageiros, funcionários e auditor.
      • Adicionar bagagens, listar passageiros, auditar voos.
      • Mostrar saídas no console para validar implementações.
    """
    pass



