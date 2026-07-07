Git — Resumo rápido para uso diário
1. Verificar o estado do projeto

Mostra arquivos modificados, adicionados ou pendentes.

git status
2. Inicializar Git em um projeto

Usado quando o projeto ainda não tem controle de versão.

git init
3. Adicionar arquivos para o commit

Adicionar um arquivo específico:

git add nome-do-arquivo

Adicionar todos os arquivos modificados:

git add .
4. Criar um commit

Salva uma versão do projeto com uma mensagem descritiva.

git commit -m "mensagem do commit"

Exemplo:

git commit -m "Cria tela de agendamentos"
5. Ver histórico de commits
git log

Versão resumida:

git log --oneline
6. Conectar projeto ao GitHub
git remote add origin URL_DO_REPOSITORIO

Exemplo:

git remote add origin https://github.com/usuario/repositorio.git

Verificar repositório remoto:

git remote -v
7. Enviar commits para o GitHub

Primeiro envio:

git push -u origin main

Próximos envios:

git push
8. Baixar atualizações do GitHub
git pull

Ou informando a branch:

git pull origin main
9. Clonar um repositório

Baixa um projeto existente do GitHub.

git clone URL_DO_REPOSITORIO
Branches
10. Ver branches
git branch

Ver branches locais e remotas:

git branch -a
11. Criar uma nova branch
git checkout -b nome-da-branch

Exemplo:

git checkout -b feature/agendamentos
12. Trocar de branch
git checkout nome-da-branch

Exemplo:

git checkout main

Também pode usar:

git switch nome-da-branch
13. Renomear uma branch

Se estiver dentro da branch:

git branch -m novo-nome

Se não estiver dentro dela:

git branch -m nome-antigo novo-nome
14. Enviar uma branch nova para o GitHub
git push -u origin nome-da-branch
15. Deletar uma branch local
git branch -d nome-da-branch

Forçar exclusão:

git branch -D nome-da-branch
16. Deletar uma branch remota
git push origin --delete nome-da-branch
Merge
17. Juntar uma branch na main

Entre na branch principal:

git checkout main

Atualize a main:

git pull origin main

Faça o merge:

git merge nome-da-branch

Envie para o GitHub:

git push
Fluxo correto de trabalho
Criar uma nova tarefa

Sempre comece pela branch principal atualizada:

git checkout main
git pull origin main
git checkout -b feature/nome-da-tarefa

Depois trabalhe normalmente:

git add .
git commit -m "Descreve o que foi feito"
git push -u origin feature/nome-da-tarefa
Padrão de nomes para branches

Use nomes claros e organizados:

feature/agendamentos
feature/cadastro-clientes
fix/erro-login
refactor/views
hotfix/correcao-urgente
Significado
feature/ → nova funcionalidade
fix/ → correção de erro
refactor/ → melhoria interna no código
hotfix/ → correção urgente
Comandos úteis
Ver diferenças antes do commit
git diff
Desfazer alteração em um arquivo
git checkout -- nome-do-arquivo

Ou:

git restore nome-do-arquivo
Remover arquivo da área de stage
git reset nome-do-arquivo

Ou:

git restore --staged nome-do-arquivo
Quando usar cada comando
Antes de começar a trabalhar
git checkout main
git pull origin main
git checkout -b feature/nome-da-tarefa
Durante o desenvolvimento
git status
git add .
git commit -m "mensagem clara"
Para enviar para o GitHub
git push -u origin nome-da-branch
Depois que a tarefa for finalizada
git checkout main
git pull origin main
git merge nome-da-branch
git push
Depois do merge
git branch -d nome-da-branch
git push origin --delete nome-da-branch
Boas práticas
Faça commits pequenos e claros.
Não trabalhe direto na main.
Crie uma branch para cada tarefa.
Antes de criar branch nova, atualize a main.
Use mensagens de commit objetivas.
Sempre confira com git status antes de commitar.
Depois do merge, delete branches antigas.
Evite reutilizar a mesma branch para tarefas diferentes.
Exemplo de fluxo completo
git checkout main
git pull origin main
git checkout -b feature/agendamentos

# fazer alterações no código

git status
git add .
git commit -m "Cria página de agendamentos"
git push -u origin feature/agendamentos

Depois do merge:

git checkout main
git pull origin main
git branch -d feature/agendamentos
git push origin --delete feature/agendamentos