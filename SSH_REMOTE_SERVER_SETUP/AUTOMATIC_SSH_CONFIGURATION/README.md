# 🚀 AUTOMATIC SSH CONFIGURATION

**AUTOMATIC SSH CONFIGURATION** é uma aplicação Python de código aberto que gera automaticamente chaves SSH e configura o arquivo `~/.ssh/config` para facilitar conexões seguras com servidores remotos.

Ideal para quem quer **economizar tempo** e **evitar erros** ao configurar acessos SSH manualmente!

---

## 📋 O que essa aplicação faz?

- Gera **duas chaves SSH** novas (sem senha) na pasta `~/.ssh`.
- Atualiza automaticamente o arquivo `~/.ssh/config`, adicionando entradas para conexão rápida a servidores.
- Simula uma barra de progresso para uma experiência mais amigável.

Assim, você pode se conectar ao seu servidor apenas digitando:

```bash
ssh servidor1
```

ou

```bash
ssh servidor2
```

**sem precisar decorar o IP** ou especificar a chave manualmente toda vez.

---

## 🛠️ Como funciona internamente?

O programa:

1. **Pede o IP** público do servidor.
2. **Pede o nome** que você deseja dar para duas novas chaves SSH.
3. **Cria as chaves** usando o `ssh-keygen`.
4. **Atualiza o arquivo `~/.ssh/config`**, adicionando as configurações corretas.
5. **Exibe uma barra de progresso** durante o processo para mostrar que está tudo indo bem!

---

## 💻 Como usar?

### Pré-requisitos

- Python 3 instalado.
- O comando `ssh-keygen` disponível no sistema (vem instalado por padrão em Linux e MacOS, e também no Windows com WSL ou Git Bash).

### Rodando a aplicação

1. Clone este repositório ou copie o arquivo Python.

2. No terminal, execute:

```bash
python automatic_ssh_configuration.py
```

3. Siga as instruções:
   - Digite o IP público do servidor.
   - Escolha os nomes para as chaves SSH.

4. Pronto! Suas chaves serão criadas e configuradas.

---

## 📂 Estrutura dos Arquivos Criados

- **Chaves SSH**: serão criadas em `~/.ssh/` (ex: `key1`, `key1.pub`, `key2`, `key2.pub`).
- **Arquivo de Configuração**: será atualizado em `~/.ssh/config` com algo parecido com:

```text
Host servidor1
    HostName seu-ip-publico
    User ubuntu
    IdentityFile ~/.ssh/key1

Host servidor2
    HostName seu-ip-publico
    User ubuntu
    IdentityFile ~/.ssh/key2
```

---

## 🧠 Tecnologias usadas

- **Python** (bibliotecas nativas):
  - `os`
  - `subprocess`
  - `time`

---

## 🤝 Contribuição

Contribuições são muito bem-vindas!  
Se quiser melhorar o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

## 📃 Licença

Este projeto é de código aberto, sob a seguinte licença personalizada:

Licença de Uso - Automatic SSH Configuration

Copyright (c) 2025 Felipe Thales

Este software e toda a sua documentação associada ("Software") são fornecidos gratuitamente para uso pessoal e educacional, sob as seguintes condições:

- É permitido usar, copiar, modificar e distribuir este Software, desde que não seja utilizado para fins comerciais ou lucrativos.

- É estritamente proibido vender, sublicenciar ou redistribuir o Software, ou quaisquer trabalhos derivados, para fins comerciais.

- O aviso de copyright acima e esta permissão devem ser incluídos em todas as cópias ou partes substanciais do Software.

O Software é fornecido "no estado em que se encontra", sem qualquer tipo de garantia expressa ou implícita, incluindo, mas não se limitando a garantias de comercialização, adequação a um propósito específico e não violação. Em nenhum caso os autores serão responsáveis por quaisquer danos decorrentes do uso do Software.

---

## ✨ Nota do autor

Este projeto foi criado para simplificar a vida de quem precisa trabalhar com múltiplas conexões SSH de forma rápida e segura.

Se isso te ajudou, ⭐ marque este projeto e compartilhe!
