from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# importante: sempre considerar que o início do plano é o canto inferior esquerdo,  0,0
# utiliza pontos, que é a unidade de medida do plano cartesiano. conseguimos converter essa medida com uma função

nomes = ['Cláudio', 'Adilson', 'Flávio']

# função para converter milímetros em pontos
def mm2p(milimetros):
  return milimetros / 0.352777


cnv = canvas.Canvas("meu_pdf.pdf")
cnv.setFont('Helvetica-Bold', 18) # alterando fonte
eixoX = 100

eixoY = 100

# mexendo com eixo X do plano cartesiano
for nome in nomes:
  cnv.drawString(mm2p(eixoX), 450, nome)
  eixoX += 30

# mexendo com eixo y do plano cartesiano
for nome in nomes:
  cnv.drawString(250, mm2p(eixoY), nome)
  eixoY += 30

cnv.showPage() # indica ao ReportLab que terminamos de desenhar a página atual e queremos iniciar uma nova. 

# criando um círculo
# para desenhar o círculo verificamos as coordenadas e tamanho -> coordenadas x e y é um ponto e raio
cnv.circle(mm2p(100), mm2p(150), mm2p(100))

# criando uma linha
# informamos x e y início e x e y do fim
cnv.line(mm2p(100), mm2p(150), mm2p(120), mm2p(160))

# criando um retãngulo
# informamos dois pontos -> canto superior esquerdo e canto inferior direito
cnv.rect(mm2p(100), mm2p(150), mm2p(50), mm2p(50))

# criando imagem
cnv.drawImage('PetCareConnect.png', 200, 250, width=200, height=100)

cnv.save()

# core para criar pdf e salvar

# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4

# cnv = canvas.Canvas("meu_pdf.pdf")
# cnv.drawString(250, 450, "Teste")