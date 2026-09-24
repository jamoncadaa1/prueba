from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.fonts import addMapping
F="/usr/share/fonts/truetype/liberation/LiberationSans-"
for n,f in [("Arial","Regular"),("Arial-B","Bold"),("Arial-I","Italic"),("Arial-BI","BoldItalic")]:
    pdfmetrics.registerFont(TTFont(n,F+f+".ttf"))
addMapping("Arial",0,0,"Arial");addMapping("Arial",1,0,"Arial-B");addMapping("Arial",0,1,"Arial-I");addMapping("Arial",1,1,"Arial-BI")
N=ParagraphStyle("n",fontName="Arial",fontSize=12,leading=18,alignment=TA_JUSTIFY)
C=ParagraphStyle("c",parent=N,alignment=TA_CENTER)
B=ParagraphStyle("b",parent=C,fontName="Arial-B")
E=Spacer(1,18)
s=[]
def p(t,st=N): s.append(Paragraph(t,st))
p("ACTIVIDAD 1. HISTORIAS",B);p("EL FUEGO EN LAS SOMBRAS",B);s.append(Spacer(1,150))
p("JOSÉ LEONARDO BORRERO",C);p("JULIÁN MONCADA",C);s.append(Spacer(1,150))
p("Antropología",C);s.append(Spacer(1,150));p("24 de septiembre de 2026",C);s.append(PageBreak())
p("1. ANÁLISIS DE LA HISTORIA ORIGINAL",B);s.append(E)
p("<b>a. ¿Qué elementos culturales están presentes?</b>")
for t in ["El elemento central es la religión. El autor explica que las religiones dan sentido a las vivencias de una sociedad, fijan prohibiciones y reglas, y según la religión de cada grupo las personas interpretan por qué ocurren las cosas.",
"Aparecen los lugares sagrados, sean mezquitas, iglesias u otros espacios, a los que se acude para adorar y rezar a entes sobrenaturales que cambian de una religión a otra.",
"También están las prácticas funerarias, que varían con la religión y con la cultura en la que cada persona se cría. Un ejemplo son los entierros de los neandertales.",
"Por último se mencionan las túnicas y vestimentas, los adornos corporales, las imágenes, las figuras y los grabados en las paredes, además de los rituales y los mitos. Todos forman parte de las tradiciones culturales."]:
    p(t)
s.append(E);p("<b>b. ¿Qué valores, creencias o prácticas se reflejan?</b>")
for k,v in [("Respeto por los muertos:","los entierros muestran una atención especial hacia las personas fallecidas."),
("Creencia en un posible más allá:","el autor la plantea, aunque no precisa en qué creencias concretas se apoya."),
("Valor de lo sagrado:","ciertos lugares, como los espacios subterráneos, adquirieron un significado especial."),
("Simbolismo:","grabados, imágenes y adornos se usaban para la adoración."),
("Tradición cultural:","las fórmulas artísticas y los códigos se mantuvieron durante mucho tiempo."),
("Organización social:","el texto relaciona rituales, mitos, valores y diferencias de estatus entre individuos.")]:
    p(f"• <b>{k}</b> {v}")
s.append(PageBreak())
p("2. NUEVA HISTORIA: EL FUEGO EN LAS SOMBRAS",B);s.append(E)
for t in open("historia.txt",encoding="utf-8").read().strip().split("\n\n"):
    p(t);s.append(Spacer(1,6))
s.append(E);s.append(Image("guacharo.png",width=14*cm,height=8.75*cm))
p("<i>Figura 1. Ilustración de la primera pintura del guácharo a la luz de la lámpara de grasa. Imagen elaborada digitalmente para esta actividad.</i>",C)
s.append(PageBreak())
p("3. SOCIALIZACIÓN DE LA PROPUESTA",B);s.append(E)
for t in open("socializacion.txt",encoding="utf-8").read().strip().split("\n\n"):
    p(t);s.append(Spacer(1,6))
SimpleDocTemplate("Actividad1_Historias_Borrero_Moncada.pdf",pagesize=letter,topMargin=3*cm,bottomMargin=3*cm,leftMargin=4*cm,rightMargin=2*cm,title="Actividad 1. Historias",author="José Leonardo Borrero, Julián Moncada").build(s)
