from main import Estudo, adiciona_conteudo
import pytest, json

# Given When Then

json_teste = """
{
    "ciclos" : [["Red", "Fis", "Lit"], ["Mat", "Hist", "Geo"], ["Qui", "Bio", "Filo/Socio"]],
    "historico" : {
        "1" : {
            "Redação" : "Introdução",
            "Física" : "Gravitação universal",
            "Literatura" : "Parnasianismo e Romantismo"
        },
        "2" : {
            "Matemática" : "Geometria Plana e Espacial",
            "História" : "Introdução à História",
            "Geografia" : "Relevo brasileiro"
        },
        "3" : {
            "Química" : "Estequiometria",
            "Biologia" : "Mitose e Meiose",
            "Filo/Socio" : "Kant e Marx"
        },
        "4" : {
            "Redação" : "Desenvolvimento",
            "Física" : "Elevadores e elasticidade",
            "Literatura" : "Simbolismo e Realismo"
        },
        "5" : {
            "Matemática" : "Aritmética e Logaritmo",
            "História" : "Grandes Navegações",
            "Geografia" : "Hidrografia"
        },
        "6" : {
            "Química" : "Pilhas e Eletrodos",
            "Biologia" : "Genética",
            "Filo/Socio" : "Rousseau e Hegel"
        },
        "7" : {
            "Redação" : "Conclusão",
            "Física" : "MRU e MRUV",
            "Literatura" : "Trovadorismo"
        },
        "8" : {
            "Matemática" : "Matrizes e Produtos notáveis",
            "História" : "Feudalismo",
            "Geografia" : "Blocos econômicos"
        },
        "9" : {
            "Química" : "Alcoois e Cetonas",
            "Biologia" : "Fisiologia humana",
            "Filo/Socio" : "Filosofia Moderna"
        }
    }
}
"""

class TestClass:
    def test_quando_json_for_teste_estudo_atual_deve_ter_turno_10_e_ciclo_Red_Fis_Lit(self):
        json_string_teste = """
{
    "ciclos" : [["Red", "Fis", "Lit"], ["Mat", "Hist", "Geo"], ["Qui", "Bio", "Filo/Socio"]],
    "historico" : {
        "1" : {
            "Redação" : "Introdução",
            "Física" : "Gravitação universal",
            "Literatura" : "Parnasianismo e Romantismo"
        },
        "2" : {
            "Matemática" : "Geometria Plana e Espacial",
            "História" : "Introdução à História",
            "Geografia" : "Relevo brasileiro"
        },
        "3" : {
            "Química" : "Estequiometria",
            "Biologia" : "Mitose e Meiose",
            "Filo/Socio" : "Kant e Marx"
        },
        "4" : {
            "Redação" : "Desenvolvimento",
            "Física" : "Elevadores e elasticidade",
            "Literatura" : "Simbolismo e Realismo"
        },
        "5" : {
            "Matemática" : "Aritmética e Logaritmo",
            "História" : "Grandes Navegações",
            "Geografia" : "Hidrografia"
        },
        "6" : {
            "Química" : "Pilhas e Eletrodos",
            "Biologia" : "Genética",
            "Filo/Socio" : "Rousseau e Hegel"
        },
        "7" : {
            "Redação" : "Conclusão",
            "Física" : "MRU e MRUV",
            "Literatura" : "Trovadorismo"
        },
        "8" : {
            "Matemática" : "Matrizes e Produtos notáveis",
            "História" : "Feudalismo",
            "Geografia" : "Blocos econômicos"
        },
        "9" : {
            "Química" : "Alcoois e Cetonas",
            "Biologia" : "Fisiologia humana",
            "Filo/Socio" : "Filosofia Moderna"
        }
    }
}
"""
        save_dict = json.loads(json_string_teste) # Given
        esperado = [10, ["Red", "Fis", "Lit"]]

        estudo_teste = Estudo(save_dict)
        turno_teste = estudo_teste.turno
        ciclo_teste = estudo_teste.ciclo # When

        assert [turno_teste, ciclo_teste] == esperado

    def test_adiciona_conteudo_json_quando_ultimo_turno_for_10_deve_adicionar_turno_11_e_conteudos(self):
        # Given
        json_dado = """
{
    "ciclos" : [["Redação", "Física", "Literatura"], ["Matemática", "História", "Geografia"], ["Química", "Biologia", "Filo/Socio"]],
    "historico" : {
        "001" : {
            "Redação" : "Introdução",
            "Física" : "Gravitação universal",
            "Literatura" : "Parnasianismo e Romantismo"
        },
        "002" : {
            "Matemática" : "Geometria Plana e Espacial",
            "História" : "Introdução à História",
            "Geografia" : "Relevo brasileiro"
        }
    }
}
"""
        json_dict = json.loads(json_dado)
        lista_conteudo = ["Estequiometria", "Mitose e Meiose", "Kant e Marx"]
        dict_esperado = json.loads("""
{
    "ciclos" : [["Redação", "Física", "Literatura"], ["Matemática", "História", "Geografia"], ["Química", "Biologia", "Filo/Socio"]],
    "historico" : {
        "001" : {
            "Redação" : "Introdução",
            "Física" : "Gravitação universal",
            "Literatura" : "Parnasianismo e Romantismo"
        },
        "002" : {
            "Matemática" : "Geometria Plana e Espacial",
            "História" : "Introdução à História",
            "Geografia" : "Relevo brasileiro"
        },
        "003" : {
            "Química" : "Estequiometria",
            "Biologia" : "Mitose e Meiose",
            "Filo/Socio" : "Kant e Marx"
        }
    }
}
        """)

        # When
        obj_estudo = Estudo(json_dict)
        dict_final = adiciona_conteudo(obj_estudo, lista_conteudo, json_dict)

        # Then
        assert dict_final == dict_esperado