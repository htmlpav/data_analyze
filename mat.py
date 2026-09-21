import sys
import subprocess

# Этот код принудительно устанавливает matplotlib в текущее активное окружение
subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
print("Готово! Перезапустите ваш редактор кода и проверьте импорт.")
