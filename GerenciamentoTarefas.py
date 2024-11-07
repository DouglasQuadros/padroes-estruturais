# 1. Sub-sistema: Tarefa
class Tarefa:
    def __init__(self, nome):
        self.nome = nome
        self.concluida = False

    def marcar_como_concluida(self):
        self.concluida = True
        print(f"Tarefa '{self.nome}' concluída!")

    def __str__(self):
        return f"{'[Concluída]' if self.concluida else '[Pendente]'} {self.nome}"

# 2. Sub-sistema: Armazenamento de Tarefas
class ArmazenamentoTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f"Tarefa '{tarefa.nome}' adicionada!")

    def listar_tarefas(self):
        print("Tarefas:")
        for tarefa in self.tarefas:
            print(tarefa)

# 3. Sub-sistema: Sistema de Notificação
class SistemaNotificacao:
    def enviar_notificacao(self, tarefa):
        print(f"Notificação: A tarefa '{tarefa.nome}' foi concluída!")

# 4. Facade: SistemaGerenciamentoTarefas (Padrão Facade)
class SistemaGerenciamentoTarefas:
    def __init__(self):
        self.armazenamento = ArmazenamentoTarefas()
        self.notificacao = SistemaNotificacao()

    def adicionar_tarefa(self, nome_tarefa):
        tarefa = Tarefa(nome_tarefa)
        self.armazenamento.adicionar_tarefa(tarefa)

    def concluir_tarefa(self, nome_tarefa):
        for tarefa in self.armazenamento.tarefas:
            if tarefa.nome == nome_tarefa and not tarefa.concluida:
                tarefa.marcar_como_concluida()
                self.notificacao.enviar_notificacao(tarefa)
                break
        else:
            print(f"Tarefa '{nome_tarefa}' não encontrada ou já concluída!")

    def listar_tarefas(self):
        self.armazenamento.listar_tarefas()

# 5. Testes Unitários (usando unittest)
import unittest

class TestSistemaGerenciamentoTarefas(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaGerenciamentoTarefas()

    def test_adicionar_e_listar_tarefas(self):
        self.sistema.adicionar_tarefa("Comprar leite")
        self.sistema.adicionar_tarefa("Estudar Python")
        self.sistema.listar_tarefas()
        self.assertEqual(len(self.sistema.armazenamento.tarefas), 2)

    def test_concluir_tarefa(self):
        self.sistema.adicionar_tarefa("Fazer compras")
        self.sistema.concluir_tarefa("Fazer compras")
        self.assertTrue(self.sistema.armazenamento.tarefas[0].concluida)

    def test_concluir_tarefa_inexistente(self):
        self.sistema.adicionar_tarefa("Ler livro")
        self.sistema.concluir_tarefa("Ir ao cinema")
        self.assertFalse(self.sistema.armazenamento.tarefas[0].concluida)

# 6. Classe principal para rodar o código (Exemplo de uso)
if __name__ == "__main__":
    # Exemplo de uso
    sistema = SistemaGerenciamentoTarefas()

    # Adicionar Tarefas
    sistema.adicionar_tarefa("Estudar Design Patterns")
    sistema.adicionar_tarefa("Fazer exercício de matemática")
    sistema.adicionar_tarefa("Ler capítulo de livro")

    # Listar Tarefas
    sistema.listar_tarefas()

    # Concluir Tarefa
    sistema.concluir_tarefa("Estudar Design Patterns")
    sistema.concluir_tarefa("Fazer exercício de matemática")

    # Listar novamente para ver as mudanças
    sistema.listar_tarefas()

    # Rodar os testes unitários
    unittest.main(argv=[''], exit=False)
