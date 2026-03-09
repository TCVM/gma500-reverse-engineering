import subprocess
import datetime
import os
import sys

REPO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def prompt_questions():
    print("\n--- PREGUNTAS PARA CLAUDE ---")
    print("Ingresá preguntas que surgieron en esta sesión (Enter vacío para terminar):")
    questions = []
    while True:
        q = input(f"Pregunta {len(questions)+1}: ")
        if not q:
            break
        questions.append(q)
    return questions

def prompt_findings():
    print("\n--- HALLAZGOS DE LA SESIÓN ---")
    print("Ingresá hallazgos importantes (Enter vacío para terminar):")
    findings = []
    while True:
        f = input(f"Hallazgo {len(findings)+1}: ")
        if not f:
            break
        findings.append(f)
    return findings

def create_log(session_name, output, findings, questions, next_steps):
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = os.path.join(REPO_PATH, f"logs/{date}_{session_name}.md")

    questions_md = "\n".join([f"- {q}" for q in questions]) if questions else "- Ninguna"
    findings_md = "\n".join([f"- {f}" for f in findings]) if findings else "- Ninguna"
    next_md = "\n".join([f"- {s}" for s in next_steps]) if next_steps else "- Pendiente"

    template = f"""# Sesión: {session_name}
**Fecha:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}

## Output de terminal
```
{output}
```

## Hallazgos
{findings_md}

## Preguntas para Claude
{questions_md}

## Próximos pasos
{next_md}
"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"\nLog creado: {filename}")
    return filename

def auto_commit(filename, session_name):
    os.chdir(REPO_PATH)
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"log: {session_name} - {datetime.datetime.now().strftime('%Y-%m-%d')}"])
    subprocess.run(["git", "push", "origin", "main"])
    print("Pusheado a GitHub")

if __name__ == "__main__":
    session_name = sys.argv[1] if len(sys.argv) > 1 else input("Nombre de sesión: ")
    
    print("Pegá el output de la terminal (Ctrl+Z + Enter para terminar):")
    output = sys.stdin.read()
    
    findings = prompt_findings()
    questions = prompt_questions()
    
    print("\n--- PRÓXIMOS PASOS ---")
    print("Ingresá próximos pasos (Enter vacío para terminar):")
    next_steps = []
    while True:
        s = input(f"Paso {len(next_steps)+1}: ")
        if not s:
            break
        next_steps.append(s)

    filename = create_log(session_name, output, findings, questions, next_steps)

    response = input("\n¿Pushear a GitHub? (s/n): ")
    if response.lower() == 's':
        auto_commit(filename, session_name)