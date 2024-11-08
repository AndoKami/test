import subprocess

def set_git_user():
    username = input("Entrez votre nom d'utilisateur Git: ")
    email = input("Entrez votre email Git: ")
    subprocess.run(["git", "config", "--global", "user.name", username])
    subprocess.run(["git", "config", "--global", "user.email", email])

def git_add():
    add_target = input("Entrez '.' pour ajouter tout ou le chemin du fichier/dossier : ")
    subprocess.run(["git", "add", add_target])

def git_commit():
    message = input("Entrez le message de commit : ")
    subprocess.run(["git", "commit", "-m", message])

def git_push():
    branch = input("Entrez le nom de la branche : ")
    subprocess.run(["git", "push", "origin", branch])

def main():
    set_git_user()
    git_add()
    git_commit()
    git_push()

if __name__ == "__main__":
    main()
