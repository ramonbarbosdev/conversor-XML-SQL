import xml.etree.ElementTree as ET
import time
import conexao
import pyodbc


#arquivo XML
xml_file = r"C:\Users\W5IRamon\Desktop\PRODUTO.xml"

def importar_xml_para_sql(xml_file, tabela):
    conn = None
    try:

        conn = conexao.obter_conexao()
        with conn.cursor() as cursor:

            tree = ET.parse(xml_file)
            root = tree.getroot()

            #ex: tag <PATRIMONIO>
            for patrimonio in root.findall(".//PRODUTO"):
                colunas = []
                valores = []

                for elemento in patrimonio:
                    colunas.append(elemento.tag)
                    valores.append(elemento.text)

                colunas_sql = ", ".join(colunas)
                placeholders = ", ".join(["?"] * len(colunas))
                query = f"INSERT INTO {tabela} ({colunas_sql}) VALUES ({placeholders})"

                try:
                    cursor.execute(query, valores)
                except pyodbc.Error as e:
                    print(f"Erro ao inserir dados: {e}. Dados ignorados: {valores}")

            conn.commit()
            print("Importação concluída com sucesso!")

    except ET.ParseError as e:
        print(f"Erro ao processar o XML: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()
            print("Conexão fechada.")

tabela_sql = "PRODUTO"

importar_xml_para_sql(xml_file, tabela_sql)
