🚀 Comandos Diários do Git

Guia rápido com o fluxo essencial de comandos para o dia a dia de desenvolvimento.

🔄 Fluxo de Trabalho Padrão

# 1. Atualize seu repositório local com a branch principal
git checkout main
git pull

# 2. Crie e mude para uma nova branch de desenvolvimento
git checkout -b minha-feature

# 3. Verifique o status dos arquivos modificados
git status

# 4. Adicione as alterações para a área de preparação (stage)
git add .

# 5. Grave as alterações com uma mensagem descritiva
git commit -m "Explique aqui o que você fez"

# 6. Envie a nova branch para o repositório remoto (GitHub/GitLab)
git push -u origin minha-feature
```

##💡 Dicas Rápidas
git log --oneline`**: Mostra o histórico de commits de forma simplificada.
git diff`**: Veja as alterações exatas feitas nos arquivos antes de usar o `git add`.
git checkout .`**: Descarta todas as alterações locais que ainda não foram salvas.