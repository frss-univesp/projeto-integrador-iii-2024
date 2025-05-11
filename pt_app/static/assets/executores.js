// Função para coletar e incluir os executores selecionados no formulário
function coletarExecutoresSelecionados() {
    console.log('Coletando executores selecionados...');
    
    // Obter todos os checkboxes marcados
    const checkboxesExecutores = document.querySelectorAll('#executores-qualificados-body input[type="checkbox"]:checked');
    console.log('Checkboxes marcados:', checkboxesExecutores.length);
    
    // Coletar IDs e informações dos executores selecionados
    const executoresSelecionados = [];
    
    checkboxesExecutores.forEach(checkbox => {
        const row = checkbox.closest('tr');
        
        // Obter o ID do executor do valor do checkbox
        const executorId = checkbox.value;
        
        // Obter o nome e função do executor das células da linha
        const nomeExecutor = row.cells[1].textContent;
        const funcaoExecutor = row.cells[2].textContent;
        
        console.log(`Executor selecionado: ID=${executorId}, Nome=${nomeExecutor}, Função=${funcaoExecutor}`);
        
        // Adicionar ao array de executores selecionados
        executoresSelecionados.push({
            id: executorId,
            nome: nomeExecutor,
            funcao: funcaoExecutor
        });
    });
    
    // Criar um campo hidden para cada executor selecionado
    const form = document.getElementById('form-pt');
    
    // Verificar se encontrou o formulário
    if (!form) {
        console.error('Formulário com ID "form-pt" não encontrado!');
        return false;
    }
    
    // Remover executores anteriores, se houver
    const executoresAntigos = document.querySelectorAll('input[name="executores_selecionados"]');
    executoresAntigos.forEach(executor => executor.remove());
    
    // Adicionar um campo hidden contendo o JSON de executores selecionados
    const inputExecutores = document.createElement('input');
    inputExecutores.type = 'hidden';
    inputExecutores.name = 'executores_selecionados';
    inputExecutores.value = JSON.stringify(executoresSelecionados);
    
    console.log('Valor do campo hidden:', inputExecutores.value);
    
    form.appendChild(inputExecutores);
    
    return true;
}

// Adicionar este evento ao formulário
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM carregado, procurando formulário...');
    
    const form = document.getElementById('form-pt');
    if (form) {
        console.log('Formulário encontrado, adicionando evento de submit');
        
        form.addEventListener('submit', function(event) {
            console.log('Formulário sendo enviado...');
            // Coleta os executores antes do envio
            coletarExecutoresSelecionados();
        });
    } else {
        console.error('Formulário com ID "form-pt" não encontrado!');
    }
    
    // Adicionar evento de click para debug
    document.querySelectorAll('#executores-qualificados-body input[type="checkbox"]').forEach(checkbox => {
        checkbox.addEventListener('click', function() {
            console.log('Checkbox clicado:', this.checked, 'ID:', this.value);
        });
    });
});