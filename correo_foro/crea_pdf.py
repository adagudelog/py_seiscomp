# -*- coding: utf-8 -*-

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def make_pdf(nombre_usuario,filiacion, dir="./cartas/"):

	print nombre_usuario
	documento="Invitacion_"+nombre_usuario+".pdf"
	ruta=dir+documento

	doc = SimpleDocTemplate(ruta, pagesize=letter,
	                        rightMargin=72, leftMargin=72,
	                        topMargin=0, bottomMargin=0)

	estilos = getSampleStyleSheet()
	estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	Story = []

	logo_foro = 'logo_foro.png'
	logo_patrocinadores = 'logo_patrocinadores.png'
	firma_marta = 'firma_marta.jpg'

	imagen = Image(logo_foro, 8*inch, 1.5*inch)
	Story.append(imagen)

	texto="Bogotá D.C., 26 de septiembre de 2018"                                                                             
	Story.append(Paragraph(texto, estilos["Justify"]))

	Story.append(Spacer(1, 12))
	texto="Respetado(a):"                                                                             
	Story.append(Paragraph(texto, estilos["Justify"]))

	Story.append(Spacer(1, 2))                                                             
	Story.append(Paragraph(nombre_usuario, estilos["Justify"]))

	Story.append(Spacer(1, 2))
	Story.append(Paragraph(filiacion, estilos["Justify"]))

	Story.append(Spacer(1, 12))
	texto = 'Asunto: Respuesta participación en el <i><b>“Primer Foro \
	        Internacional de Redes Sismológicas, Amenaza Sísmica \
	        Gestión del Riesgo de Desastres </b></i>"' 
	Story.append(Paragraph(texto, estilos["Justify"]))

	Story.append(Spacer(1, 20))
	texto = 'Reciba un respetuoso y cordial saludo,' 
	Story.append(Paragraph(texto, estilos["Justify"]))

	Story.append(Spacer(1, 20))
	texto = 'La Agencia Presidencial de Cooperación Internacional \
	de Colombia – APC Colombia, el Servicio Geológico Colombiano — \
	SGC, la Unidad Nacional de Gestión del Riesgo de Desastres – \
	UNGRD y la Gobernación del Quindío con el apoyo de la Agencia \
	de los Estados Unidos para el Desarrollo Internacional a \
	través de la Oficina de Asistencia para Desastres en el \
	Extranjero - USAID/OFDA, tienen el gusto de invitarle a \
	participar de manera activa como asistente en el <i><b>"Primer \
	foro internacional de redes sismológicas, amenaza sísmica\
	 y gestión del riesgo de desastres"</b></i>, que se llevará a \
	 cabo del 1° al 4 de octubre de 2018 en Armenia, Quindío\
	  — Colombia. El foro está motivado en atender la demanda \
	  de los países de la región para impulsar la cooperación \
	  técnica y científica en torno al fortalecimiento de la \
	  toma de decisiones ante la posible ocurrencia de eventos\
	   sísmicos con poder destructivo, por lo cual consideramos\
	    que es de gran importancia contar con su participación.' 
	Story.append(Paragraph(texto, estilos["Justify"]))

	Story.append(Spacer(1, 12))
	texto = 'En América Latina y el Caribe la ocurrencia de \
	eventos sísmicos de gran magnitud con efectos destructivos\
	 ha proporcionado experiencias y lecciones aprendidas \
	 enriquecedoras. Reconociendo la importancia de esto,\
	  así como los avances en ciencia y tecnología, los aportes \
	  en el manejo de desastres de las redes sismológicas y\
	   organismos de gestión del riesgo de estos países, \
	   Colombia busca fortalecer la cooperación internacional \
	   de los países de la región para la creación de escenarios \
	   que permitan el intercambio de dichas experiencias, \
	   avances y aportes, enfocado al manejo y toma de \
	   decisiones para la reducción del riesgo de desastres \
	   por actividad sísmica.' 
	Story.append(Paragraph(texto, estilos["Justify"]))


	Story.append(Spacer(1, 12))
	texto = 'Agradecemos poder contar con su participación y \
	valiosa contribución a este evento.' 
	Story.append(Paragraph(texto, estilos["Justify"]))

	Story.append(Spacer(1, 12))
	texto = '<i>El foro no tiene ningún costo de inscripción. Los \
	 gastos de trasporte, alojamiento y alimentación corren \
	 por cuenta de cada uno de los asistentes.</i>' 
	Story.append(Paragraph(texto, estilos["Justify"]))

	Story.append(Spacer(1, 30))
	imagen = Image(firma_marta, 3*inch, 0.5*inch)
	imagen.hAlign = 'LEFT'
	Story.append(imagen)

	Story.append(Spacer(1, 1))
	texto="_______________________________________"                                                                             
	Story.append(Paragraph(texto, estilos["Justify"]))	

	Story.append(Spacer(1, 2))
	texto="<b>MARTA LUCIA CALVACHE</b>"
	Story.append(Paragraph(texto, estilos["Justify"]))

	Story.append(Spacer(1, 2))
	texto="Directora – Dirección de Geoamenazas"
	Story.append(Paragraph(texto, estilos["Justify"]))

	Story.append(Spacer(1, 2))
	texto="Servicio Geológico Colombiano "
	Story.append(Paragraph(texto, estilos["Justify"]))
	
	Story.append(Spacer(1, 5))
	imagen = Image(logo_patrocinadores, 6.4*inch, 1.3*inch)
	Story.append(imagen)

	doc.build(Story)

	return ruta

if __name__ == '__main__':
	make_pdf("Guzman", "SGC")




 
