class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Encuentra el prefijo común más largo en una lista de palabras.
        
        :param strs: Lista de palabras
        :type strs: List[str]
        :return: Prefijo común más largo
        :rtype: str
        """
        if not strs:  # Si la lista está vacía
            return ""  # El prefijo común también es vacío.

        # Calculamos la longitud de la cadena más corta en la lista para recorrer solo hasta esa cantidad de caracteres.
        min_length = min(len(s) for s in strs)  # Encontramos la longitud mínima entre todas las cadenas.
        result = ""  # Inicializamos el resultado como una cadena vacía.

        # Recorremos todas las posiciones de las letras en las palabras.
        for i in range(min_length):
            # Tomamos la letra en la posición i de la primera palabra en la lista y la consideramos como la primera letra en común.
            common_char = strs[0][i]

            # Recorremos cada cadena en la lista.
            for j in strs:
                # Si la letra en la posición i de la cadena j es diferente a common_char, no hay un prefijo común en esta posición.
                if j[i] != common_char:
                    return result  # Retornamos el prefijo común encontrado hasta ahora.

            result += common_char  # Si todas las letras en la posición i son iguales, agregamos esa letra al resultado común.

        return result  # Retornamos el prefijo común más largo encontrado.

# Crear una instancia de la clase Solution
solution = Solution()

# Lista de palabras de ejemplo
strs = ["flower", "flow", "flight"]

# Imprimir el resultado de encontrar el prefijo común más largo en la lista de palabras
print(solution.longestCommonPrefix(strs))