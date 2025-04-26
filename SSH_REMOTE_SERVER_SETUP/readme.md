# 🔐 Configuração de Servidor Linux Remoto com Acesso SSH Seguro

## 📘 Visão Geral

Este projeto tem como objetivo configurar um servidor Linux remoto com acesso SSH seguro, utilizando pares de chaves SSH. Também inclui a instalação opcional do Fail2Ban para proteção contra ataques de força bruta.

## ✅ Requisitos

- Conta na AWS (Amazon Web Services)
- Acesso ao terminal (PowerShell no Windows)
- Servidor com sistema operacional Linux (Sistema Operacional usado: Ubuntu 22.04)
- OpenSSH instalado no Windows (já vem por padrão no Windows 10/11)

## ⚙️ Etapas

### 1. Criar o Servidor na AWS

- Crie uma instância EC2 com sistema Linux (Ubuntu 22.04)
- Certifique-se de liberar a porta **22** no grupo de segurança (SSH)

### 2. Criar Par de Chaves SSH no Windows

No terminal local (PowerShell), execute:

```bash
ssh-keygen -t rsa -b 4096 -f C:\Users\SeuUsuario\.ssh\nome_da_sua_chave1
ssh-keygen -t rsa -b 4096 -f C:\Users\SeuUsuario\.ssh\nome_da_sua_chave2
```

> 📝 **Quando solicitado por uma passphrase, apenas pressione `Enter` para deixar em branco.**

> Esse comando criará dois arquivos:
>
> - `nome_da_sua_chave` → **chave privada**
> - `nome_da_sua_chave.pub` → **chave pública**

### 3. Subir a Chave Pública no Servidor

Conecte-se ao servidor usando a chave `.pem` fornecida pela AWS:

```bash
ssh -i C:\caminho\para\sua-chave.pem ubuntu@SEU-ENDERECO-IP
```

Dentro do servidor, execute:

```bash
mkdir -p ~/.ssh
nano ~/.ssh/authorized_keys
```

Cole o conteúdo das suas chaves públicas (`nome_da_sua_chave.pub`) e salve com `CTRL+O`, depois `CTRL+X`.

### 4. Ajustar Permissões no Servidor

Ainda dentro do servidor, execute:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

### 5. Testar a Nova Conexão SSH

No terminal local (PowerShell):

```powershell
ssh -i C:\Users\SeuUsuario\.ssh\nome_da_sua_chave ubuntu@SEU-ENDERECO-IP
```

Se tudo estiver correto, você acessará o servidor usando sua nova chave sem precisar mais da `.pem`.

### 6. (Opcional) Criar Alias de Conexão com `~/.ssh/config`

Edite o arquivo `config` em:

```
C:\Users\SeuUsuario\.ssh\config
```

Exemplo de configuração:

```ssh
Host servidor-aws
    HostName <server-ip>
    User ubuntu
    IdentityFile C:/Users/SeuUsuario/.ssh/nome_da_sua_chave1

Host servidor-aws
    HostName <server-ip2>
    User ubuntu
    IdentifyFile C:/Users/SeuUsuario/.ssh/nome_da_sua_chave2
```

Agora, para conectar:

Para conectar ao servidor-aws:

```powershell
ssh servidor-aws
```

Para conectar ao servidor-aws:

```powershell
ssh servidor-aws
```
Agora é possível conectar ao servidor AWS com as duas chaves SSH!

## 🛡️ Proteção Adicional com Fail2Ban (Opcional)

Fail2Ban ajuda a proteger seu servidor contra tentativas de acesso indevido. Para instalar:

No servidor remoto (Ubuntu):

```bash
sudo apt update && sudo apt install fail2ban -y
```

Ative o serviço:

```bash
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

✅ O Fail2Ban estará rodando e bloqueando IPs que tentarem atacar seu SSH.

> Para ver o status do Fail2Ban:

```bash
sudo systemctl status fail2ban
```

> Para checar quais IPs foram banidos:

```bash
sudo fail2ban-client status sshd
```
📄 Explicação sobre o Fail2ban:
- O Fail2ban monitora tentativas de login inválidas no SSH (e outros serviços, se você quiser) e bloqueia o IP que tentar forçar entrada errada várias vezes.
- Por padrão, ele já protege o SSH automaticamente, mas você pode configurar detalhes como quantidade de tentativas permitidas, tempo de bloqueio, IP que nunca pode ser bloqueado e muito mais coisas.

📂 Arquivo de configuração básico do Fail2ban:

```bash
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nano /etc/fail2ban/jail.local
```
Dentro do jail.local, você pode configurar, por exemplo:
```ini
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 5
bantime = 3600
```
- maxretry = 5 -> Se errar 5 vezes o login, o IP será bloqueado.
- bantime = 3600 -> Bloqueio de 1 hora (3600 segundos).
---

## Resultado:

Agora você deve conseguir:

- Entrar no seu servidor via SSH usando qualquer uma das duas chaves SSH.
- Simplificar o comando SSH usando `~/.ssh/config`.
- Ter o Fail2Ban instalado e configurado para fornecer proteção básica contra ataques de força bruta.
