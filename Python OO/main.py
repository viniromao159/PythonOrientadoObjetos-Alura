from conta import Conta
from datas import Datas

conta = Conta(123, "vinicius lopes romao", 55.5, 1000.0)

print(conta.limite)

conta.limite = 2000.0

print(conta.limite)

print(conta.saldo)

conta.deposita(50)

conta.extrato()
