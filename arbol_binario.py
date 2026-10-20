class NodoArbol:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.root = None

    def insertar(self,dato):
        if not self.root:
            self.root = NodoArbol(dato)
        else:
            self.insertar_recursivo(self.root,dato)
    
    def insertar_recursivo(self,nodo,dato):
        if dato < nodo.data:
            if nodo.left == None:
                nodo.left = NodoArbol(dato)
            else:
                self.insertar_recursivo(nodo.left,dato)
        else: #dato > nodo.data o es igual
            if nodo.right == None: #no es nodo Hoja 
                nodo.right = NodoArbol(dato)
            else:
                self.insertar_recursivo(nodo.right,dato)
    def recorrido_inorder(self, nodo):
        if nodo != None:
            self.recorrido_inorder(nodo.left)
            print(nodo.data)
            self.recorrido_inorder(nodo.right)
    
    def recorrido_preorden(self, nodo):
        if nodo != None:
            print(nodo.data)
            self.recorrido_preorden(nodo.left)
            self.recorrido_preorden(nodo.right)
    
    def recorrido_postorden(self, nodo):
        if nodo != None:
            self.recorrido_postorden(nodo.left)
            self.recorrido_postorden(nodo.right)
            print(nodo.data)
    
    def _construir_lineas_ascii(self,nodo):
    
        if nodo is None:
            return [], 0, 0

        etiqueta = str(nodo.data)
        len_etiq = len(etiqueta)

        # Caso 1: Hoja
        if nodo.left is None and nodo.right is None:
            return [etiqueta], len_etiq, len_etiq // 2

        # Caso 2: Solo hijo izquierdo
        if nodo.right is None:
            lineas_izq, n_izq, p_izq = self._construir_lineas_ascii(nodo.left)
            espacio_izq = p_izq + 1
            pos_raiz = n_izq
            
            linea_raiz = " " * espacio_izq + "_" * (n_izq - espacio_izq) + etiqueta
            linea_rama = " " * p_izq + "/" + " " * (pos_raiz - p_izq - 1 + len_etiq)
            
            lineas_unificadas = [linea_raiz, linea_rama] + [l + " " * len_etiq for l in lineas_izq]
            return lineas_unificadas, len(linea_raiz), pos_raiz + len_etiq // 2

        # Caso 3: Solo hijo derecho
        if nodo.left is None:
            lineas_der, n_der, p_der = self._construir_lineas_ascii(nodo.right)
            linea_raiz = etiqueta + "_" * p_der + " " * (n_der - p_der)
            linea_rama = " " * (len_etiq + p_der) + "\\" + " " * (n_der - p_der - 1)
            
            lineas_unificadas = [linea_raiz, linea_rama] + [" " * len_etiq + l for l in lineas_der]
            return lineas_unificadas, len(linea_raiz), len_etiq // 2

        # Caso 4: Ambos hijos presentes
        lineas_izq, n_izq, p_izq = self._construir_lineas_ascii(nodo.left)
        lineas_der, n_der, p_der = self._construir_lineas_ascii(nodo.right)

        pos_raiz = n_izq + 1
        len_total_raiz = n_izq + 1 + len_etiq + 1 + n_der

        linea_raiz = (
            " " * (p_izq + 1)
            + "_" * (n_izq - p_izq - 1)
            + " "
            + etiqueta
            + " "
            + "_" * p_der
            + " " * (n_der - p_der)
        )
        linea_rama = (
            " " * p_izq
            + "/"
            + " " * (n_izq - p_izq - 1 + 1 + len_etiq + 1 + p_der)
            + "\\"
            + " " * (n_der - p_der - 1)
        )

        # Rellenar con espacios para igualar la altura de ambos subarboles
        dif_altura = len(lineas_izq) - len(lineas_der)
        if dif_altura > 0:
            lineas_der.extend([" " * n_der] * dif_altura)
        elif dif_altura < 0:
            lineas_izq.extend([" " * n_izq] * (-dif_altura))

        subarboles_pegados = [
            li + " " * (len_etiq + 2) + ld for li, ld in zip(lineas_izq, lineas_der)
        ]
        
        return [linea_raiz, linea_rama] + subarboles_pegados, len(linea_raiz), pos_raiz + len_etiq // 2

    def imprimir_arbol_centrado(self,raiz):
        if raiz is None:
            print("(Arbol vacio)")
            return
        lineas, _, _ = self._construir_lineas_ascii(raiz)
        for linea in lineas:
            print(linea)
if(__name__ == "__main__"):
    abb = ArbolBinarioBusqueda()
    abb.insertar(10)
    abb.insertar(5)
    abb.insertar(15)
    abb.insertar(3)
    abb.insertar(7)
    abb.insertar(12)
    abb.insertar(18)
    #abb.recorrido_inorder(abb.root)
    #abb.recorrido_postorden(abb.root)
    abb.recorrido_preorden(abb.root)
    abb.imprimir_arbol_centrado(abb.root)
    