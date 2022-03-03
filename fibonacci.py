def metodofib(n):
   if n <= 1:
       return n
   else:
       return(metodofib(n-1) + metodofib(n-2))

NumeroSecuencia = 10

if NumeroSecuencia <= 0:
   print("pon un numero positivo")
else:
   print("secuencia fibonacci de {NumeroSecuencia}:".format (NumeroSecuencia=NumeroSecuencia))
   for i in range(NumeroSecuencia):
       print(metodofib(i))