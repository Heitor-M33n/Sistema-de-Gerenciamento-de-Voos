from abc import ABC, abstractmethod
import uuid

# -------------------------------------------------
# 1) Interface                                   🡇
# -------------------------------------------------
class Logavel(ABC):
    """Qualquer classe logável DEVE implementar logar_entrada()."""
    @abstractmethod
    def logar_entrada(self):
        pass


# -------------------------------------------------
# 2) Mixins                                      🡇
# -------------------------------------------------
class IdentificavelMixin:
    """Gera um ID único; combine-o com outras classes."""
    def __init__(self):
        # TODO: gerar e armazenar um ID (use uuid.uuid4())
        pass
    def get_id(self):
        # TODO: retornar o ID
        pass


class AuditavelMixin:
    """Fornece logs simples ao console."""
    def log_evento(self, evento: str):
        # TODO: imprimir no formato  [LOG] <mensagem>
        pass


# -------------------------------------------------
# 3) Classe base Pessoa                          🡇
# -------------------------------------------------
class Pessoa:
    """Classe base para pessoas do sistema."""
    def __init__(self, nome: str, cpf: str):
        # TODO: armazenar nome e cpf como atributos protegidos
        pass
    @property
    def nome(self):
        # TODO: retornar o nome
        pass
    def __str__(self):
        # TODO: "Maria (123.456.789-00)"
        pass


# -------------------------------------------------
# 4) Bagagem — classe simples                    🡇
# -------------------------------------------------
class Bagagem:
    def __init__(self, descricao: str, peso: float):
        self.descricao = descricao
        self.peso = peso  # kg
    def __str__(self):
        return f"{self.descricao} – {self.peso} kg"


# -------------------------------------------------
# 5) Passageiro                                  🡇
# -------------------------------------------------
class Passageiro(Pessoa):
    """Herda de Pessoa e possui bagagens."""
    def __init__(self, nome: str, cpf: str):
        # TODO: chamar super().__init__ e criar lista vazia de bagagens
        pass
    def adicionar_bagagem(self, bagagem: Bagagem):
        # TODO: adicionar bagagem à lista
        pass
    def listar_bagagens(self):
        # TODO: imprimir as bagagens
        pass


# -------------------------------------------------
# 6) Funcionario (herança múltipla + mixins)     🡇
# -------------------------------------------------
# TODO: Implementar a classe Funcionario
# - Herda de Pessoa, IdentificavelMixin e Logavel (pode usar AuditavelMixin)
# - Atributos: cargo, matricula
# - Métodos:
#   • exibir_dados() → imprime nome, cargo, matrícula e ID
#   • logar_entrada() → registra no log


# -------------------------------------------------
# 7) MiniAeronave                                🡇
# -------------------------------------------------
class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int):
        # TODO: armazenar modelo e capacidade
        pass
    def resumo_voo(self):
        # TODO: retornar string com modelo e capacidade
        pass


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

