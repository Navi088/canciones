# BODY OF PROCESS TO DISPLAY ONE BY ONE
# song = test['song']

# r1 = len(song['lirycs'])
# r2 = len(song['chords'])

# if r1 == r2:
#     for x in range(r1):
#         print (song['chords'][x])
#         print (song['lirycs'][x])
from chords_dict import all_chords

hymn = { # FOR EACH LETTER OF LIRYCS YOU HAVE TO GIVE 2-4 BLANK SPACES IN CHORDS
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
                all_chords['Do'],all_chords['Do7'],all_chords['Rem'],all_chords['Mim'],all_chords['Fa'],all_chords['Sol'],all_chords['Lam']
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
                all_chords['Re'],all_chords['Mim'],all_chords['Fa#m'],all_chords['Sol'],all_chords['La'],all_chords['Sim']
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
                all_chords['Re'],all_chords['Re7'],all_chords['Mim'],all_chords['Fa#m'],all_chords['Sol'],all_chords['La'],all_chords['Sim']
            ]
        }
    }
}