function validacao(){
    let nome = document.getElementById('nome').value;
    let email = document.getElementById('email').value;
    let fone = document.getElementById('fone').value;
    let curso = document.getElementById('cursos');
    let opcao = curso.options[curso.selectedIndex].value;
    let genero = document.querySelector('input[name="genero"]:checked').value;
    
    
    
    if(email == ""){
        alert('Preencha o campo do email')
        document.getElementById('email').focus();
        return true
    
    } if(fone == ""){
        alert('Preencha o campo do celular')
        document.getElementById('fone').focus();
        return false
    
    }
    
    if(document.forms.genero[0].checked == false && document.forms.genero[1].checked == false){
        alert('Informe seu genero')
        return false;
    }
    
    if(curso.options[curso.selectedIndex].value == ""){
       alert('Informe o curso antes de enviar o formulario')
        return false;
    
    }
    
        confirm( `Os dados preenchidos estão corretos?\nNome: ${nome}\nE-mail: ${email}\nCelular: ${fone}\n${genero}\nCurso: ${opcao} `)
        return false;
    
    } 
    