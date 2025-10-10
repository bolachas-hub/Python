
seg = int(input("Digite o tempo em segundos: "))


hrs = seg // 3600  
rst_seg = seg % 3600  
minutos = rst_seg // 60  
seg_final = rst_seg % 60  


print(f"{hrs} hora(s), {minutos} minuto(s) e {seg_final} segundo(s)")