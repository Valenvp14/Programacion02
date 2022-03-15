class VistasDeAxiomas:
    def mostrar(self):
        pass
    def escojeAxioma(self,):
        vResult = None
        vResult = int(input("Tipee el nro. de axioma que quiere ver: "))
        if vResult >= 1 and vResult <= 5:
            return vResult
        else:
            return "El número introducido no se encuentra en la lista"

class vistaAxiomasPorTerminal(VistasDeAxiomas):
    def mostrar(self,vAxioma):
        print("y el axioma es: ", vAxioma)

class vistaAxiomasHTML(VistasDeAxiomas):
    def mostrar(self, vAxioma):
        vArchivoHtml = open('vistaMVC.html', 'w')

        vPlantilla = """
        <html>
        <head>
        <title> Telematica - Prog2 </title>
        </head>
        <body> 
        <h1>Modelo-Vista-Controlador (MVC)</h1>
        <h2>Vista html</h2>
        <table border="1">
        <tbody>
        <tr>
        <td>y el Axioma es: </td>
        </tr>
        <tr>
        <td>        
        """
        vPlantilla += vAxioma
        vPlantilla += """
        </td>
        </tr>
        </tbody>
        </table>
        </body>
        </html>
        """

        vArchivoHtml.write(vPlantilla)
        vArchivoHtml.close()
