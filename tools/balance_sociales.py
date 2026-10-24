"""
Equilibra las longitudes de opciones en Sociales para eliminar el sesgo de longitud
(la opción correcta es la más larga en <= 30% de preguntas) y elimina distractores absurdos.
"""
import json
from tools.gen_area_hojas import build_hoja_for_question

def balance_sociales():
    soc = json.load(open('content/questions/sociales.json', 'r', encoding='utf-8'))
    hojas = json.load(open('content/hojas.json', 'r', encoding='utf-8'))
    guiones = json.load(open('content/guiones.json', 'r', encoding='utf-8'))
    enfoques = json.load(open('content/enfoques.json', 'r', encoding='utf-8'))

    # Custom balanced options for questions that had high length bias
    # We enrich the distractors so all 4 options are well-developed (~110-150 chars)
    # and for several questions make a distractor slightly longer than the correct option.
    balanced = {
        'soc-005': {
            'opciones': [
                'La acción popular, creada para proteger derechos colectivos como el medio ambiente sano y el espacio público.',
                'La acción de tutela, interpuesta argumentando la protección judicial colectiva de los recursos hídricos y el agua de la zona.',
                'El hábeas corpus preventivo, con el fin de exigir sanciones penales inmediatas y privación de libertad a los gerentes de la empresa.',
                'El plebiscito municipal, para que la ciudadanía vote en las urnas si aprueba la licencia ambiental de la fábrica en el territorio.'
            ]
        },
        'soc-006': {
            'opciones': [
                'El hábeas corpus, garantía fundamental que debe resolverse en un plazo máximo de 36 horas frente a capturas arbitrarias.',
                'El hábeas data, interpuesto ante las autoridades competentes para borrar sus antecedentes de la base de datos de la policía.',
                'Una consulta previa obligatoria con las autoridades comunitarias y líderes del barrio donde se produjo la detención preventiva.',
                'Un referendo derogatorio contra el Código Nacional de Policía tramitado mediante firmas ciudadanas ante el Congreso.'
            ]
        },
        'soc-009': {
            'opciones': [
                'El Estado tiene el deber prioritario de garantizar condiciones mínimas materiales de vida digna, salud, educación y equidad para todas las personas.',
                'El Estado solo debe garantizar la seguridad policial y el orden público, absteniéndose de intervenir en la economía, los servicios y la salud.',
                'Las leyes aprobadas pueden ser ignoradas legítimamente por los gobernantes de turno si consideran que no son convenientes para la administración.',
                'Solo los ciudadanos con altos ingresos tributarios tienen derecho al amparo judicial del Estado y a la representación de las instituciones públicas.'
            ]
        },
        'soc-010': {
            'opciones': [
                'La supremacía constitucional y el sistema de frenos y contrapesos entre las ramas del poder público.',
                'La subordinación absoluta y permanente del poder legislativo a las decisiones tomadas por los mandos militares en el territorio nacional.',
                'La concentración de todo el poder estatal en la Presidencia de la República para asegurar la gobernabilidad y el orden institucional.',
                'La anulación definitiva de la separación de poderes públicos a favor de una dictadura judicial centralizada en las altas cortes.'
            ]
        },
        'soc-012': {
            'opciones': [
                'Mantener el poder adquisitivo de la moneda y controlar la inflación, sin depender de los intereses electorales del gobierno de turno.',
                'Financiar directamente las campañas electorales de los partidos políticos y fijar unilateralmente los precios de venta en los supermercados.',
                'Fijar por decreto los salarios de todos los empleados del sector privado e intervenir en la designación de ministros del gabinete.',
                'Administrar los recursos de la salud pública municipal y gestionar las licitaciones de obras públicas de infraestructura vial.'
            ]
        },
        'soc-013': {
            'opciones': [
                'Detener la violencia bipartidista y restaurar la democracia compartiendo el poder de manera paritaria, aunque excluyendo a otras fuerzas políticas.',
                'Instaurar una dictadura militar indefinida para combatir a las guerrillas emergentes y suspender el funcionamiento del Congreso.',
                'Eliminar por completo las elecciones populares y designar a perpetuidad a los gobernantes de turno en todos los departamentos del país.',
                'Fusionar los partidos Liberal y Conservador en un único partido político socialista obligatorio para todos los ciudadanos colombianos.'
            ]
        },
        'soc-015': {
            'opciones': [
                'La ganadería extensiva en los valles del Caribe, que demandó la construcción de canales de riego para el transporte masivo de carne.',
                'La economía cafetera campesina, que generó ingresos masivos de divisas y promovió ferrocarriles y carreteras hacia los puertos.',
                'La explotación petrolera en la Amazonía, que motivó el traslado de la mayor parte de la población campesina hacia las selvas del sur.',
                'La minería de oro en el Chocó, que concentró todas las inversiones estatales en infraestructura portuaria del océano Pacífico.'
            ]
        },
        'soc-016': {
            'opciones': [
                'El inicio inmediato del Frente Nacional y el desarme pacífico de todas las cuadrillas armadas liberales y conservadoras del país.',
                'El Bogotazo, una ola masiva de revueltas populares e incendios en la capital que profundizó el período conocido como La Violencia.',
                'La proclamación inmediata de una nueva Constitución Política con amplia participación de sectores obreros, indígenas y campesinos.',
                'La firma de un tratado de libre comercio con Estados Unidos para industrializar la producción agrícola del centro de Colombia.'
            ]
        },
        'soc-017': {
            'opciones': [
                'La centralización fiscal total en Bogotá, exigiendo que todos los municipios soliciten autorización presidencial para contratar obras menores.',
                'El traslado de recursos y competencias de la Nación a departamentos y municipios para financiar salud, educación, agua potable y saneamiento básico.',
                'La privatización absoluta de todos los colegios y hospitales públicos del país, delegando su administración a fundaciones extranjeras.',
                'La eliminación de las alcaldías municipales, reemplazando a los alcaldes electos por gobernadores designados por el Congreso de la República.'
            ]
        },
        'soc-018': {
            'opciones': [
                'La titulación individual privada de parcelas agrícolas con autorización expresa de venta inmediata a corporaciones agroindustriales.',
                'El reconocimiento de la propiedad colectiva de tierras a comunidades afrodescendientes y mecanismos para proteger su identidad cultural.',
                'La reubicación forzosa de las comunidades negras de las cuencas del Pacífico hacia centros urbanos industriales del interior del país.',
                'La prohibición de toda actividad económica tradicional de pesca y agricultura en los territorios ancestrales ribereños del litoral Pacífico.'
            ]
        },
        'soc-019': {
            'opciones': [
                'Los cabildos indígenas pueden aplicar normas de cualquier país extranjero sin consultar a las autoridades ni a los jueces colombianos.',
                'Las autoridades tradicionales ejercen funciones jurisdiccionales dentro de su territorio según sus normas, respetando la Constitución y los derechos humanos.',
                'Los pueblos indígenas quedan totalmente exonerados de cumplir las leyes de la República y pueden crear sus propios ejércitos armados.',
                'La justicia ordinaria colombiana asume de manera forzosa el juzgamiento de todos los conflictos internos de los resguardos del país.'
            ]
        },
        'soc-020': {
            'opciones': [
                'Los TLC benefician por igual a todos los sectores productivos sin que ninguna rama de la economía experimente dificultades ni pérdidas de empleo.',
                'Benefician a exportadores competitivos (flores, café) mientras generan pérdidas a pequeños agricultores que compiten con productos subsidiados del exterior.',
                'Los tratados comerciales eliminan automáticamente la pobreza extrema y garantizan que no existan fluctuaciones en la tasa de cambio del dólar.',
                'Los acuerdos prohíben la inversión extranjera en el país y obligan al Estado a subsidiar la totalidad de los costos de importación.'
            ]
        },
        'soc-021': {
            'opciones': [
                'Tensión entre el crecimiento económico por regalías mineras y el derecho colectivo al agua y la protección del ecosistema de páramo.',
                'Conflicto limítrofe internacional entre Colombia y países vecinos por la demarcación de la soberanía en la cordillera Oriental.',
                'Debate exclusivo sobre si las oficinas administrativas de la compañía deben instalarse en la capital departamental o en el municipio sede.',
                'Disputa sobre qué empresa de telefonía celular debe instalar antenas de telecomunicación en las cumbres montañosas del páramo andino.'
            ]
        },
        'soc-022': {
            'opciones': [
                'Un trámite informativo rápido donde la empresa notifica sus planes sin necesidad de escuchar los argumentos de la comunidad.',
                'Un derecho fundamental de concertación previa, libre e informada con comunidades étnicas antes de autorizar proyectos en sus territorios ancestrales.',
                'Una consulta informal por internet donde cualquier ciudadano del país puede votar si aprueba o rechaza el proyecto de extracción.',
                'Un mecanismo administrativo exclusivo para proyectos petroleros que no aplica en proyectos de minería de oro ni de infraestructura vial.'
            ]
        },
        'soc-024': {
            'opciones': [
                'Erradican de manera inmediata y permanente la desigualdad estructural sin necesidad de invertir en educación, salud ni empleo formal.',
                'Alivian la pobreza extrema a corto plazo condicionando los subsidios a la asistencia escolar y controles de salud, pero requieren políticas de empleo duraderas.',
                'Incentivan a las familias beneficiarias a abandonar el trabajo productivo para depender exclusivamente de las transferencias del gobierno.',
                'Son programas diseñados exclusivamente para financiar campañas políticas y no tienen ningún efecto en la nutrición de los menores de edad.'
            ]
        },
        'soc-025': {
            'opciones': [
                'El modelo exclusivamente punitivo que combate el consumo con penas de cárcel y el enfoque de salud pública, derechos humanos y regulación estatal.',
                'La discusión sobre si el cultivo debe prohibirse únicamente en zonas urbanas o permitirse exclusivamente en parques nacionales naturales.',
                'La controversia sobre si el Estado debe importar toda la producción desde Europa o privatizar la venta en droguerías comerciales.',
                'El debate sobre si los impuestos recaudados deben entregarse a los bancos privados o invertirse en propaganda televisiva del gobierno.'
            ]
        },
        'soc-026': {
            'opciones': [
                'La ganadería extensiva, el acaparamiento de tierras comunales y los cultivos de uso ilícito que destruyen la cobertura boscosa tropical.',
                'La construcción masiva de rascacielos y zonas residenciales de alta densidad poblacional para familias de clase media del departamento.',
                'La proliferación de empresas de reciclaje de plástico que talan árboles nativos para instalar plantas procesadoras de residuos orgánicos.',
                'El aumento descontrolado de turistas internacionales que recogen hojas secas y ramas caídas en los senderos ecológicos de la selva.'
            ]
        },
        'soc-027': {
            'opciones': [
                'La libertad de expresión es absoluta y autoriza la difusión de cualquier acusación, sin importar el daño causado a la dignidad de la persona afectada.',
                'La libertad de expresión protege la crítica y el debate público, pero tiene límites constitucionales cuando vulnera la honra y el buen nombre ajenos.',
                'El derecho a la honra exige que toda publicación en redes sociales sea previamente censurada y aprobada por un funcionario del Ministerio de Justicia.',
                'Las redes sociales no están sujetas a la Constitución ni a las leyes nacionales, por tratarse de plataformas digitales de origen extranjero.'
            ]
        },
        'soc-028': {
            'opciones': [
                'Una tarifa que penaliza el uso del transporte público masivo e incentiva la compra masiva de camionetas particulares de alto consumo.',
                'Un instrumento económico de gestión de la demanda que desincentiva el uso del vehículo particular y genera recursos para el transporte masivo.',
                'Una prohibición total de ingreso de cualquier vehículo automotor al perímetro urbano de la ciudad durante todos los días del año calendario.',
                'Un subsidio estatal para que los conductores de automóviles particulares paguen menos dinero en las estaciones de gasolina de la ciudad.'
            ]
        },
        'soc-029': {
            'opciones': [
                'El deber del Estado de preservar el espacio público para el disfrute colectivo frente al derecho al trabajo y al mínimo vital de los vendedores informales.',
                'La disputa entre diferentes empresas multinacionales de comidas rápidas por instalar franquicias comerciales en las principales aceras peatonales.',
                'El conflicto sobre si los semáforos de las avenidas principales deben sincronizarse para favorecer el paso de ciclistas o de vehículos de carga pesada.',
                'La controversia entre el sindicato de policías metropolitanos y la alcaldía sobre el aumento en el presupuesto de dotación de uniformes y patrullas.'
            ]
        },
        'soc-030': {
            'opciones': [
                'El perdón incondicional y el indulto generalizado para todos los comparecientes sin obligación de aportar verdad ni reparar a las víctimas.',
                'El equilibrio entre justicia restaurativa, sanción a máximos responsables, aporte pleno a la verdad y reparación integral para las víctimas del conflicto.',
                'La aplicación exclusiva de la pena de muerte y el destierro forzoso de los combatientes sin derecho a la defensa jurídica en los tribunales especiales.',
                'El pago de indemnizaciones económicas millonarias por parte del tribunal de paz a los acusados de violaciones a los derechos humanos del país.'
            ]
        },
        'soc-031': {
            'opciones': [
                'Cerrar de manera inmediata todas las minas de carbón sin ofrecer planes de reconversión laboral ni alternativas económicas para las comunidades de la región.',
                'Planificar una reconversión productiva integral y gradual que sustituya las regalías del carbón por energías limpias y empleo digno en los territorios mineros.',
                'Aumentar al doble la extracción de carbón térmico para exportarlo a países vecinos antes de que entren en vigencia los compromisos climáticos mundiales.',
                'Trasladar a todos los trabajadores de las minas hacia proyectos de exploración petrolera en el mar Caribe colombiano sin previo entrenamiento técnico.'
            ]
        },
        'soc-032': {
            'opciones': [
                'Permitir que los menores de edad trabajen a tiempo completo en labores pesadas porque la tradición familiar campesina prima sobre las normas internacionales.',
                'Proteger de manera prevalente los derechos de los niños a la educación y el desarrollo integral, combatiendo la deserción escolar en el campo.',
                'Multar económicamente y retirar la patria potestad a todas las familias campesinas pobres sin brindarles apoyos estatales ni becas educativas.',
                'Prohibir que los menores de edad visiten el campo o tengan contacto con actividades agropecuarias recreativas durante los fines de semana.'
            ]
        },
        'soc-033': {
            'opciones': [
                'Al encarecer el crédito bancario para consumo e inversión, se modera la demanda agregada de bienes y servicios desacelerando el ritmo de los precios.',
                'Al elevar la tasa, el banco central emite mayor cantidad de dinero en efectivo para que los ciudadanos adquieran más bienes de la canasta familiar.',
                'Al decretar tasas altas, el gobierno fija administrativamente precios máximos congelados para todos los productos de consumo masivo en el comercio.',
                'Al incrementar el interés, se devalúa inmediatamente la moneda nacional frente a divisas extranjeras abaratando las importaciones de alimentos.'
            ]
        },
        'soc-034': {
            'opciones': [
                'Un sistema tributario progresivo busca que quienes tienen mayor capacidad de pago aporten una proporción más alta de sus ingresos a las finanzas del Estado.',
                'Un sistema progresivo exige que los ciudadanos de menores ingresos paguen tasas impositivas más altas para obligarlos a incorporarse al sector formal.',
                'Un modelo fiscal progresivo elimina todos los impuestos a las ganancias empresariales y financia el presupuesto exclusivamente con el impuesto al valor agregado.',
                'Un régimen progresivo distribuye la carga tributaria en partes idénticas en pesos entre todos los habitantes sin importar su salario ni su patrimonio.'
            ]
        },
        'soc-035': {
            'opciones': [
                'Fenómeno de demanda inducida: ampliar la capacidad vial puede aliviar la congestión a corto plazo, pero a mediano plazo atrae más vehículos particulares a la avenida.',
                'Solución definitiva: construir más carriles vehiculares reduce permanentemente los trancones urbanos sin importar el crecimiento del parque automotor de la ciudad.',
                'Afectación económica: la obra de ampliación genera pérdidas comerciales irreparables que obligan a clausurar el comercio formal de todo el municipio.',
                'Efecto ambiental positivo: aumentar el espacio para automóviles reduce de forma inmediata las emisiones de gases de efecto invernadero en la ciudad.'
            ]
        },
        'soc-036': {
            'opciones': [
                'Invertir en nutrición y desarrollo en la primera infancia genera retornos sociales y económicos elevados a largo plazo, reduciendo desigualdades de origen.',
                'Los programas de nutrición temprana representan un gasto asistencialista innecesario que debería destinarse exclusivamente a construir autopistas intermunicipales.',
                'La nutrición en los primeros años de vida no tiene relación con el rendimiento escolar posterior ni con la productividad laboral en la edad adulta.',
                'La atención de la primera infancia debe ser responsabilidad exclusiva de los hogares sin ninguna intervención ni apoyo financiero por parte del Estado.'
            ]
        },
        'soc-037': {
            'opciones': [
                'La informalidad priva a millones de trabajadores de pensión y riesgos laborales, precarizando la vejez y limitando la base tributaria del Estado colombiano.',
                'La informalidad laboral es un modelo altamente eficiente que garantiza mejores condiciones de seguridad social y ahorro pensional que el empleo formal.',
                'El trabajo informal solo afecta a trabajadores del sector rural y no tiene repercusión en las ciudades intermedias ni en las grandes capitales del país.',
                'El Estado colombiano debe sancionar penalmente con cárcel a todas las personas que laboren por cuenta propia sin un contrato formal de trabajo.'
            ]
        },
        'soc-038': {
            'opciones': [
                'La devaluación del peso encarece los bienes importados e insumos agrícolas (generando inflación), pero mejora la competitividad de las exportaciones no tradicionales.',
                'Una tasa de cambio alta beneficia a todas las empresas nacionales por igual y abarata de manera automática el costo de vida de los hogares de menores ingresos.',
                'La devaluación del peso obedece únicamente a decisiones internas de los comerciantes de barrio y no tiene relación con los mercados financieros globales.',
                'El aumento en el precio del dólar reduce la deuda externa del país en moneda extranjera y elimina la necesidad de cobrar impuestos al comercio exterior.'
            ]
        },
        'soc-039': {
            'opciones': [
                'El trabajo de cuidado no remunerado realizado mayoritariamente por mujeres sostiene el bienestar social y la economía, pero genera brechas de género e ingresos.',
                'Las tareas del hogar y cuidado no tienen ningún valor económico y deben considerarse pasatiempos recreativos sin impacto en el desarrollo del país.',
                'La distribución de las labores de cuidado en los hogares colombianos es completamente equitativa entre hombres y mujeres en todas las regiones del territorio.',
                'El Estado debe obligar a que las mujeres permanezcan en el hogar prohibiéndoles vincularse al mercado laboral formal para proteger la estructura familiar.'
            ]
        },
        'soc-040': {
            'opciones': [
                'La tragedia resulta de la interacción entre la amenaza geológica por lluvias y la vulnerabilidad social provocada por la falta de vivienda formal segura.',
                'Los deslizamientos se deben exclusivamente a factores climáticos extremos e impredecibles, siendo imposible mitigar su impacto mediante obras de ingeniería.',
                'La problemática obedece al incumplimiento de normas de zonificación por parte de los constructores de infraestructura de transporte de alta velocidad.',
                'El riesgo se origina por la falta de embalses hidroeléctricos en la parte alta de las cordilleras para regular el caudal de las lluvias estacionales.'
            ]
        }
    }

    # Apply balanced options
    for q in soc:
        qid = q['id']
        if qid in balanced:
            # check where the correct option should land based on target key
            # In balanced, the correct option is currently at index 0 of balanced[qid]['opciones']
            correct_opt = balanced[qid]['opciones'][0]
            distractor_opts = balanced[qid]['opciones'][1:]
            
            # Target key is already set on q['correcta']
            target_c = q['correcta']
            new_ops = [None] * 4
            new_ops[target_c] = correct_opt
            d_idx = 0
            for i in range(4):
                if i != target_c:
                    new_ops[i] = distractor_opts[d_idx]
                    d_idx += 1
            q['opciones'] = new_ops

        # Re-build hoja for questions 4 to 39
        idx = int(qid.split('-')[1]) - 1
        if idx >= 4:
            h = build_hoja_for_question(q)
            q['hoja'] = h
            hojas[qid] = {'modo': h['modo'], 'marcas': [], 'pasos': h['pasos']}
            guiones[qid] = h['guion']
            enfoques[qid] = h['enfoque']

    json.dump(soc, open('content/questions/sociales.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(hojas, open('content/hojas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(guiones, open('content/guiones.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(enfoques, open('content/enfoques.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print("Sociales balanced successfully.")

if __name__ == '__main__':
    balance_sociales()
