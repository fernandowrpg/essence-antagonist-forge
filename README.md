# Essence Antagonist Forge

Ferramenta para criar antagonistas de **Exalted: Essence** (Onyx Path, 2023):

- **Templates** de stats por Essence do Círculo (Extra, Padrão, Elite, Chefe, Nêmesis), tabelas de grupos de batalha e blocos oficiais do livro para comparação.
- **Biblioteca** com 532 Charms, artes marciais, feitiços e rituais, 241 modos por tipo de Exaltado e 94 qualidades de antagonista, com resumos em inglês e português (alternância EN/PT na barra superior).
- **Inimigos** salvos automaticamente no navegador, vários ao mesmo tempo, organizados em **pastas**, com prévia fixa (acima, abaixo, esquerda ou direita).
- **Grupos de batalha:** marque a ficha como grupo de batalha e escolha Size e Drill; a vida segue a tabela de Size e a prévia mostra debandada e qualidades grátis. No Foundry a ficha sai com `battlegroup`, `size` e `drill` preenchidos, e o sistema calcula Drill e Overwhelming. No JSON: `"battlegroup": true, "size": 2, "drill": 2` (0 Poor … 3 Elite).
- **Importação em lote:** cole um inimigo `{...}`, uma lista `[...]` ou uma pasta `{"folder": "...", "enemies": [...]}`, ou selecione vários arquivos `.json` de uma vez.
- **Exportação para Foundry VTT**, sistema *Exalted Essence* 2.0.11 (Foundry 13): macro de script que cria o NPC com stats, pools, arma, qualidades e Charms como itens, ou JSON para *Import Data*. A **macro da pasta** cria todos os NPCs da pasta de uma vez, dentro de uma pasta de Actors com o mesmo nome.

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
