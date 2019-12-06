from django.db import models
# Create your models here.



class Status(models.Model):
    situacao= models.CharField(max_length=50)

    def __str__(self):
        return "({})".format(self.situacao)

class Curso(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return "({})".format(self.nome)

class DiasAtendimento(models.Model):
    diaAtendimento = models.CharField(max_length=20)
    horario_inicio= models.TimeField()
    horario_termino= models.TimeField()

    def __str__(self):
        return "{}".format(self.diaAtendimento)


class Estagiario(models.Model):
    nome = models.CharField(max_length=120, default=False)
    cgu = models.CharField(max_length=11, default=False, unique=True)
    cpf = models.CharField(max_length=11, default=False, unique=True)
    telefone = models.CharField(max_length=12, default=False)
    tipoEstagiario = models.IntegerField()
    diasAtendimento = models.ManyToManyField(DiasAtendimento, default='')

    def __str__(self):
        return "{} ({})".format(self.nome, self.cgu, self.cpf, self.tipoEstagiario)


class Recurso(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=120)
    quantidade = models.IntegerField(default=0, null=True)

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao, self.quantidade)


class Categoria(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=120)

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)


class Servico(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=120)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='servico')

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao, self.categoria)


class TipoDeficiencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)


class Academico(models.Model):
    cgu = models.CharField(max_length=9, unique=True,null=True,blank=True)
    nome = models.CharField(max_length=120)
    dataNascimento = models.DateField(null=True,blank=True)
    sexo = models.CharField(max_length=2,null=True, blank=True)
    naturalidade = models.CharField(max_length=30,null=True,blank=True)
    telefone = models.CharField(max_length=11, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, null=False)
    turno = models.CharField(max_length=20,null=True,blank=True)
    disponibilidadeAtendimento = models.CharField(max_length=50, null=True, blank=True)
    motivo = models.CharField(max_length=200, null=True, blank=True)
    observacoes = models.CharField(max_length=100, null=True, blank=True)
    vinculo = models.CharField(max_length=45, null=True, blank=True)
    tipoDeficiencia = models.ForeignKey(TipoDeficiencia, on_delete=models.PROTECT, null=True,blank=True)

    def __str__(self):
        return "{} ({})".format(self.cgu, self.nome, self.email)


class Agendamento(models.Model):
    academico = models.ForeignKey(Academico, on_delete=models.PROTECT)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    recurso = models.ForeignKey(Recurso, on_delete=models.PROTECT, null=True,blank=True)
    estagiario = models.ForeignKey(Estagiario, on_delete=models.PROTECT)
    data = models.DateField()
    horario = models.TimeField()
    frequenciaAcademico = models.IntegerField(null=True)
    frequenciaEstagiario = models.IntegerField(null=True)

    def __str__(self):
        return "{} ({})".format(self.academico, self.servico, self.estagiario, self.data)

class Biblioteca(models.Model):
    curse= models.CharField(max_length=120, null=True,blank=True)
    people= models.CharField(max_length=120, null=False,blank=False)
    data=models.DateField()
    livro= models.CharField(max_length=200)
    cargo= models.CharField(max_length=100, null=True,blank=True)
    status= models.ForeignKey(Status,on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.livro, self.status)

class Grupo(models.Model):
    nome_grupo= models.ForeignKey(Servico,on_delete=models.PROTECT)
    academico= models.ForeignKey(Academico,on_delete=models.PROTECT)
    curso= models.ForeignKey(Curso,on_delete=models.PROTECT)
    email= models.EmailField(unique=True,null=True,blank=True)
    inscricao= models.CharField(max_length=100,null=True,blank=True)
    data= models.DateField()
    sabendo_grupo= models.CharField(max_length=200, null=True, blank=True)
    expectativas= models.CharField(max_length=200, null=True, blank=True)
    horarios_disponiveis= models.CharField(max_length=200)

    def __str__(self):
        return "{} ({})".format(self.nome_grupo,self.academico,self.curso)

class Prova(models.Model):
    data= models.DateField()
    nome= models.CharField(max_length=120)
    sexo= models.CharField(max_length=2)
    dataNascimento= models.DateField()
    numeroAcademico= models.CharField(max_length=20, null=True,blank=True)
    telefone= models.CharField(max_length=11,null=True,blank=True)
    celular= models.CharField(max_length=11,null=True,blank=True)
    email= models.EmailField(unique=True,null=True,blank=True)
    curso= models.ForeignKey(Curso,on_delete=models.PROTECT)
    periodo= models.CharField(max_length=5,null=True,blank=True)
    possuiDeficiencia= models.CharField(max_length=100,null=True,blank=True)
    recebeuAuxilioNucleo= models.CharField(max_length=100,null=True,blank=True)
    disciplina= models.CharField(max_length=100)
    turma= models.CharField(max_length=6)
    professor= models.CharField(max_length=120)
    tipoAuxilio= models.CharField(max_length=120,null=True,blank=True)
    monitor= models.CharField(max_length=120)
    observacoes= models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return "{} ({})".format(self.data,self.nome,self.curso,self.disciplina,self.monitor)

class Cadeira_de_Rodas(models.Model):
    data=models.DateField()
    nome_pessoa=models.CharField(max_length=120)
    nome_curso=models.CharField(max_length=120,null=True,blank=True)
    cargo=models.CharField(max_length=120,null=True,blank=True)
    celular=models.CharField(max_length=20)
    data_devolucao=models.DateField()

    def __str__(self):
        return "{} ({})".format(self.data,self.nome_pessoa,self.data_devolucao)
