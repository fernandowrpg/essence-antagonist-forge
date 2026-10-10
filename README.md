# Essence Antagonist Forge

Ferramenta para criar antagonistas de **Exalted: Essence** (Onyx Path, 2023):

- **Templates** de stats por Essence do Círculo (Extra, Padrão, Elite, Chefe, Nêmesis), tabelas de grupos de batalha e blocos oficiais do livro para comparação.
- **Biblioteca** com 532 Charms, artes marciais, feitiços e rituais, 241 modos por tipo de Exaltado e 94 qualidades de antagonista, com resumos em inglês e português (alternância EN/PT na barra superior).
- **Inimigos** salvos automaticamente no navegador, vários ao mesmo tempo, com prévia fixa (acima, abaixo, esquerda ou direita).
- **Exportação para Foundry VTT**, sistema *Exalted Essence* 2.0.11 (Foundry 13): macro de script que cria o NPC com stats, pools, arma, qualidades e Charms como itens, ou JSON para *Import Data*.

Os resumos são funções destiladas para uso com antagonistas, como o livro recomenda (p. 315). Não substituem o texto original; cada entrada indica a página.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `src/index.template.html` | Página (HTML, CSS e JS) com o marcador `__DATA__` |
| `data/exalted-essence-antagonist-library.json` | Biblioteca: templates, qualidades e Charms |
| `build.py` | Gera a build em `docs/` |
| `docs/` | Build publicada (GitHub Pages) |

## Build

```sh
python3 build.py
```

Gera `docs/index.html` (página única, sem dependências) e `docs/library.json` (a biblioteca para importar em outras ferramentas). Requer apenas Python 3.

## GitHub Pages

Em **Settings → Pages**, escolha *Deploy from a branch*, branch `main`, pasta `/docs`.

## Formato da biblioteca

```jsonc
{
  "meta": { "counts": { ... } },
  "templates": { "byEssence": { "1": { "extra": {...}, "standard": {...}, ... } }, "battleGroups": {...}, "officialBlocks": [...] },
  "qualities": [ { "id", "name", "qualityType", "page", "summary": { "en", "pt" } } ],
  "charms": [ { "id", "name", "source", "category", "ability", "prerequisites", "minEssence",
                "cost", "step", "page", "tags", "summary": { "en", "pt" },
                "modes": [ { "name", "exalts": [...], "summary": { "en", "pt" } } ] } ]
}
```

Exalted é marca registrada da Paradox Interactive AB. Projeto de fã, sem afiliação.
