from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100) # Aumentei um pouco para nomes compostos
    email = models.EmailField(max_length=100, unique=True) # Valida e garante e-mail único
    telefone = models.CharField(max_length=20) # 20 é suficiente para (99) 99999-9999
    cpf = models.CharField(max_length=14, unique=True) # 14 permite salvar com pontos e traço

    def __str__(self):
        # Retorna uma string organizada e legível
        return f"{self.nome} (CPF: {self.cpf})"

