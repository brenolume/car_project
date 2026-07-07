Resumo passo a passo dos conceitos

request
Todo view function no Django recebe o objeto request como primeiro parâmetro. Ele carrega tudo sobre a requisição HTTP: método (GET/POST), parâmetros de busca, usuário autenticado, cookies, etc.

Model.objects.all()
É o manager padrão do Django ORM. Retorna um QuerySet — uma coleção "preguiçosa" (lazy) de todos os registros da tabela correspondente ao model. "Preguiçosa" significa que a query só é executada no banco quando os dados são realmente acessados (ex: no template, ao iterar).

.order_by('-name')
Ordena o QuerySet pelo campo indicado. O - na frente indica ordem decrescente (Z→A ou maior→menor). Sem o -, seria crescente.

request.GET.get('search')
request.GET é um dicionário-like (QueryDict) com os parâmetros passados na URL via método GET (ex: ?search=toyota). .get('search') busca a chave search e retorna None se não existir — evita KeyError.

if search:
Só aplica o filtro se o usuário realmente enviou algo na busca, evitando filtrar com None ou string vazia.
.filter(name__icontains=search)
filter() retorna um novo QuerySet com apenas os registros que atendem à condição.

name__icontains usa a sintaxe de lookups do Django ORM: campo__lookup. Aqui, icontains faz uma busca de substring case-insensitive (não diferencia maiúsculas/minúsculas), similar a um LIKE '%valor%' no SQL.

render(request, template, context)
Função que combina um template HTML com um dicionário de contexto ({'cars': cars}) e retorna um HttpResponse pronto para o navegador. É obrigatório retornar isso — sem return, o Django não sabe o que enviar de volta e lança erro.