from ..models import Pregao

class Tabela:
    def __init__(self,pregao: Pregao, empenhado, capacidade, percent) :
        self.pe = pregao.pregao
        self.homologado = f"R$ {pregao.saldo_homologado:_.2f}".replace('.',',').replace('_','.')
        self.empenhado = f"R$ {empenhado:_.2f}".replace('.',',').replace('_','.')
        self.capacidade = f"R$ {capacidade:_.2f}".replace('.',',').replace('_','.') 
        self.percent = F'{percent}%'
    
    
    def __str__(self) -> str:
        return self.pe
