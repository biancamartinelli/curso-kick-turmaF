var cidadePorEstado = {
    SP: ["São Paulo", "Campinas", "Santos"],
    RJ:["Rio de Janeiro", "Angra", "Volta Redonda"],
    MG:["Belo Horizonte", "Viçosa", "Juiz de Fora"],
};

function mostraCidades(){
    var estadoSelect = document.getElementById("estado")
    var cidadeSelect = document.getElementById("cidade")

    cidadeSelect.innerHTML = ""

    var estadoSelecionado = estadoSelect.value

    if(estadoSelecionado){
        var cidades = cidadesPorEstado[estadoSelecionado]
        if(cidades){
            cidades.forEach(function(cidade){
                adicionarCidade(cidade, cidadeSelect);
            });
        }
    }
}

function adicionarCidade(cidade, select) {
    var option = document.createElement("option")
    option.text = cidade
    select.add(option)
}