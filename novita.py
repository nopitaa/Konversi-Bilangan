try :
    print ('***** UJIAN SEKOLAH DP1-DP3 *****')
    print ('Konversi dari :')
    print ('1. Desimal')
    print ('2. Biner')
    print ('3. Oktal')
    print ('4. Hexadecimal')
    print ('5. ASCII')
    print ('0. exit')

    masukan = int (input('Masukan pilihan : '))
    print ('')

    while masukan > 4 or masukan < 0 : #mengecek inputan pemilihan menu
        print ('Silahkan masukan angka yang ada pada menu.')
        masukan = int (input('Masukan pilihan : '))
        print ('')
        
    while masukan != 0 :
        tampil = ''
        biner = 0
        hexa = 0
        pembalik = []
        cetak = []

        #KONVERSI HEXADECIMAL
        if masukan == 1: 
            print ('')
            print ('Konvert ke')
            print ('1. Biner')
            print ('2. Oktal')
            print ('3. Hexadecimal')
            print ('')
            menu = int (input('Masukan pilihan : '))
            print ('')
            while menu > 4 or menu < 0 :
                print ('Silahkan masukan angka yang ada pada menu.')
                menu = int (input('Masukan pilihan : '))
                print ('')
            
            #DECIMAL TO BINER
            if menu == 1:
                desimal = int (input('Masukan angka desimal:'))
                print ('')
                while desimal != 0:
                    hasil = desimal % 2 
                    cetak.insert(0, str(hasil)) 
                    desimal = desimal//2 
                    if desimal == 0:
                        for i in range (len(cetak)):
                            tampil +=  cetak[i]
                print ('Hasilnya adalah : ', tampil)
                print ('')
                
            #DECIMAL TO OKTAL
            elif menu == 2:
                desimal = int (input('Masukan angka desimal :'))
                print ('')
                while desimal != 0:
                    hasil = desimal % 8 
                    cetak.insert(0, str(hasil)) 
                    desimal = desimal//8  
                    if desimal == 0:
                        for i in range (len(cetak)): 
                            tampil +=  cetak[i]
                print ('Hasilnya adalah : ', tampil)
                print ('')
                
            # DECIMALTO HEX
            elif menu == 3:
                desimal = int (input('Masukan angka desimal :'))
                print ('')
                while desimal != 0:
                    hasil = desimal % 16 
                    if hasil == 10:
                        hasil = 'A'
                    if hasil == 11:
                        hasil = 'B'
                    if hasil == 12:
                        hasil = 'C'
                    if hasil == 13:
                        hasil = 'D'
                    if hasil == 14:
                        hasil = 'E'
                    if hasil == 15:
                        hasil = 'F'
                    cetak.insert(0, str(hasil))
                    desimal = desimal//16  
                    if desimal == 0:
                        for i in range (len(cetak)): 
                            tampil +=  cetak[i]
                print ('Hasilnya adalah : ',tampil)
                print ('')

              #KONVERSI BINER  
        elif masukan == 2:
            print ('Konvert ke')
            print ('1. Desimal')
            print ('2. Oktal')
            print ('3. Hexadecimal')
            menu = int (input('Masukan pilihan :'))
            print ('')

            while menu > 4 or menu < 0 :
                print ('Silahkan masukan angka yang ada pada menu.')
                menu = int (input('Masukan pilihan : '))
                print ('')
            
            #BINER TO DECIMAL
            if menu == 1:
                bin = input('Masukan biner :')
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i]) #membalikkan biner
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(2**i)
                print('Hasilnya adalah : ',biner)
                print ('')

                #BINER TO OKTAL
            if menu == 2:
                bin = input('Masukan biner :')
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(2**i)
                
                while biner != 0:
                    hasil = biner % 8
                    cetak.insert(0, str(hasil))
                    biner = biner//8
                    if biner == 0:
                        for i in range (len(cetak)):
                            tampil +=  cetak[i]
                print ('Hasilnya adalah : ',tampil)
                print ('')

                #BINER TO HEXA
            if menu == 3:
                bin = input('Masukan biner :')
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(2**i)

                while biner != 0:
                    hasil = biner % 16
                    if hasil == 10:
                        hasil = 'A'
                    if hasil == 11:
                        hasil = 'B'
                    if hasil == 12:
                        hasil = 'C'
                    if hasil == 13:
                        hasil = 'D'
                    if hasil == 14:
                        hasil = 'E'
                    if hasil == 15:
                        hasil = 'F'
                    cetak.insert(0, str(hasil))
                    biner = biner//16
                    if biner == 0:
                        for i in range (len(cetak)):
                            tampil +=  cetak[i]
                print ('hasilnya adalah : ',tampil)
                print ('')

        #KONVERSI OKTAL
        elif masukan == 3:
            print ('Konvert ke')
            print ('1. Desimal')
            print ('2. Biner')
            print ('3. Hexadecimal')
            menu = int (input('Masukan pilihan :'))
            print ('')
            
            while menu > 4 or menu < 0 :
                print ('Silahkan masukan angka yang ada pada menu.')
                menu = int (input('Masukan pilihan : '))
                print ('')
            
            #OKTAL TO DECIMAL
            if menu == 1:
                bin = input('Masukan oktal :')
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(8**i)
                print('Hasilnya adalah : ', biner)
                print ('')

            #OKTAL TO BINER
            if menu == 2:
                bin = input('Masukan oktal :')
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(8**i)

                while biner != 0:
                    hasil = biner % 2
                    cetak.insert(0, str(hasil))
                    biner = biner//2
                    if biner == 0:
                        for i in range (len(cetak)):
                            tampil +=  cetak[i]
                print ('Hasilnya adalah : ',tampil)
                print ('')
            #OKTAL TO HEXA 
            if menu == 3:
                bin = input('Masukan oktal :')
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(8**i)

                while biner != 0:
                    hasil = biner % 16
                    if hasil == 10:
                        hasil = 'A'
                    if hasil == 11:
                        hasil = 'B'
                    if hasil == 12:
                        hasil = 'C'
                    if hasil == 13:
                        hasil = 'D'
                    if hasil == 14:
                        hasil = 'E'
                    if hasil == 15:
                        hasil = 'F'
                    cetak.insert(0, str(hasil))
                    biner = biner//16
                    if biner == 0:
                        for i in range (len(cetak)):
                            tampil +=  cetak[i]
                print ('Hasilnya adalah : ',tampil)
                print ('')
        #KONVERSI HEXADECIMAL       
        elif masukan == 4:
            print ('Konvert ke')
            print ('1. Desimal')
            print ('2. Biner')
            print ('3. Oktal')
            menu = int (input('Masukan pilihan :'))
            print ('')


            while menu > 4 or menu < 0 :
                print ('Silahkan masukan angka yang ada pada menu.')
                menu = int (input('masukan pilihan : '))
                print ('')
            
            #HEXA TO DECIMAL 
            if menu == 1:
                bin = input('Masukan hexa :')
                print ('')
                for i in range (len(bin)):
                    if bin[i] == 'A' or bin[i] == 'a':
                        hasil = 10
                    if bin[i] == 'B' or bin[i] == 'b':
                        hasil = 11
                    if bin[i] == 'C' or bin[i] == 'c':
                        hasil = 12
                    if bin[i] == 'D' or bin[i] == 'd':
                        hasil = 13
                    if bin[i] == 'E' or bin[i] == 'e':
                        hasil = 14
                    if bin[i] == 'F' or bin[i] == 'f':
                        hasil = 15
                    hexa += hasil*(16**i)
                print('Hasilnya adalah : ',hexa)
                print ('')
            
            #HEXA TO BINER
            if menu == 2:
                bin = input('Masukan biner :')

                for i in range (len(bin)) :
                    if bin[i] != 'a' or bin[i] != 'b' or bin[i] != 'c' or bin[i] != 'd' or bin[i] != 'e' or bin[i] != 'f' :
                        a = False;
                    else :
                        a = True

                while a == False :
                    for i in range (len(inputan)) :
                        if inputan[i] != 'a' or inputan[i] != 'b' or inputan[i] != 'c' or inputan[i] != 'd' or inputan[i] != 'e' or inputan[i] != 'f' :
                            a = False;
                            break
                        else :
                            a = True
                        
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i]) #membalikkan biner
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(2**i)
                

                
                for i in range (len(bin)):
                    if bin[i] == 'A':
                        hasil = 10
                    if bin[i] == 'B':
                        hasil = 11
                    if bin[i] == 'C':
                        hasil = 12
                    if bin[i] == 'D':
                        hasil = 13
                    if bin[i] == 'E':
                        hasil = 14
                    if bin[i] == 'F':
                        hasil = 15
                    hexa += hasil*(16**i)

                while hexa != 0:
                    hasil = hexa % 2
                    cetak.insert(0, str(hasil))
                    hexa = hexa//2
                    if hexa == 0:
                        for i in range (len(cetak)):
                            tampil +=  cetak[i]
                print ('Hasilnya adalah : ',tampil)
                print ('')
            
            #HEXA TO OKTAL
            if menu == 3:
                bin = input('Masukan hexa :')
                print ('')
                for i in range (len(bin)):
                    if bin[i] == 'A':
                        hasil = 10
                    if bin[i] == 'B':
                        hasil = 11
                    if bin[i] == 'C':
                        hasil = 12
                    if bin[i] == 'D':
                        hasil = 13
                    if bin[i] == 'E':
                        hasil = 14
                    if bin[i] == 'F':
                        hasil = 15
                    hexa += hasil*(16**i)

                while hexa != 0:
                    hasil = hexa % 8
                    cetak.insert(0, str(hasil))
                    hexa = hexa//8
                    if hexa == 0:
                        for i in range (len(cetak)):
                            tampil +=  cetak[i]
                print ('Hasilnya adalah : ',tampil)
                print ('')

        #KONVERSI ASCII
        elif masukan == 5:
            string = input("Masukkan string yang ingin dikonversi ke ASCII: ")

            # STRING TO ASCII
            ascii_result = ""
            for char in string:
                ascii_result += str(ord(char)) + " "
            print("ASCII: ", ascii_result)

            # STRING TO DESIMAL
            decimal_result = ""
            for char in string:
                decimal_result += str(ord(char)) + " "
            print("Desimal: ", decimal_result)

            # STRING TO BINER
            binary_result = ""
            for char in string:
                binary_result += bin(ord(char))[2:] + " "
            print("Biner: ", binary_result)

            # STRING TO OKTAL
            octal_result = ""
            for char in string:
                octal_result += oct(ord(char))[2:] + " "
            print("Oktal: ", octal_result)

            # STRING TO HEXADESIMAL
            hex_result = ""
            for char in string:
                hex_result += hex(ord(char))[2:] + " "
            print("Hexadesimal: ", hex_result) 
        
        print('***** UJIAN SEKOLAH DP1-DP3 *****')
        print('Konversi dari :')
        print ('1. Desimal')
        print ('2. Biner')
        print('3. Oktal')
        print ('4. Hexadecimal')
        print ('0. exit')
        masukan = int (input('Masukan pilihan : '))
        print ('')
        
except :
    print ('Anda memasukan inputan yang salah. Maaf program terhenti.')
