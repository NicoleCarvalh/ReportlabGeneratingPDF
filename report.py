import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
import matplotlib.pyplot as plt

def generate_pdf(report_data, filename="report.pdf"):
    # Configurar o documento PDF
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Título
    elements.append(Paragraph("Relatório de Vendas", styles['Title']))

    # Introdução
    elements.append(Paragraph("Este relatório apresenta uma análise detalhada das vendas e desempenho dos produtos para o período selecionado.", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Resumo Executivo
    elements.append(Paragraph("Resumo Executivo", styles['Heading2']))
    elements.append(Paragraph(f"Total de Vendas: R$ {report_data['total_vendas']:.2f}", styles['Normal']))
    elements.append(Paragraph(f"Produtos Vendidos: {sum(produto['quantidade'] for produto in report_data['produtos_vendidos'])}", styles['Normal']))
    elements.append(Paragraph(f"Ticket Médio: R$ {report_data['ticket_medio']:.2f}", styles['Normal']))
    elements.append(Paragraph(f"Produto Mais Vendido: {report_data['produto_mais_vendido']}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Análise de Vendas Diárias
    elements.append(Paragraph("Análise de Vendas Diárias", styles['Heading2']))
    sales_data = [["Data", "Total de Vendas", "Variação %"]]
    for data in report_data['vendas_diarias']:
        sales_data.append([data['data'], f"R$ {data['total']:.2f}", f"{data['variacao']}%"])
    t = Table(sales_data)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('FONTSIZE', (0, 0), (-1, 0), 12),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                           ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(t)
    elements.append(Spacer(1, 12))

    # Análise de Produtos Vendidos
    elements.append(Paragraph("Análise de Produtos Vendidos", styles['Heading2']))
    products_data = [["Produto", "Quantidade Vendida"]]
    for produto in report_data['produtos_vendidos']:
        products_data.append([produto['nome'], produto['quantidade']])
    t = Table(products_data)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('FONTSIZE', (0, 0), (-1, 0), 12),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                           ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(t)
    elements.append(Spacer(1, 12))

    # Gráfico de Exemplo
    elements.append(Paragraph("Gráfico de Vendas", styles['Heading2']))

    # Gerar um gráfico com matplotlib
    buffer = io.BytesIO()
    plt.figure(figsize=(6, 4))
    dates = [data['data'] for data in report_data['vendas_diarias']]
    sales = [data['total'] for data in report_data['vendas_diarias']]
    plt.plot(dates, sales, marker='o')
    plt.title('Total de Vendas Diárias')
    plt.xlabel('Data')
    plt.ylabel('Total de Vendas')
    plt.grid(True)
    plt.savefig(buffer, format='PNG')
    buffer.seek(0)
    
    # Adicionar gráfico ao PDF
    img = Image(buffer)
    elements.append(img)
    plt.close()

    # Conclusões e Recomendações
    elements.append(Paragraph("Conclusões e Recomendações", styles['Heading2']))
    elements.append(Paragraph("Baseado nos dados apresentados, recomenda-se focar nos produtos mais vendidos e analisar a performance dos métodos de pagamento para otimizar as estratégias de vendas.", styles['Normal']))

    # Construir o PDF
    doc.build(elements)

    buffer.close()

# Exemplo de dados para o relatório
report_data = {
    'total_vendas': 1234.56,
    'produtos_vendidos': [
        {'nome': 'Produto A', 'quantidade': 10},
        {'nome': 'Produto B', 'quantidade': 5},
    ],
    'ticket_medio': 123.46,
    'produto_mais_vendido': 'Produto A',
    'vendas_diarias': [
        {'data': '2024-06-08', 'total': 600.00, 'variacao': 10},
        {'data': '2024-06-07', 'total': 550.00, 'variacao': -5},
    ],
}

generate_pdf(report_data, filename="relatorio_vendas.pdf")
