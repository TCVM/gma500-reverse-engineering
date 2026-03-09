import subprocess
import datetime
import os
import sys

def create_log_entry(session_name, content):
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"logs/{date}_{session_name}.md"
    
    template = f"""# Session: {session_name}
**Date:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}

## Commands & Output
```
{content}
```

## Findings
<!-- Completar manualmente después de la sesión -->

## Questions for Claude
<!-- Preguntas complejas para pasar al chat -->

## Next Steps
<!-- Qué hacer en la próxima sesión -->
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"Log creado: {filename}")
    return filename

def auto_commit(filename, session_name):
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"log: {session_name}"])
    subprocess.run(["git", "push", "origin", "main"])
    print("Pusheado a GitHub")

if __name__ == "__main__":
    session_name = sys.argv[1] if len(sys.argv) > 1 else "session"
    print(f"Pegá el contenido de la sesión (Ctrl+Z para terminar):")
    content = sys.stdin.read()
    filename = create_log_entry(session_name, content)
    
    response = input("¿Pushear a GitHub? (s/n): ")
    if response.lower() == 's':
        auto_commit(filename, session_name)