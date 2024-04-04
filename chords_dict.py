import os

urlfiles = 'static/css/chords'
img_list = list(os.listdir(urlfiles))


all_chords = {

    'Do': img_list[0],
    'Dom': img_list[2],
    'Do7': img_list[1],
    'Dom7': img_list[3],
    'DoS': img_list[4],
    'DoSm': img_list[5],
    
    'Re': img_list[22],
    'Rem': img_list[24],
    'Re7': img_list[23],
    'Rem7': img_list[25],
    'ReS': img_list[26],
    'ReSm': img_list[27],
    
    'Mi': img_list[18],
    'Mim': img_list[20],
    'Mi7': img_list[19],
    'Mim7': img_list[21],
    
    'Fa': img_list[6],
    'Fam': img_list[8],
    'Fa7': img_list[7],
    'Fam7': img_list[9],
    'FaS': img_list[10],
    'FaSm': img_list[11],
    
    'Sol': img_list[32],
    'Solm': img_list[34],
    'Sol7': img_list[33],
    'Solm7': img_list[35],
    'SolS': img_list[36],
    'SolSm': img_list[37],
    
    'La': img_list[12],
    'Lam': img_list[14],
    'La7': img_list[13],
    'Lam7': img_list[15],
    'LaS': img_list[16],
    'LaSm': img_list[17],
    
    'Si': img_list[28],
    'Sim': img_list[30],
    'Si7': img_list[29],
    'Sim7': img_list[31]

}