# Anotaçoes rapidas

## não e uma boa pratica deixar nomeclaturas do projeto em diferentes linguagesn e bom sempre deixar em ingles

### none e o retorno padrão quando a função não retorna nada

### arquivos estaticos do django são armazenados no cache do navegador por padrão

### Load static carrega por arquivo

### O termo "slug" se refere às URLs que descrevem o conteúdo que carregam. Geralmente, conseguimos gerar URLs descritivas ao utilizar o título do conteúdo com certas modificações ao final da URL. Nas modificações, geralmente substituímos caracteres inválidos por seus correspondentes mais próximos, trocamos espaços por hífen ou underline e removemos a pontuação. Por exemplo, um título "Chuvas ainda exigem atenção!!!" se tornaria "chuvas-ainda-exigem-atencao"

### Podemos filtrar dados usando uma Foreign Key (chave estrangeira) de determinado model. Para isso, usamos o nome do campo que representa a foreign key, dois underlines e o nome do campo no model estrangeiro (de onde vem a foreign key). Se o campo "category", de "Recipe", é uma foreign key para "Category", quando eu filtro category__name='Vegana', o que será retornado?

### Blank quer dizer que o campo pode ficar em branco

### category_name = getattr(getattr(recipes.first(), 'category', None), 'name', 'Not Found')

#### tenta pegar o que ta tentando pegar o primeiro recipe se pegar pega category se não retorna none se pegar tenta pegar name se não retorna not found
