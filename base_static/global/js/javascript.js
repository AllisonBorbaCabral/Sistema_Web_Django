// VIEW MODAL PAIS
$(document).on('click', '[data-bs-target="#modalViewPais"]', function (event) {
    var url = $(this).data('url');
    $.ajax({
        url: url,
        success: function (data) {                 
            $('#modalViewPaisLabel').html(data.funcao)
            $('#modalViewPais #id').val(data.id);
            $('#modalViewPais #nm-pais').val(data.nm_pais);
            $('#modalViewPais #sigla').val(data.sigla);
            $('#modalViewPais #ddi').val(data.ddi);
            $('#modalViewPais #dt-cad').val(data.dt_cad);            
            $('#modalViewPais #dt-alt').val(data.dt_ult);
            if (data.situacao == 'A'){
                $('#modalViewPais #situacao').val('ATIVO');
            } else {
                $('#modalViewPais #situacao').val('INATIVO');
            }
            $('#modalViewPais').modal('show');            
        }
    });
});

// EDIT MODAL PAIS
$(document).on('click', '[data-bs-target="#modalEditPais"]', function (event) {
    var url = $(this).data('url');
    $.ajax({
        url: url,
        success: function (data) {
            $('#modalEditPaisLabel').html(data.funcao)
            $('#modalEditPais #id').val(data.id);
            $('#modalEditPais #nm-pais').val(data.nm_pais);
            $('#modalEditPais #sigla').val(data.sigla);
            $('#modalEditPais #ddi').val(data.ddi);
            $('#modalEditPais #dt-cad').val(data.dt_cad);
            $('#modalEditPais #dt-alt').val(data.dt_ult);
            if (data.situacao == 'A') {
                $('#modalEditPais #ativo').val('select');
            } else {
                $('#modalEditPais #inativo').val('select');
            }
            $('#modalEditPais').modal('show');
        }
    });
});



// $(document).on('click', '[data-bs-toggle="modal"]', function (event) {
//     var url = $(this).data('bs-url');
//     console.log(url)

//     $.ajax({
//         url: url,        
//         success: function (data) {            
//             $('#myModal .modal-body').html('<h1>' + data.id + '</h1><p>' + data.nm_pais + '</p>');
//             $('#myModal .modal-footer').html('<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button> ')
//         }
//     });
// });

// $(document).ready(function () {
//     var url = $(this).data('bs-url');
//     function consulta_pais(pk){
//         $.get("pais/consulta/" + pk + "/", function(data){
//             $('#myModal .modal-body').html(data.descricao);
//             $('#myModal .modalfooter').html('<button class="btn btn-info">TESTE</button>')
//             $('#myModal').modal('show');
//         });   
//     }
    
//     $('.consulta-pais').click(function () {
//         var pk = $(this).attr('data-pk');
//         consulta_pais(pk);
//         console.log(pk)
//     });
// });

// // EDIT MODAL PAIS  
// $(document).ready(function () {
//     // Função para carregar a modal   
//     function load_edit_pais(pk) {
//         $.get("/pais/editar/" + pk + "/", function (data) {
//             $('#PaisModalLabel').html(data.funcao);
//             $('#viewpais .modal-body').html(data.form);
//             $('#viewpais .modal-footer').html('<button class="btn btn-primary" form="edit-pais" id="salvar-pais">Salvar</button> | <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button> ');    
            
//             $('#viewpais').modal('show');
//         });
//     }
    
//     // adicionar um evento de clique ao botão de edição
//     $('.edit-pais').click(function () {
//         var pk = $(this).attr('data-pk');
//         load_edit_pais(pk);
//     });

// });

// $(document).ready(function () {
//     // Adicione um manipulador de eventos para o botão de "Salvar"
//     $('#salvar-pais').on('click', function (event) {
//         event.preventDefault();

         
//         // Obtenha os dados do formulário
//         var formData = $('#edit-pais').serialize();
//         alert(csrftoken)
        
//         // Envie uma solicitação AJAX para o servidor
//         $.ajax({
//             url: $('#edit-pais').attr('action'),
//             type: 'POST',
//             data: formData,
//             headers: {
//                 'X-CSRFToken': csrftoken
//             },
//             success: function (data) {
//                 // Se a solicitação for bem-sucedida, feche o modal
//                 $('#viewpais').modal('hide');

//                 // Recarregue a página ou atualize a tabela de países
//                 // conforme necessário
//             },
//             error: function (xhr, textStatus, errorThrown) {
//                 // Se houver um erro, exiba uma mensagem de erro ao usuário
//                 alert('Ocorreu um erro ao salvar as alterações.');
//             }
//         });
//     });
// });