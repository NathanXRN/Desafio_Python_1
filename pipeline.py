import pandas as pd 
import time 
from datetime import datetime
from main import carregar_df
import erros
import relatorio_individual
import kpis 

class ProcessadorDados:
    def __init__(self):
        self.df = None 
        self.inicio_execucao = None 
        self.logs = [] 

    def registrar_log(self, mensagem): 
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_mensagem = f"[{timestamp}] {mensagem}" 
        print(log_mensagem)
        self.logs.append(log_mensagem) 

    def carregar_dados(self):
        try:
            self.registrar_log("Carregando dados do arquivo CSV...")
            self.df = carregar_df()
            self.registrar_log(f"Dados carregados com sucesso! Total: {len(self.df)} registros")
            return True 
        except Exception as e:
            self.registrar_log(f"Erro ao carregar dados: {e}")
            return False 
    
    def processar_erros(self):
        try:
            self.registrar_log("Iniciando validação de erros...")
            erros.validacao_erros(self.df)
            self.registrar_log("Arquivo de erros processado!")
            return True 
        except Exception as e:
            self.registrar_log(f"Erro no processamento de erros: {e}")
            return False 
    
    def gerar_relatorio_validos(self):
        try:
            self.registrar_log("Gerando relatório de registros válidos...")
            df_validos = relatorio_individual.relatorio(self.df)
            self.registrar_log(f"Relatório gerado! Registros válidos: {len(df_validos) if df_validos is not None else 0}")
            return True
        except Exception as e:
            self.registrar_log(f"Erro na geração do relatório: {e}")
            return False
    
    def calcular_kpis(self):
        try:
            self.registrar_log("Calculando KPIs...")
            kpis.metricas(self.df)
            self.registrar_log("KPIs calculados e salvos!")
            return True 
        except Exception as e:
            self.registrar_log(f"Erro no cálculo de KPIs: {e}")
            return False
        
    def executar_pipeline(self):
        self.inicio_execucao = time.time()
        
        print("=" * 70)
        print("PIPELINE DE PROCESSAMENTO DE DADOS - INICIADO")
        print("=" * 70)
        
        processos = [
            ("Carregamento de Dados", self.carregar_dados),
            ("Validação de Erros", self.processar_erros),
            ("Relatório de Válidos", self.gerar_relatorio_validos), 
            ("Cálculo de KPIs", self.calcular_kpis)
        ]
        
        sucessos = 0
        total_processos = len(processos)
        
        for i, (nome, funcao) in enumerate(processos, 1):
            self.registrar_log(f"Etapa {i}/{total_processos}: {nome}")
            
            if funcao():
                sucessos += 1
            else:
                self.registrar_log(f"Etapa '{nome}' falhou.")
                if i == 1: 
                    self.registrar_log("Pipeline interrompida - falha no carregamento de dados")
                    break
        
        tempo_total = time.time() - self.inicio_execucao
        
        print("\n" + "=" * 70)
        print("RESUMO DA EXECUÇÃO")
        print("=" * 70)
        print(f"Tempo total de execução: {tempo_total:.2f} segundos")
        print(f"Processos executados com sucesso: {sucessos}/{total_processos}")
        
        if sucessos == total_processos:
            print("PIPELINE CONCLUÍDO COM SUCESSO!")
            print("\n Arquivos gerados:")
            print("   • erros.csv")
            print("   • relatorio_individual.csv")
            print("   • kpis.json")
        else:
            print("Pipeline concluído com algumas falhas")
        
        print("=" * 70)

def main():
    processador = ProcessadorDados()
    processador.executar_pipeline() 

if __name__ == "__main__":
    main()