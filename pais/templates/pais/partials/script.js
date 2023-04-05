$(document).on('click', '[data-bs-toggle="modal"]', function (event) {
    var url = $(this).data('bs-url');
    $.ajax({
        url: url,
        success: function (data) {
            $('#myModalLabel').html(data.funcao);
            $('#myModal .modal-body').html('<h1>' + data.id + '</h1><p>' + data.nm_pais + '</p>');
        }
    });
});

$(document).ready(function () {
    $('#tablepais').DataTable({
        language: {
            url:"https://cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json"
        },
    });
});