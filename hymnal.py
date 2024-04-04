# BODY OF PROCESS TO DISPLAY ONE BY ONE
# song = test['song']

# r1 = len(song['lirycs'])
# r2 = len(song['chords'])

# if r1 == r2:
#     for x in range(r1):
#         print (song['chords'][x])
#         print (song['lirycs'][x])
# 'name of the song': {
#             'name': '',
#             'tone': '',
#             'lirycs': [],
#             'chords': [],
#             'chord_image': []
#         }
from chords_dict import all_chords

hymn = { # FOR EACH LETTER OF LIRYCS YOU HAVE TO GIVE 2-4 BLANK SPACES IN CHORDS *** THE SYMBOL # WILL BE REPLACED BY A t
    'song': {
        'amor es':{
            'name': 'Amor es',
            'tone': 'Do',
            'lirycs': [
                'La gente de nuetrso tiempo',
                'no sabe lo que es el amor',
                'pues vive perdiendo el tiempo',
                'buscando y sin encontrar',
                '  ',
                '*** Coro ***',
                'Amar es entregarse',
                'en alma y cuerpo a la humanidad',
                'vivir siempre sirviendo',
                'sin que tu esperes algo para ti',
                ' ',
                ' ',
                'En Cristo, yo he encontrado',
                'un mensaje de paz y de amor',
                'La muerte del crucificado',
                'es un ejemplo de su gran amor',
                ' ',
                '*** Coro ***',
                'Amar es entregarse',
                'en alma y cuerpo a la humanidad',
                'vivir siempre sirviendo',
                'sin que tu esperes algo para ti',
                ' ',
                'Y siempre debes hablar que',
                'en Cristo hay salvacion',
                'Llevando ese mensaje',
                'de muerte y resurrección',
                ' ',
                '*** Coro ***',
                'Amar es entregarse',
                'en alma y cuerpo a la humanidad',
                'vivir siempre sirviendo',
                'sin que tu esperes algo para ti'
            ],
            'chords': [ 
                '       Do                          Rem',
                '       Sol                         Do/Sol',
                '       Do                          Rem',
                '       Sol                         Do/Sol',
                ' ',
                ' ', # CHORUS
                'Fa/Sol             Mim/Lam',
                '                   Rem/Sol                 Do/Do7',
                'Fa/Sol                     Mim/Lam',
                '                   Rem/Sol                 Do',
                ' ',
                ' ', 
                '       Do                          Rem',
                '       Sol                                 Do/Sol',
                '       Do                          Rem',
                '               Sol                         Do/Sol',
                ' ',
                ' ', # CHORUS
                'Fa/Sol             Mim/Lam',
                '                   Rem/Sol                 Do/Do7',
                'Fa/Sol                     Mim/Lam',
                '                   Rem/Sol                 Do',
                ' ',
                '       Do                          Rem',
                '       Sol                         Do/Sol',
                '       Do                          Rem',
                '       Sol                         Do/Sol',
                ' ',
                ' ', # CHORUS
                'Fa/Sol             Mim/Lam',
                '                   Rem/Sol                 Do/Do7',
                'Fa/Sol                     Mim/Lam',
                '                   Rem/Sol                 Do',
            ],
            'chord_image': [
                all_chords['Do'],all_chords['Do7'],all_chords['Rem'],all_chords['Mim'],
                all_chords['Fa'],all_chords['Sol'],all_chords['Lam']
            ]
        },
        'lo debes compartir': {
            'name': 'Lo debes compartir',
            'tone': 'Re',
            'lirycs': [
                'Con una sola chispa',
                'se enciende un fuego',
                'Y los de alrededor',
                'caliéntanse muy luego',
                ' ',
                '*** Coro ***',
                'Así es el amor de Dios',
                'esto al experimentar',
                'y este amor hay que esparcir',
                'lo debes compartir',
                ' ',
                'Las plantas al brotar',
                'en bella primavera',
                'Las aves al cantar',
                'las flores al abrirse',
                ' ',
                '*** Coro ***',
                'Nos hablan del amor de Dios',
                'y esto al experimentar',
                'a todos lo has de repetir',
                'lo debes compartir',
                ' ',
                'Deseo para ti',
                'mi amigo este gozo',
                'Confía en Dios así',
                'y hallarás reposo',
                ' ',
                '*** Coro ***',
                'De las montañas gritaré',
                'el gran mensaje de amor',
                'que a todos hay que repetir',
                'lo debes compartir'
            ],
            'chords': [
                # VERSE
                '         Re            Fa#m',
                '      Sol                  La',
                '     Re            Fa#m',
                '      Sol                    La',
                ' ',
                ' ',# CHORUS
                'Sol           Re',
                'Sol/La       Fa#m/Sim',
                '    Sol   Re        Mim      Re',
                '     Sol/La      Re   La',
                ' ',# VERSE
                '         Re            Fa#m',
                '      Sol                  La',
                '     Re            Fa#m',
                '      Sol                    La',
                ' ',
                ' ',# CHORUS
                'Sol           Re',
                'Sol/La       Fa#m/Sim',
                '    Sol   Re        Mim      Re',
                '     Sol/La      Re   La',
                ' ',# VERSE
                '         Re            Fa#m',
                '      Sol                  La',
                '     Re            Fa#m',
                '      Sol                    La',
                ' ',
                ' ',# CHORUS
                'Sol           Re',
                'Sol/La       Fa#m/Sim',
                '    Sol   Re        Mim      Re',
                '     Sol/La      Re   La'
            ],
            'chord_image': [
                all_chords['Re'],all_chords['Mim'],all_chords['FaSm'],
                all_chords['Sol'],all_chords['La'],all_chords['Sim']
            ]
        },
        'el espiritu de dios esta': {
            'name': 'El espiritu de Dios esta',
            'tone': 'Re',
            'lirycs': [
                'El espiritu de Dios esta en este lugar',
                'el espiritu de Dios se mueve en este lugar',
                'esta aquí para consolar',
                'esta aquí para liberar',
                'esta aquí para guiar, el espiritu de Dios esta aquí',
                ' ',
                '*** Coro ***',
                'Muevete en mi',
                'muevete en mi',
                'Toca mi mente, mi corazón',
                'llena mi vida de tu amor',
                'Muevete en mi',
                'Dios espiritu, muevete en mi'
            ],
            'chords': [
                # VERSE
                '           Re                    Sol                 Re',
                '                                           Sol                   La',
                '           Re                Sol',
                '           Re                Sol',
                '           Re                              La                              Re/Re7',
                ' ',
                ' ',
                # CHORUS
                '           Sol/La',
                '           Re',
                '       Sol         La',
                '       Fa#m        Sim',
                '       Mim',
                '       La          Re/Re7      Sim'
            ],
            'chord_image': [
                all_chords['Re'],all_chords['Re7'],all_chords['Mim'],
                all_chords['FaSm'],all_chords['Sol'],all_chords['La'],all_chords['Sim']
            ]
        },        
        'majestuoso': {
            'name': 'Majestuoso',
            'tone': 'Re',
            'lirycs': [
                ' ',
                ' ',
                ' ',
                'Majestuoso, poderoso',
                'digno de loor',
                'proclamemos su grandeza hoy',
                ' ',#6
                '*** Coro ***',#7
                'Jesucristo es rey',
                'Jesucristo es, es Rey',
                'postrados hoy ante sus pies',
                'Jesucristo es Rey',
                ' ',#12
                'Jesucristo es rey',
                'Jesucristo es, es Rey',
                'postrados hoy ante sus pies',
                'Jesucristo es Rey',
                '// Jesucristo es Rey //'
            ],
            'chords': [
                'Re         La      Sol    Re',
                'Sol      Fa#m  La',
                ' ',
                'Re         La      Sol    Re',
                'Sol      Fa#m  La',
                'Re           La      Sol         Re       La',
                ' ',#6
                ' ',#7
                'Sol          La      Fa#m',
                'Sol          La      Fa#m',
                'Sol                          La      Fa#m      Si',
                'Sol          La      Re/Re7',
                ' ',#12
                'Sol          La      Fa#m',
                'Sol          La      Fa#m',
                'Sol                          La      Fa#m      Si',
                'Sol          La      Re      Sim',
                '    Mim           La      Re'
            ],
            'chord_image': [
                all_chords['Re'], all_chords['Re7'], all_chords['Mim'], all_chords['FaSm'], 
                all_chords['Sol'], all_chords['Si'], all_chords['Sim']
            ]
        },
        'mi amado jesus': {
            'name': 'Mi amado Jesus',
            'tone': 'Do',
            'lirycs': [
                '// Mi amado Jesús',
                'mi compañero inseparable',
                'la confianza de mi vida',
                'es el Dios que me fortalece',
                'el motivo de mi alma eres tú //',
                ' ',
                '*** Coro ***',
                'Te amo',
                'mi Jesús, tú eres mi fuerza y mi',
                'esperanza',
                'la única esperanza es tu amor,',
                'inevitable',
                '¿a quien tengo yo',
                'en el cielo sino a ti y tu grande',
                'amor?',
                'Haz llenado mi existecia, oh',
                'Jesús',
                'mi dueño eres tú'
            ],
            'chords': [
                '    Do      Lam      Mim',
                'Fa              Sol          Do',
                'Fa                               Sol',
                '          Mim                Lam',
                'Fa                           Sol          Do',
                ' ',
                ' ',
                '      Sol',
                '        Fa                         Sol',
                '    Do',
                '      Fa            Do                  Sol',
                '    Do',
                '        Sol',
                '            Fa            Sol',
                '    Do',
                '            Fa                    Do',
                '  Sol',
                '                          Do'
            ],
            'chord_image': [
                all_chords['Do'], all_chords['Mim'], all_chords['Fa'], all_chords['Sol'],
                all_chords['Lam'],
            ]
        },
        'tu amor por mi': {
            'name': 'Tu amor por mi',
            'tone': 'La',
            'lirycs': [
                '// Tu amor por mi',
                'es más dulce que la miel',
                'y tu misericordia es',
                'nueva cada día //',
                ' ',
                '*** Coro ***',
                '// Es po eso que te alabo',
                'es por eso que te sirvo',
                'es por eso que te doy todo',
                'mi amor //'
            ],
            'chords': [
                '    Lam               Mim',
                '              Lam               Mim',
                '              Rem           Do',
                'Lam               Sol',
                ' ',
                ' ',
                '                Fa               Do',
                '             La#              Fa',
                '             Do               Rem',
                '        Sol'
            ],
            'chord_image': [
                all_chords['Do'], all_chords['Rem'], all_chords['Mim'], all_chords['Fa'], 
                all_chords['Sol'],all_chords['LaS'],all_chords['Lam']
            ]
        },
        'vine a adorar a dios': {
            'name': 'Vine a adorar a Dios',
            'tone': 'La',
            'lirycs': [
                '// Vine a adorar a Dios',
                'vine a adorar a Dios',
                'vine a adorar su santo nombre',
                'vine a adorar a Dios //',
                ' ',
                '*** Coro ***',
                'El vino a mi vida',
                'un dia muy especial',
                'cambió mi corazon',
                'me mostro su camino mejor',
                'y esa es la razón',
                'por la que canto hoy',
                ' ',
                '// Vine a adorar a Dios //'
            ],
            'chords': [
                'La  Do#m  Fa#m',
                'Re  Sim  Mi',
                'La  Do#m  Fa#m',
                'Re  Mi  La',
                ' ',
                ' ',
                'Re  Mi',
                'Do#m  Fa#m',
                'Re  Mi',
                'La  La7',
                'Re  Mi',
                'Do#m  Fa#m',
                ' ',
                'Re  Mi  La  Fa#m'
            ],
            'chord_image': [
                all_chords['DoSm'], all_chords['Re'], all_chords['Mi'],
                all_chords['FaSm'], all_chords['La'], all_chords['La7'],
                all_chords['Si']
            ]
        }
    } # THE DICTIONARY ENDS HERE
}