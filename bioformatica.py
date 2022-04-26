entrada = open("16s_bacteria.fasta").read()
saida = open("16s_bacteria.html", "w")

count = {}
entrada = entrada.replace('\n', '')

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        count[i + j] = 0

for k in range(len(entrada) - 1):
    count[entrada[k] + entrada[k + 1]] += 1

# html

saida.write("<div>")


i = 1
for k in count:
    transparencia = count[k] / max(count.values())
    saida.write("<div style='width:100px; border:1px solid #111; color:#fff; "
                "height:100px; float:left; background-color:rgba(0, 0, 0, " +
                str(transparencia) + "')>" + k + ":" + str(count[k]) + "</div>")

    if i % 4 == 0:
        saida.write("<div style='clear:both'></div>")

    i += 1

saida.close()
