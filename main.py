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


# -------------------------------------------------
# 8) Voo (composição com MiniAeronave)           🡇
# -------------------------------------------------
# TODO: Implementar a classe Voo
# - Atributos: numero_voo, origem, destino, aeronave
# - Listas: passageiros, tripulacao
# - Métodos:
#   • adicionar_passageiro()  (verificar duplicidade e capacidade)
#   • adicionar_tripulante()
#   • listar_passageiros()
#   • listar_tripulacao()


# -------------------------------------------------
# 9) CompanhiaAerea                              🡇
# -------------------------------------------------
class CompanhiaAerea:
    """Agrupa seus voos (has-a)."""
    def __init__(self, nome: str):
        # TODO: validar nome (≥ 3 letras) e criar lista vazia de voos
        pass
    @property
    def nome(self):
        # TODO: retornar nome
        pass
    @nome.setter
    def nome(self, novo_nome: str):
        # TODO: validar + atualizar nome
        pass
    def adicionar_voo(self, voo):
        # TODO: adicionar voo à lista
        pass
    def buscar_voo(self, numero: str):
        # TODO: retornar voo ou None
        pass
    def listar_voos(self):
        # TODO: imprimir todos os voos
        pass


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

