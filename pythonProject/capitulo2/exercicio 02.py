precocapalivro= 24.95
precocapalivrodesconto = precocapalivro - (precocapalivro * 0.40)
custodofreteprimeiroexemplar = precocapalivrodesconto + 3.00
custodefreteparaorestantedeexemplares = precocapalivrodesconto + 0.75
custototalatacado = custodofreteprimeiroexemplar + (custodefreteparaorestantedeexemplares * 59)

print("o preco total de atacado para os exemplares e de:", custototalatacado)
