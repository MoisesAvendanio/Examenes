{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Primer Examen Parcial"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: A-1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Los numeros que faltan son: \n",
      "[0]\n",
      "Los numeros que estan son: \n",
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n"
     ]
    }
   ],
   "source": [
    "#Indicar cuál es el que falta.\n",
    "#En una lista de números enteros (0 < N < 9) falta un número. Indicar de cuál se trata\n",
    "#en cada caso.\n",
    "arra=[0,1,2,3,4,5,6,7,8,9,10]\n",
    "arr=[2, 1, 9, 3, 8, 7, 4, 6, 10, 5] #[1, 2, 3, 4, 5, 6, 7, 8, 9]  [2, 1, 9, 3, 8, 7, 4, 6, 0]\n",
    "esta=[]\n",
    "noesta=[]\n",
    "#for i in range(len(arra)):\n",
    "for i in arra:\n",
    "    if i in arr:\n",
    "        esta.append(i)\n",
    "    else:\n",
    "        noesta.append(i)\n",
    "if len(esta) ==len(arra):\n",
    "    print (\"No falta ninguno\")  \n",
    "else:\n",
    "    print(\"Los numeros que faltan son: \" )\n",
    "    print(noesta)\n",
    "    print(\"Los numeros que estan son: \" )\n",
    "    print(esta)\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: L - 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n",
      "[1, 3]\n",
      "[1, 3, 5]\n",
      "[1, 3, 5, 7]\n",
      "[1, 3, 5, 7, 9]\n",
      "[1, 3, 5, 7, 9, 11]\n",
      "[1, 3, 5, 7, 9, 11, 13]\n",
      "[1, 3, 5, 7, 9, 11, 13, 15]\n",
      "[1, 3, 5, 7, 9, 11, 13, 15, 17]\n",
      "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]\n"
     ]
    }
   ],
   "source": [
    "# Triángulo.\n",
    "#Utilizando ciclos (loops), “dibujar” el siguiente triángulo de 10 renglones de alto\n",
    "#únicamente con números nones.:\n",
    "num=[]\n",
    "n=1\n",
    "for i in range(0,10):\n",
    "    num.append(n)\n",
    "    print(num)\n",
    "    n=n+2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: L - 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       *\n",
      "      ***\n",
      "     *****\n",
      "    *******\n",
      "   *********\n",
      "  ***********\n",
      " *************\n",
      "***************\n"
     ]
    }
   ],
   "source": [
    "#Triángulo.\n",
    "#Utilizando ciclos (loops), “dibujar” el siguiente triángulo:\n",
    "    \n",
    "lim=8\n",
    "for i in range (lim):\n",
    "    print(' '*(lim-i-1)+'*'*(2*i+1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: AL - 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Son Primos\n",
      "[2, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]\n",
      "No son Primos\n",
      "[3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99]\n"
     ]
    }
   ],
   "source": [
    "#Primos.\n",
    "#Dentro del rango [2, 100] de números naturales, indicar cuáles son primos y cuáles no.\n",
    "prim=[2]\n",
    "noprim=[]\n",
    "for x in range(2, 100):\n",
    "    for i in range(2, x):\n",
    "        if ((x%i) != 0 and (x%3) != 0 and (x%5) != 0 and (x%7) != 0):\n",
    "            prim.append(x)\n",
    "            break\n",
    "        else:\n",
    "            noprim.append(x)\n",
    "            break \n",
    "print(\"Son Primos\")\n",
    "print(prim)\n",
    "print(\"No son Primos\")\n",
    "print(noprim)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: Fn - 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "[0, 2, 4]\n"
     ]
    }
   ],
   "source": [
    "#El enésimo número par.\n",
    "#Crear una función que regrese el enésimo número par.\n",
    "n=3  #Enesimo número par\n",
    "par=n*2-2\n",
    "print(par)\n",
    "arr=[]\n",
    "for i in range (n):\n",
    "    arr.append(i*2)\n",
    "print (arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: Fn - 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "[1, 3, 5]\n"
     ]
    }
   ],
   "source": [
    "#El enésimo número Non\n",
    "#Crear una función que regrese el enésimo número non\n",
    "n=3  #Enesimo número par\n",
    "par=n*2-1\n",
    "print(par)\n",
    "arr=[]\n",
    "for i in range (1,n+1):\n",
    "    arr.append(i*2-1)\n",
    "print (arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: A - 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[9, 12, 3]\n"
     ]
    }
   ],
   "source": [
    "#Divisible\n",
    "#Crear un programa que indique qué números de una lista son divisibles por un\n",
    "#número dado. El orden en el resultado no importa.\n",
    "num=3 #Número Dado\n",
    "arreglo=[9,12,3,0,1,4] #[1,2,3,4,5,6]   [9,12,3,0,1,4]    [10,11,3]\n",
    "arrAux=[]\n",
    "aux=0\n",
    "for i in range(len(arreglo)):\n",
    "    if((arreglo[i]%num)==0):\n",
    "        if(arreglo[i]!=0):\n",
    "            arrAux.append(arreglo[i])\n",
    "            aux=aux+1\n",
    "if(range(len(arrAux))==0):\n",
    "    print(\"No hay ningun valor divisible entre \"+num)\n",
    "else:\n",
    "    print(arrAux)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: A - 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "-65\n"
     ]
    }
   ],
   "source": [
    "#Cuenta de positivos / Suma de negativos\n",
    "#Dado un arreglo de números enteros, indicar el conteo de números positivos y la\n",
    "#suma de los números negativos. El número 0 (cero) no cuenta.\n",
    "\n",
    "arr=[1, 2, 3, 4, 5, 6, -11, -12, -13, -14, -15] # [1, 2, 3, 4, 5, 6, -11, -12, -13, -14, -15] “6 positivos, -65 la suma de negativos\n",
    "#[9, -8, 2, 1, -2] -> “3 positivos, -10 la suma de negativos”\n",
    "conta=0\n",
    "suma=0\n",
    "for i in range(len(arr)):\n",
    "    if(arr[i]>0):\n",
    "        conta+=1\n",
    "    elif(arr[i]<0):\n",
    "        suma=suma+arr[i]\n",
    "print(conta)   \n",
    "print(suma)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# # Clave: A - 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Promedios\n",
    "#En una lista de calificaciones, determinar el porcentaje de alumnos que aprobaron el\n",
    "#curso. Se considera una calificación aprobatoria si es igual o mayor a 6\n",
    "def aprovados(valores):\n",
    "    resultado = 0.0\n",
    "    for x in range(0,len(valores)):\n",
    "        if(valores[x]>5):\n",
    "            resultado +=1\n",
    "    prom=resultado/(len(valores)) \n",
    "    return prom*100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19.999999999999996%\n"
     ]
    }
   ],
   "source": [
    "a=[9, 8, 7, 5, 2, 10]\n",
    "b=[5, 5, 5, 5, 5, 5]\n",
    "c=[0, 1, 2]\n",
    "d=[4, 2, 4, 5, 7, 8]\n",
    "e=[1, 1, 1, 1]\n",
    "prom=(aprovados(a)+aprovados(b)+aprovados(c)+aprovados(d)+aprovados(e))/5\n",
    "print(str(prom)+\"%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: A - 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6]\n"
     ]
    }
   ],
   "source": [
    "#Divisible\n",
    "#Crear un programa que indique qué números de una lista son divisibles por un\n",
    "#número dado. El orden en el resultado no importa.\n",
    "num=2 #Número Dado\n",
    "arreglo=[1,2,3,4,5,6] #[1,2,3,4,5,6]   [9,12,3,0,1,4]    [10,11,3]\n",
    "arrAux=[]\n",
    "aux=0\n",
    "for i in range(len(arreglo)):\n",
    "    if((arreglo[i]%num)==0):\n",
    "        if(arreglo[i]!=0):\n",
    "            arrAux.append(arreglo[i])\n",
    "            aux=aux+1\n",
    "if(range(len(arrAux))==0):\n",
    "    print(\"No hay ningun valor divisible entre \"+num)\n",
    "else:\n",
    "    print(arrAux)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: Fn - 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2]\n"
     ]
    }
   ],
   "source": [
    "#Únicos\n",
    "#Crear una función que remueva los elementos repetidos en un arreglo y regrese un\n",
    "#nuevo arreglo con los elementos restantes.\n",
    "arr=[9,3,1,3,2,9]\n",
    "arrnew = []\n",
    "conta=0\n",
    "for j in range (len(arr)):\n",
    "    conta=0\n",
    "    for i in range (0,len(arr)):\n",
    "        if( arr[j]==arr[i]):\n",
    "            conta=conta+1 \n",
    "    if(conta==1):   \n",
    "        arrnew.append(arr[j])\n",
    "print(arrnew)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: Fn - 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Suma de promedios\n",
    "#Programar una función que sume los promedios de los arreglos en una lista.\n",
    "def Promedio(valores):\n",
    "    resultado = 0.0\n",
    "    for x in range(0,len(valores)):\n",
    "            resultado = resultado + valores[x]\n",
    "            #print(resultado)\n",
    "    prom=resultado/(len(valores))      \n",
    "    return prom"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "44.2\n"
     ]
    }
   ],
   "source": [
    "a=[3, 4, 1, 3, 5, 1, 4]\n",
    "b=[21, 54, 33, 21, 77]\n",
    "print(Promedio(a)+Promedio(b))\n",
    "#promedio([[3, 4, 1, 3, 5, 1, 4], [21, 54, 33, 21, 77]]) // 44.2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: Fn - 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Encuentra a los líderes\n",
    "#Un número será “líder” si es mayor al promedio del resto en una lista. Crear una\n",
    "#función que dado un arreglo de al menos 3 números enteros (mayores o iguales a 0),\n",
    "#regrese el número líder.\n",
    "def promedioExepto(valores,pos):\n",
    "    resultado = 0.0\n",
    "    for x in range(0,len(valores)):\n",
    "        if x != pos:\n",
    "            resultado = resultado + valores[x]\n",
    "    regresa=resultado/(len(valores)-1)      \n",
    "    return regresa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def sacaLider(listas):\n",
    "    anterior=-1\n",
    "    resultado=[]\n",
    "    for i in range(0,len(listas)):\n",
    "        if listas[i] > promedioExepto(listas,i):\n",
    "            resultado.append(listas[i])\n",
    "            anterior=listas[i]\n",
    "    if anterior >= 0:\n",
    "        return resultado\n",
    "    else:\n",
    "        print(\"No hay lider\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10]\n",
      "[5]\n",
      "[4]\n"
     ]
    }
   ],
   "source": [
    "a =[3,2,10,1]#10\n",
    "b=[5,0,1,2]#5\n",
    "c=[1,1,4,1]#4\n",
    "\n",
    "#print(promedioExepto(lider,0))\n",
    "print(sacaLider(a))\n",
    "print(sacaLider(b))\n",
    "print(sacaLider(c))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Clave: Fn - 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "#Suma de diferencias\n",
    "#Escribir una función que sume las diferencias entre números consecutivos en un\n",
    "#arreglo. Los números en el arreglo se encuentran ordenados descendentemente.\n",
    "arr=[11, 10, 5]  #[10, 2, 1]   [11, 10, 5]   [4, 3, 2, 1]\n",
    "\n",
    "for i in range (len(arr)):  \n",
    "    dif=arr[0]\n",
    "    dif=dif-arr[i]\n",
    "print(dif)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
