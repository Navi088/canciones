import os

urlfiles = 'static/css/chords'
img_list = list(os.listdir(urlfiles))


all_chords = {

    'Do': img_list[2],
    'Dom': img_list[4],
    'Do7': img_list[3],
    'Dom7': img_list[5],
    'Do#': img_list[0],
    'Do#m': img_list[1],
    
    'Re': img_list[24],
    'Rem': img_list[26],
    'Re7': img_list[25],
    'Rem7': img_list[27],
    'Re#': img_list[22],
    'Re#m': img_list[23],
    
    'Mi': img_list[18],
    'Mim': img_list[20],
    'Mi7': img_list[19],
    'Mim7': img_list[21],
    
    'Fa': img_list[8],
    'Fam': img_list[10],
    'Fa7': img_list[9],
    'Fam7': img_list[11],
    'Fa#': img_list[6],
    'Fa#m': img_list[7],
    
    'Sol': img_list[34],
    'Solm': img_list[36],
    'Sol7': img_list[35],
    'Solm7': img_list[37],
    'Sol#': img_list[32],
    'Sol#m': img_list[33],
    
    'La': img_list[14],
    'Lam': img_list[16],
    'La7': img_list[15],
    'Lam7': img_list[17],
    'La#': img_list[12],
    'La#m': img_list[13],
    
    'Si': img_list[28],
    'Sim': img_list[30],
    'Si7': img_list[29],
    'Sim7': img_list[31]

}