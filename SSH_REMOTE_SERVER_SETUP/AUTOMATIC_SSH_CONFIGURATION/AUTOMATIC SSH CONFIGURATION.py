import os
import subprocess
import time

def criar_chave(nome_chave):
    caminho_ssh = os.path.expanduser("~/.ssh")
    os.makedirs(caminho_ssh, exist_ok=True)

    chave_privada = os.path.join(caminho_ssh, nome_chave)
    chave_publica = chave_privada + ".pub"

    subprocess.run([
        "ssh-keygen",
        "-t", "rsa",
        "-b", "4096",
        "-f", chave_privada,
        "-N", ""  # <- Gera sem senha
    ], check=True)

    return chave_privada, chave_publica

def atualizar_arquivo_config(alias, ip, caminho_chave):
    caminho_ssh = os.path.expanduser("~/.ssh")
    caminho_config = os.path.join(caminho_ssh, "config")

    # Corrige barras no caminho do Windows
    caminho_chave_corrigido = caminho_chave.replace(os.sep, '/')

    nova_entry = f"""Host {alias}
    HostName {ip}
    User ubuntu
    IdentityFile {caminho_chave_corrigido}
"""

    with open(caminho_config, "a") as f:
        f.write(nova_entry.strip() + "\n")

def mostrar_progress_bar(etapas):
    print("\nConfigurando ambiente...")
    for i, etapa in enumerate(etapas, start=1):
        print(f"[{i}/{len(etapas)}] {etapa}...", end="", flush=True)
        time.sleep(1.2)  # Simula carregamento
        print(" OK")
    print("\n✅ Tudo concluído com sucesso!")

def main():
    print("=== Gerador de Chaves SSH e Configurador de Conexão ===\n")

    ip = input("Digite o IP público do servidor (ex: ec2-xx-xx-xx-xx.sa-east-1.compute.amazonaws.com): ").strip()

    chave1_nome = input("Nome da primeira chave (ex: key1): ").strip()
    chave2_nome = input("Nome da segunda chave (ex: key2): ").strip()

    alias1 = "servidor1"
    alias2 = "servidor2"

    etapas = [
        f"Gerando chave {chave1_nome}",
        f"Gerando chave {chave2_nome}",
        "Atualizando arquivo de configuração SSH (~/.ssh/config)"
    ]

    chave1_priv, _ = criar_chave(chave1_nome)
    chave2_priv, _ = criar_chave(chave2_nome)

    atualizar_arquivo_config(alias1, ip, chave1_priv)
    atualizar_arquivo_config(alias2, ip, chave2_priv)

    mostrar_progress_bar(etapas)

if __name__ == "__main__":
    main()
