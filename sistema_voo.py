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
    def log_evento(self, evento: str) -> None:
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
        return f"{self._nome}, ({self._cpf})"

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

    def __str__(self) -> str:
        return self.nome

class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int) -> None:
        self.modelo = modelo
        self.capacidade = capacidade
        
    def resumo_voo(self) -> str:
        return f"{self.modelo} (Capacidade: {self.capacidade})"

    def __str__(self) -> str:
        return self.resumo_voo

class Voo:
    """Classe para representar um voo"""
    def __init__(self, numero_voo: str, origem: str, destino: str, aeronave: MiniAeronave) -> None:
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        if isinstance(aeronave, MiniAeronave):
            self.aeronave = aeronave
        else:
            raise ValueError("Aeronave deve ser uma instância da classe MiniAeronave.")
        self.passageiros = []
        self.tripulacao = []
        
    def adicionar_passageiro(self, passageiro: Passageiro) -> None:
        if not isinstance(passageiro, Passageiro):
            raise("Passageiro deve ser uma instância da classe Passageiro.")
        elif not len(self.passageiros) < self.aeronave.capacidade:
            print("Aeronave está cheia.")
        else:
            print(f"{passageiro} Adicionado ao voo")
            self.passageiros.append(passageiro)
    
    def adicionar_tripulante(self, funcionario: Funcionario) -> None:
        if not isinstance(funcionario, Funcionario):
            raise ValueError("Funcionário deve ser uma instância da classe Funcionario.")
        else:
            self.tripulacao.append(funcionario)
        
    def listar_passageiros(self) -> None:
        if not self.passageiros:
            print(f"Voo {self.numero_voo} não possui passageiros.")
        else:
            print(f"Passageiros do voo {self.numero_voo}:")
            for passageiro in self.passageiros:
                print(f"- {passageiro}")
    
    def listar_tripulacao(self) -> None:
        if not self.tripulacao:
            print(f"Voo {self.numero_voo} não possui tripulação.")
        else:
            print(f"Tripulação do voo {self.numero_voo}:")
            for tripulante in self.tripulacao:
                print(f"- {tripulante}")    
    
class CompanhiaAerea:
    """Agrupa seus voos (has-a)."""
    def __init__(self, nome: str) -> None:
        if len(nome) <= 3:
            raise ValueError("Nome da companhia aérea deve ter mais de 3 caracteres.")
        else:
            self._nome = nome
            self.voos = []
        
    @property
    def nome(self) -> str:
        return self._nome
        
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        if len(novo_nome) <= 3:
            raise ValueError("Nome da companhia aérea deve ter mais de 3 caracteres.")
        else:
            self._nome = novo_nome
        
    def adicionar_voo(self, voo: Voo) -> None:
        if not isinstance(voo, Voo):
            raise ValueError("Voo deve ser uma instância da classe Voo.")
        elif voo in self.voos:
            print(f"Voo {voo.numero_voo} já está cadastrado na companhia {self.nome}.")
        else:
            self.voos.append(voo)
            
    def buscar_voo(self, numero: str) -> Voo:
        for voo in self.voos:
            if voo.numero_voo == numero:
                return voo
        print(f"Voo {numero} não encontrado.")
        
    def listar_voos(self) -> None:
        print(f"Lista de voos de {self.nome}:")
        for voo in self.voos:
            print(f" Voo {voo.numero_voo}, de {voo.origem} para {voo.destino} - Aeronave: {voo.aeronave.resumo_voo()}")

class Auditor(IdentificavelMixin, AuditavelMixin, Logavel):
    '''Auditor responsável por auditar os voos'''
    def __init__(self, nome: str) -> None:
        super().__init__()
        self.nome = nome
        
    def logar_entrada(self) -> None:
        self.log_evento(f"Auditor {self.nome} logou no sistema.")
        
    def auditar_voo(self, voo: Voo) -> bool:
        if not isinstance(voo, Voo):
            raise ValueError("Voo deve ser uma instância da classe Voo")
            
        print(f"Auditoria: {voo.numero_voo}:")
        conformidade = True
        
        if len(voo.passageiros) > voo.aeronave.capacidade:
            print(f"- Passageiros excedem a capacidade ({len(voo.passageiros)} > {voo.aeronave.capacidade})")
            conformidade = False
            
        if not voo.tripulacao:
            print("- Nenhum tripulante registrado.")
            conformidade = False
            
        if conformidade == True:
            print("- Voo em conformidade.")
        else:
            print("- Voo NÃO está em conformidade.")

        return conformidade
                
    def __str__(self) -> str:
        return f"Auditor {self.nome} (ID: {self.get_id()})"
    
if __name__ == "__main__":
    Gol = CompanhiaAerea("Gol Linhas Aéreas")
    Qatar = CompanhiaAerea("Qatar Airways")
    vgol1 = Voo("GOL564", "Pau dos Ferros", "Mossoró", MiniAeronave("Boeing 737-700", 138))
    vgol2 = Voo("GOL744", "São Paulo", "Montevidéu", MiniAeronave("Boeing 737 MAX 8", 186))
    vqatar1 = Voo("QTR123", "Doha", "Muscat", MiniAeronave("Airbus A320 / A321", 150))
    vqatar2 = Voo("QTR456", "Doha", "Sao Paulo", MiniAeronave("Airbus A350-1000", 350))
    Gol.adicionar_voo(vgol1)
    Gol.adicionar_voo(vgol2)
    Qatar.adicionar_voo(vqatar1)
    Qatar.adicionar_voo(vqatar2)
    
    p1 = Passageiro("Robson Junior", "123.456.789-10")
    p2 = Passageiro("Fabricio Osorio", "987.654.321-00")
    p3 = Passageiro("Heitor Ferreira", "111.222.333-44")
    p1.adicionar_bagagem(Bagagem("Mala média", 20.5))
    p1.adicionar_bagagem(Bagagem("Mochila", 7.2))
    p2.adicionar_bagagem(Bagagem("Mala grande", 30.0))
    
    f1 = Funcionario("Darth Vader", "000.111.222-33", "Piloto", "DV123")
    f2 = Funcionario("Luke Skywalker", "444.555.666-77", "Co-piloto", "LS456")
    f3 = Funcionario("Princesa Leia", "888.999.000-11", "Comissária", "LO789")
    
    a1 = Auditor("Yoda")
    
    vgol1.adicionar_passageiro(p1)
    vgol1.adicionar_passageiro(p2)
    vgol2.adicionar_passageiro(p3)
    
    vgol1.adicionar_tripulante(f1)
    vgol1.adicionar_tripulante(f2)
    vgol1.adicionar_tripulante(f3)
    
    vgol1.listar_passageiros()
    p1.listar_bagagens()
    p2.listar_bagagens()
    p3.listar_bagagens()
    
    vgol1.listar_tripulacao()
    vgol2.listar_tripulacao()
    a1.logar_entrada()
    a1.auditar_voo(vgol1)
    a1.auditar_voo(vgol2)




