from pessoaMedico import PessoaMedico
from pessoaAdvogado import PessoaAdvogado

listPessoaMedico = []
listPessoaAdvogado = []

pessoaMedico1 = PessoaMedico(628406, "Garibalda", 38, 12345678919, 12344567)
pessoaMedico2 = PessoaMedico(130975, "Miranha", 24, 12345678944, 123443567)

listPessoaMedico.append(pessoaMedico1)
listPessoaMedico.append(pessoaMedico2)

PessoaAdvogado1 = PessoaAdvogado(1234, "Astrogilda", 45, 5645489712, 8888888)
PessoaAdvogado2 = PessoaAdvogado(5678, "Godofredo", 58, 98765432100, 2222222)

listPessoaAdvogado.append(PessoaAdvogado1)
listPessoaAdvogado.append(PessoaAdvogado2)


print("--"*40)

for ad in listPessoaAdvogado:
    print("Advogado(a):")
    print('OAB: {} / Nome: {} / Idade: {}'.format(ad.getOab(), ad.getNome(), ad.getIdade()))
    print('CPF: {} / FONE: {}'.format(ad.getCpf(), ad.getTelefone().getTelefone()))
    print()

print("--"*40)
for md in listPessoaMedico:
    print("Médico(a):")
    print('CRM: {} / Nome: {} / Idade {}'.format(md.getCrm(), md.getNome(), md.getIdade()))
    print('CPF: {} / FONE: {}'.format(md.getCpf(), md.getTelefone().getTelefone()))
    print()