# PinDiceDistance

Gerando alguns fractais com aleatoriedade

# O algoritmo

Defina uma lista `L` de pivôs na tela;

Defina uma variável `p` que armazenará o último pivô sorteado;

Defina uma variável `x` que armazenará o último ponto desenhado;

Defina uma variável `k` que armazenará um fator;

Caso `L` esteja vazio, não faça nada;

Caso `p` seja`Null`, `p = L[0]`;

Caso `x` seja`Null`, `x = [p.x, p.y]`;

Selecione aleatoriamente um elemento do `L` diferente de `p` e armazene em `c`;

Calcule `dx` = `k * (c.x - p[0])`;
Calcule `dy` = `k * (c.x - p[0])`;

Faça `x = [p.x + dx, p.y + dy]`;
Faça `p = c`;

Desenhe `x`;

Execute tudo novamente;

## A implementação

```python
def draw_dot(self):
    if len(self.pivots) == 0:
        return 
    
    if not self.last_pivot:
        self.last_pivot = self.pivots[0]

    if not self.last_dot:
        self.last_dot = (self.last_pivot.x, self.last_pivot.y)

    pivots_choosable = [ p for p in self.pivots if p != self.last_pivot ]

    choiced_pivot = random.choice(pivots_choosable)

    dx = self.factor * (choiced_pivot.x - self.last_dot[0]) 
    dy = self.factor * (choiced_pivot.y - self.last_dot[1])

    dot_position = (
        self.last_dot[0] + dx, 
        self.last_dot[1] + dy
    )

    pygame.draw.circle(
        self.display, 
        random.choice(self.dot_colors), 
        dot_position,
        self.dot_size
    )

    self.last_pivot = choiced_pivot
    self.last_dot = dot_position
```

# Como executar na sua máquina? 

Você precisará instalar o [poetry](https://python-poetry.org) caso não tenha.

Clone o repositório
`git clone https://github.com/pab-h/PinDiceDistance`

Execute no respositório clonado
`poetry init`

Execute o arquivo `main.py`
`poetry run python pindicedistance/main.py`

# Comandos

1. Clique direito do mouse: Adiciona um pivô na tela
1. 'a': Ativa o modo automático (Coloca pontos automáticamente)
1. 's': Desativa o modo automático 
1. 'space': Coloca um ponto na tela

# O Arquivo de configuração 

Altere-o conforme o necessário. Os campos são autoexplicativos 

```json
{
    "pivot": "./assets/pivot.png",
    "dot": {
        "size": 1,
        "colors": [
            [121, 63, 223],
            [112, 145, 245],
            [151, 255, 244],
            [255, 253, 140]
        ]
    },
    "factor": 0.5,
    "fps": 120,
    "display": [600, 600]
}
```

# Resultados

![triangle](/assets/triangle.jpeg)
![square](/assets/square.jpeg)
![pentagon](/assets/pentagon.jpeg)
![hexagon](/assets/hexagon.jpeg)
