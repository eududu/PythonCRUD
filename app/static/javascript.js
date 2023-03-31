(function(win, doc){
    'use strict';

    //VERIFICAÇÃO DE DELEÇÃO DE DADOS
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Você tem certeza que quer deletar este cadastro?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }



 })(window, document);