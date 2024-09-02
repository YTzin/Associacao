from django.db import models
from datetime import date

class Conjuge(models.Model):
    nome = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    idade = models.PositiveIntegerField(default=0)
    naturalidade = models.CharField(max_length=20, default="Russas")
    sexo = models.CharField(max_length=9, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')])
    profissao = models.CharField(max_length=20)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=30)
    n_rg = models.CharField(max_length=9)
    orgao_exp = models.CharField(max_length=20)
    data_expedicao = models.DateField()
    cpf = models.CharField(max_length=11)
    titulo = models.CharField(max_length=11)
    carteira_trabalho = models.CharField(max_length=10, blank=True, null=True)
    serie = models.CharField(max_length=10, blank=True, null=True)
    registro_civil = models.CharField(max_length=20, blank=True, null=True)
    certidao = models.CharField(max_length=20, choices=[('certidao_casamento', 'Certidão de Casamento'), ('certidao_nascimento', 'Certidão de Nascimento')])
    folhas = models.CharField(max_length=10, blank=True, null=True)
    livro = models.CharField(max_length=10, blank=True, null=True)
    data_emissao = models.DateField()
    outras_instituicoes = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')], default='nao', blank=True, null=True)
    detalhes_outros_instituicoes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Cônjuge'
    
    def calcula_idade(self):
        today = date.today()
        idade = today.year - self.data_nascimento.year
        if today.month < self.data_nascimento.month or (today.month == self.data_nascimento.month and today.day < self.data_nascimento.day):
            idade -= 1
        return idade

    def __str__(self):
        return self.nome

class Dependentes(models.Model):
    nome = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    idade = models.PositiveIntegerField(default=0)
    naturalidade = models.CharField(max_length=20, default="Russas")
    sexo = models.CharField(max_length=9, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')])
    endereco = models.CharField(max_length=30)
    n_rg = models.CharField(max_length=9)
    orgao_exp = models.CharField(max_length=20)
    data_expedicao = models.DateField()
    cpf = models.CharField(max_length=11)
    certidao = models.CharField(max_length=20, choices=[ ('certidao_nascimento', 'Certidão de Nascimento')])
    folhas = models.CharField(max_length=10, blank=True, null=True)
    livro = models.CharField(max_length=10, blank=True, null=True)
    data_emissao = models.DateField()
    registro_civil = models.CharField(max_length=20, blank=True, null=True)
    outras_instituicoes = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')], default='nao', blank=True, null=True)
    detalhes_outros_instituicoes = models.CharField(max_length=255, blank=True, null=True)
    estuda = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')], default='nao', blank=True, null=True)
    serie = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = 'Dependente'
    
    def calcula_idade(self):
        today = date.today()
        idade = today.year - self.data_nascimento.year
        if today.month < self.data_nascimento.month or (today.month == self.data_nascimento.month and today.day < self.data_nascimento.day):
            idade -= 1
        return idade
    
    def __str__(self):
        return self.nome

class Pessoas(models.Model):
    CERTIDAO_CASAMENTO = 'certidao_casamento'
    CERTIDAO_NASCIMENTO = 'certidao_nascimento'

    CERTIDAO_CHOICES = [
        (CERTIDAO_CASAMENTO, 'Certidão de Casamento'),
        (CERTIDAO_NASCIMENTO, 'Certidão de Nascimento'),
    ]
    data_cadastramento = models.DateField()
    data_inclusao = models.DateField()
    nome = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    idade = models.PositiveIntegerField(default=0)
    naturalidade = models.CharField(max_length=20, default="Russas")
    sexo = models.CharField(max_length=9, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')])
    estado_civil = models.CharField(max_length=13, choices=[('solteiro', 'Solteiro'), ('casado', 'Casado'), ('divorciado', 'Divorciado'), ('viuvo', 'Viúvo'), ('uniao_estavel', 'União estável')])
    profissao = models.CharField(max_length=20)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=30 )
    n_rg = models.CharField(max_length=9)
    orgao_exp = models.CharField(max_length=20)
    data_expedicao = models.DateField()
    cpf = models.CharField(max_length=11)
    titulo = models.CharField(max_length=11)
    carteira_trabalho = models.CharField(max_length=10, blank=True, null=True)
    serie = models.CharField(max_length=10, blank=True, null=True)
    registro_civil = models.CharField(max_length=20, blank=True, null=True)
    certidao = models.CharField(
        max_length=20,
        choices=CERTIDAO_CHOICES,
        default=CERTIDAO_CASAMENTO  # Define o valor padrão
    )
    folhas = models.CharField(max_length=10, blank=True, null=True)
    livro = models.CharField(max_length=10, blank=True, null=True)
    data_emissao = models.DateField()
    outras_instituicoes = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')], default='nao', blank=True, null=True)
    detalhes_outros_instituicoes = models.CharField(max_length=255, blank=True, null=True, default='Não participa')
    conjuge = models.ForeignKey(Conjuge, on_delete=models.SET_NULL, null=True, blank=True, related_name='pessoas')
    dependente = models.ManyToManyField(Dependentes, blank=True, related_name='pessoas')
    
    def calcula_idade(self):
        today = date.today()
        idade = today.year - self.data_nascimento.year
        if today.month < self.data_nascimento.month or (today.month == self.data_nascimento.month and today.day < self.data_nascimento.day):
            idade -= 1
        return idade
    
    class Meta:
        verbose_name = 'Pessoa'
    
    def __str__(self):
        return self.nome
