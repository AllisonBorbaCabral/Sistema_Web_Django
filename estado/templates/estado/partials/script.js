$(document).on('click', '[data-bs-toggle="modal"]', function (event) {
    var url = $(this).data('bs-url');
    $.ajax({
        url: url,
        success: function (data) {
            $('#myModalLabel').html(data.funcao);
            $('#myModal .modal-body').html('<h1>' + data.id + '</h1><p>' + data.nm_estado + ' - ' + data.uf + '</p>');
        }
    });
});