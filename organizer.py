import os
import time
import shutil
import ctypes
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURAÇÕES DINÂMICAS ---
# Descobre a pasta onde o script está, seja qual for o PC ou pasta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'organizer.log')

TRACK_DIR = os.path.expanduser("~/Downloads")
TEMP_DIR = os.environ.get('TEMP')
CLEANUP_INTERVAL = 604800  # 7 dias

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
    try:
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 1 | 2 | 4)
        logging.info("SYSTEM: Reciclagem esvaziada.")
    except Exception as e:
        logging.error(f"SYSTEM ERROR (Trash): {e}")

def cleanup_temp():
    if not TEMP_DIR or not os.path.exists(TEMP_DIR): return
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
        except Exception: continue
    if count > 0: logging.info(f"SYSTEM: Temp limpo ({count} itens).")

class MoveHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.process_file(event.src_path)

    def process_file(self, file_path):
        filename = os.path.basename(file_path)
        if not filename: return 
        
        try: extension = os.path.splitext(filename)[1].lower()
        except Exception: return

        if extension in [".crdownload", ".part", ".tmp"] or filename.startswith("."):
            return

        if extension in DEST_MAP:
            dest_folder = os.path.join(TRACK_DIR, DEST_MAP[extension])
            os.makedirs(dest_folder, exist_ok=True)
            
            time.sleep(1) # Pequena pausa para garantir acesso ao ficheiro
            
            final_path = os.path.join(dest_folder, filename)
            if os.path.exists(final_path):
                name, ext = os.path.splitext(filename)
                final_path = os.path.join(dest_folder, f"{name}_{int(time.time())}{ext}")

            try:
                if os.path.exists(file_path): 
                    os.rename(file_path, final_path)
                    logging.info(f"MOVED: {filename} -> {DEST_MAP[extension]}")
            except Exception as e:
                logging.error(f"MOVE ERROR: {filename} -> {e}")

# --- NOVA FUNÇÃO PARA ARRUMAR AO INICIAR ---
def organize_existing_files(handler):
    logging.info("STARTUP: A verificar ficheiros já existentes...")
    if not os.path.exists(TRACK_DIR): return
    
    for filename in os.listdir(TRACK_DIR):
        file_path = os.path.join(TRACK_DIR, filename)
        if os.path.isfile(file_path):
            handler.process_file(file_path)

if __name__ == "__main__":
    event_handler = MoveHandler()
    
    # 1. Limpeza de Sistema
    empty_trash()
    cleanup_temp()
    
    # 2. Arrumar ficheiros que já lá estavam (A CORREÇÃO QUE FALTAVA)
    organize_existing_files(event_handler)

    # 3. Iniciar monitorização
    observer = Observer()
    observer.schedule(event_handler, TRACK_DIR, recursive=False)
    observer.start()

    logging.info("SERVICE: Organizador iniciado e a monitorizar.")
    last_cleanup = time.time()
    
    try:
        while True:
            time.sleep(60)
            if time.time() - last_cleanup > CLEANUP_INTERVAL:
                empty_trash()
                cleanup_temp()
                last_cleanup = time.time()
    except Exception as e:
        logging.error(f"CRITICAL: {e}")
        observer.stop()
    observer.join()