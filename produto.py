from rich import print
from rich.panel import Panel
from rich.console import Console

console = Console()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')} "  #
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        etiqueta = Panel(conteudo, title="Produto", width=34, border_style="yellow")
        print(etiqueta)


class CarrinhoDeCompras:
    def __init__(self, catalago_produtos):
        self.itens = []
        self.catalago = catalago_produtos

    def adicionar_produto(self, nome_digitado, quantidade):
        nome_busca = nome_digitado.strip().lower()

        if nome_busca in self.catalago:
            produto = self.catalago[nome_busca]
            subtotal = produto.preco * quantidade
            self.itens.append(
                {
                    "produto": produto.nome,
                    "quantidade": quantidade,
                    "subtotal": subtotal,
                }
            )

    def exibir_total(self):
        if not self.itens:
            print("[red] O carrinho está vazio![/red]", title="Resumo", width=40)
            return

        conteudo_recibo = ""
        total = 0
        for item in self.itens:
            conteudo_recibo += f"{item['quantidade']}x {item['produto']} - R$ {item['subtotal']:,.2f}\n"
            total += item["subtotal"]

        conteudo_recibo += f"{'-' *35}\n"
        conteudo_recibo += f"[black] TOTAL A PAGAR R$ {total:,.2f} [/black]"

        recibo = Panel(
            conteudo_recibo, title="Recibo de compra", width=40, border_style="purple"
        )
        print(recibo)


p1 = Produto("Teclado Gamer", 500)
p2 = Produto("Notebook Gamer", 2000)
p3 = Produto("Computador Gamer", 4000)
p4 = Produto("Monitor Gamer", 2000)


p1.etiqueta()
p2.etiqueta()
p3.etiqueta()
p4.etiqueta()


catalago_sistema = {
    "teclado Gamer": p1,
    "notebook gamer": p2,
    "computador gamer": p3,
    "monitor gamer": p4,
}


carrinho = CarrinhoDeCompras(catalago_sistema)


while True:

    produto_escolhido = console.input(
        "[blue] Digite o nome do produto [/blue]ou [red]finalizar[/red] para fechar: "
    )

    if produto_escolhido.strip().lower() == "finalizar":
        break

    try:
        quantidade = int(
            console.input(
                f"Quantas unidades de  [blue]{produto_escolhido}[/blue] você quer?  "
            )
        )
        if quantidade <= 0:
            print(f"[red] Quantidade deve ser maior do que zero![/red]")
            continue
    except ValueError:
        print(f"[red] Erro: DEVE ser digitado apenas NÚMEROS!")
        continue

    carrinho.adicionar_produto(produto_escolhido, quantidade)


carrinho.exibir_total()
