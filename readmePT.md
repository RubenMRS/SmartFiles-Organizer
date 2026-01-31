# 📂 SmartFiles Organizer

> **Automação Inteligente de Ficheiros para Windows**
> O teu PC arruma-se a si próprio. Organiza downloads e limpa o lixo automaticamente.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

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

3.  **Zero Config:**
    * Não requer instalação de Python. Funciona logo após o download.

---

## 📦 Instalação (Simples)

### 1. Descarregar
Vai à secção **Releases** deste repositório e descarrega o ficheiro ZIP mais recente (ex: `SmartFiles_v1.0.zip`).
* Dentro vais encontrar o ficheiro `organizer.exe`.
* Extrai para uma pasta onde o queiras guardar (ex: `Documentos/SmartFiles`).

### 2. Iniciar
Basta clicar duas vezes no `organizer.exe`.
* **Nota:** O programa corre em "modo fantasma" (background), por isso **não vai abrir nenhuma janela**.
* Para confirmar que está a funcionar, verifica se foi criado um ficheiro `organizer.log` na mesma pasta.

> ⚠️ **Aviso sobre Antivírus (Windows Defender):**
> Como este programa é open-source e não possui um certificado digital pago da Microsoft, o Windows pode incorretamente marcar o ficheiro como suspeito ("Falso Positivo").
> * Se o Windows bloquear a execução, clica em **"Mais informações"** -> **"Executar mesmo assim"**.

---

## 🤖 Automatizar no Arranque
Para que o SmartFiles inicie sempre que ligas o PC:

1.  Clica com o botão direito no `organizer.exe` e escolhe **Criar Atalho**.
2.  Prime `Win + R` no teclado, escreve `shell:startup` e dá Enter.
3.  Move o atalho que criaste para dentro dessa pasta que abriu.

---

## ⚙️ Para Programadores (Código Fonte)
Se quiseres alterar as pastas de destino ou a lógica do script, precisas de usar a versão Python:

1.  Clona o repositório.
2.  Instala as dependências: `pip install watchdog`.
3.  Edita o ficheiro `organizer.py`.
4.  Executa com `python organizer.py`.

---

## 📝 Logs
Toda a atividade fica registada no ficheiro `organizer.log` na mesma pasta do executável.
* `MOVED`: Ficheiro organizado com sucesso.
* `SYSTEM`: Limpeza de lixo executada.

## 🛑 Como Parar
Como o script corre em background, para o desligar:
1.  Abre o **Gestor de Tarefas** (`Ctrl + Shift + Esc`).
2.  Vai ao separador **Detalhes**.
3.  Termina a tarefa **`organizer.exe`** (ou `pythonw.exe` se estiveres a usar o código fonte).

---
**Autor:** Rúben