# 📂 SmartFiles Organizer

> **Automação Inteligente de Ficheiros para Windows**
> O teu PC arruma-se a si próprio. Organiza downloads e limpa o lixo automaticamente.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square)

## 🚀 O que faz?

Este script é um "mordomo digital" que corre silenciosamente em background:

1.  **Organizador em Tempo Real:**
    * Monitoriza a pasta **Downloads**.
    * Move ficheiros instantaneamente para pastas organizadas (`Documentos`, `Imagens`, `Installers`, etc.).
    * Gere nomes duplicados automaticamente (adiciona data/hora se o ficheiro já existir).
    * Ignora downloads incompletos (`.crdownload`, `.part`) para evitar erros.

2.  **Manutenção Automática (Auto-Cleaner):**
    * Uma vez por semana (a cada 7 dias), executa uma limpeza profunda:
        * 🗑️ Esvazia a **Reciclagem** (sem janelas de confirmação).
        * 🧹 Limpa ficheiros inúteis da pasta **%TEMP%** do Windows.

3.  **100% Portátil:**
    * Não requer configuração de caminhos. Ele sabe onde está e cria os logs na própria pasta.

---

## 🛠️ Instalação Rápida

### 1. Preparar o Ambiente
Certifica-te que tens o **Python** instalado. Abre esta pasta no terminal (`cmd` ou `PowerShell`) e corre:

```powershell
# Cria o ambiente virtual (recomendado)
python -m venv venv

# Ativa o ambiente
.\venv\Scripts\activate

# Instala a única dependência necessária
pip install watchdog
2. Iniciar (Modo Silencioso)
Para ligar o script sem deixar janelas pretas abertas, usa o ficheiro run_smartfiles.bat incluído neste projeto.

Basta clicar duas vezes no ficheiro .bat.

Nada vai aparecer no ecrã (é intencional).

Verifica o ficheiro organizer.log para confirmar que iniciou: SERVICE: Organizador iniciado.

3. Automatizar no Arranque
Para que o SmartFiles inicie sempre que ligas o PC:

Cria um Atalho do ficheiro run_smartfiles.bat.

Prime Win + R no teclado, escreve shell:startup e dá Enter.

Move o atalho que criaste para dentro dessa pasta.

⚙️ Configuração (Opcional)
O script funciona "out-of-the-box", mas podes editar o ficheiro organizer.py para personalizar:

DEST_MAP: Define para onde vai cada tipo de ficheiro.

Ex: ".pdf": "Documentos/PDFs"

CLEANUP_INTERVAL: Frequência da limpeza da reciclagem em segundos (Default: 604800 = 7 dias).

📝 Logs & Debugging
Toda a atividade fica registada no ficheiro organizer.log na mesma pasta do script.

MOVED: Ficheiro organizado com sucesso.

SYSTEM: Limpeza de lixo executada.

ERROR: Alguma coisa correu mal (ex: ficheiro aberto noutro programa).

🛑 Como Parar
Como o script corre em background (modo stealth), para o desligar:

Abre o Gestor de Tarefas (Ctrl + Shift + Esc).

Vai ao separador Detalhes.

Termina a tarefa pythonw.exe.

Autor: Rúben