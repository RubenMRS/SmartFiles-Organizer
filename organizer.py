import os
import time
import shutil
import ctypes
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURAÇÕES ---
TRACK_DIR = os.path.expanduser("~/Downloads")
TEMP_DIR = os.environ.get('TEMP')
LOG_FILE = 'C:/Users/Rúben/Desktop/SmartFiles/organizer.log'
CLEANUP_INTERVAL = 604800  # 7 dias em segundos (60 * 60 * 24 * 7)

DEST_MAP = {
    ".pdf": "Documentos/PDFs",
    ".txt": "Documentos/Texto",
    ".docx": "Documentos/Office/Word",
    ".odt": "Documentos/Office/Word",
    ".xlsx": "Documentos/Office/Excel",
    ".csv" : "Documentos/Office/Excel",
    ".odp": "Documentos/Office/PowerPoint",
    ".pptx": "Documentos/Office/PowerPoint",
    ".zip": "Arquivos/Zip",
    ".rar": "Arquivos/Rar",
    ".7z" : "Arquivos/Zip",
    ".jpg": "Multimedia/Imagens",
    ".png": "Multimedia/Imagens",
    ".jpeg": "Multimedia/Imagens",
    ".svg" : "Multimedia/Imagens",
    ".tiff": "Multimedia/Imagens",
    ".mp4": "Multimedia/Videos",
    ".gif": "Multimedia/Videos",
    ".avi": "Multimedia/Videos",
    ".mkv": "Multimedia/Audio",
    ".mp3": "Multimedia/Audio",
    ".wav": "Multimedia/Audio",
    ".exe": "Programas/Installers",
    ".dmg": "Programas/Installers",
    ".msi": "Programas/Installers",
    ".msix": "Programas/Installers",
}

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def empty_trash():
    """Limpa a Reciclagem silenciosamente via API do Windows"""
    try:
        # Flags: 1=NoConfirmation, 2=NoProgressUI, 4=NoSound
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 1 | 2 | 4)
        logging.info("SYSTEM: Reciclagem esvaziada (Manutenção Semanal).")
    except Exception as e:
        logging.error(f"SYSTEM ERROR (Trash): {e}")

def cleanup_temp():
    """Limpa a pasta temporária do Windows"""
    if not TEMP_DIR or not os.path.exists(TEMP_DIR):
        return
    
    count = 0
    for item in os.listdir(TEMP_DIR):
        item_path = os.path.join(TEMP_DIR, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
                count += 1
            elif os.path.is_directory(item_path):
                shutil.rmtree(item_path)
                count += 1
        except Exception:
            continue # Ignora ficheiros em uso (normal no Windows)
            
    if count > 0:
        logging.info(f"SYSTEM: Pasta Temp limpa ({count} ficheiros removidos).")

class MoveHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.process_file(event.src_path)

    def process_file(self, file_path):
        filename = os.path.basename(file_path)
        # Proteção contra erros de leitura imediata
        if not filename: return 
        
        try:
            extension = os.path.splitext(filename)[1].lower()
        except Exception:
            return

        # Ignorar temporários e ficheiros ocultos
        if extension in [".crdownload", ".part", ".tmp"] or filename.startswith("."):
            return

        if extension in DEST_MAP:
            dest_folder = os.path.join(TRACK_DIR, DEST_MAP[extension])
            os.makedirs(dest_folder, exist_ok=True)
            
            # Delay crucial para downloads acabarem de escrever no disco
            time.sleep(2)
            
            final_path = os.path.join(dest_folder, filename)
            
            # Gestão de duplicados
            if os.path.exists(final_path):
                name, ext = os.path.splitext(filename)
                timestamp = int(time.time())
                final_path = os.path.join(dest_folder, f"{name}_{timestamp}{ext}")

            try:
                # Tenta mover com tratamento de erros de permissão
                if os.path.exists(file_path): 
                    os.rename(file_path, final_path)
                    logging.info(f"MOVED: {filename} -> {DEST_MAP[extension]}")
            except Exception as e:
                logging.error(f"MOVE ERROR: {filename} -> {e}")

if __name__ == "__main__":
    # Executa a limpeza imediatamente ao iniciar o script
    empty_trash()
    cleanup_temp()

    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, TRACK_DIR, recursive=False)
    observer.start()

    logging.info("SERVICE: Organizador iniciado.")
    last_cleanup = time.time()
    
    try:
        while True:
            # Verifica a cada minuto se já passou 1 semana
            time.sleep(60) 
            
            if time.time() - last_cleanup > CLEANUP_INTERVAL:
                empty_trash()
                cleanup_temp()
                last_cleanup = time.time()
                
    except Exception as e:
        logging.error(f"CRITICAL FAULT: {e}")
        observer.stop()
    
    observer.join()