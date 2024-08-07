# SHOW DO CENZÃO

Este projeto é uma implementação de um jogo de perguntas e respostas inspirado em shows de quiz. O objetivo é responder corretamente às perguntas para ganhar prêmios. O jogo foi desenvolvido em Python utilizando a biblioteca `customtkinter` para criar a interface gráfica.

## Funcionalidades

- **Perguntas e Respostas**: O jogo apresenta uma série de perguntas com múltiplas escolhas.
- **Verificação de Respostas**: As respostas são verificadas e o jogador recebe feedback imediato sobre a correção.
- **Pular Pergunta**: O jogador pode pular uma pergunta durante o jogo.
- **Ajuda**: O jogador pode eliminar duas opções erradas como forma de ajuda.
- **Parar Jogo**: O jogador pode parar o jogo a qualquer momento e receber o prêmio acumulado até a pergunta atual.
- **Reiniciar Jogo**: Após o término do jogo, o jogador pode reiniciar e começar do início.

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/show-do-cenzao.git
   cd show-do-cenzao
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   .\venv\Scripts\activate    # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install customtkinter
   ```

## Uso

Para iniciar o jogo, execute o script `show_do_cenzao.py`:

```bash
python show_do_cenzao.py
```

## Estrutura do Projeto

- `show_do_cenzao.py`: Script principal que contém a lógica do jogo e a interface gráfica.
- `README.md`: Este arquivo.

## Funcionalidades em Detalhes

### Verificação de Resposta

A função `verificar_resposta` verifica se a resposta selecionada pelo jogador é correta e fornece feedback visual imediato.

### Atualização de Pergunta

A função `atualizar_pergunta` atualiza a pergunta e as opções de resposta na interface.

### Pular Pergunta

A função `pular_pergunta` permite ao jogador pular a pergunta atual.

### Ajuda

A função `usar_ajuda` desativa duas opções erradas, deixando apenas duas opções possíveis.

### Parar Jogo

A função `parar_jogo` permite ao jogador parar o jogo e receber o prêmio acumulado.

### Reiniciar Jogo

A função `reiniciar_jogo` reinicia o jogo do começo.

## Contribuição

Contribuições são bem-vindas! 
