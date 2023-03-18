// =============  Data Table - (Start) ================= //

$(document).ready(function () {
    $('#tabelaclientes').DataTable({
        language: {
            "decimal": "",
            "emptyTable": "Sem dados disponíveis na tabela",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
            "infoEmpty": "Mostrando 0 a 0 de 0 registros",
            "infoFiltered": "(filtrado de _MAX_ registros totais)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ por página",
            "loadingRecords": "Carregando...",
            "processing": "",
            "search": "Localizar:",
            "zeroRecords": "Nenhum registro encontrado",
            "paginate": {
                "first": "Primeiro",
                "last": "Último",
                "next": "Próximo",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": ativar para classificar a coluna em ordem crescente",
                "sortDescending": ": ativar para classificar a coluna decrescente"
            }
        },
        dom: 'lBfrtip',
        buttons: [
            {
                extend: 'pdfHtml5',
                text: 'Exportar PDF',
                title: 'Lista de Hóspedes', // aqui você define o título desejado
                filename: 'Hospedes',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'excelHtml5',
                text: 'Exportar Excel',
                title: 'Lista de Hóspedes', // aqui você define o título desejado
                filename: 'Hospedes',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'print',
                text: 'Imprimir',
                title: 'Lista de Hóspedes', // aqui você define o título desejado
                exportOptions: {
                    columns: ':visible'
                }
            }
        ],
        lengthMenu: [[6, 10, 25, 50, -1], [6, 10, 25, 50, "Todos"]],
        pageLength: 6,
        order: [[0, 'des']], // define a primeira coluna (índices) como coluna de ordenação padrão
    });

    $('.dataTables_filter input[type=search]').css({ 'width': '300px' });
});


// =============  Data Table - (End) ================= //


$(document).ready(function () {
    $('#tabelaApartamentos').DataTable({
        language: {
            "decimal": "",
            "emptyTable": "Sem dados disponíveis na tabela",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
            "infoEmpty": "Mostrando 0 a 0 de 0 registros",
            "infoFiltered": "(filtrado de _MAX_ registros totais)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ por página",
            "loadingRecords": "Carregando...",
            "processing": "",
            "search": "Localizar:",
            "zeroRecords": "Nenhum registro encontrado",
            "paginate": {
                "first": "Primeiro",
                "last": "Último",
                "next": "Próximo",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": ativar para classificar a coluna em ordem crescente",
                "sortDescending": ": ativar para classificar a coluna decrescente"
            }
        },

        dom: 'lBfrtip',
        buttons: [
            {
                extend: 'pdfHtml5',
                text: 'Exportar PDF',
                title: 'Lista de Apartamentos', // aqui você define o título desejado
                filename: 'Apartamentos',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'excelHtml5',
                text: 'Exportar Excel',
                title: 'Lista de Apartamentos', // aqui você define o título desejado
                filename: 'Apartamentos',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'print',
                text: 'Imprimir',
                title: 'Lista de Hóspedes', // aqui você define o título desejado
                exportOptions: {
                    columns: ':visible'
                }
            }
        ],
        lengthMenu: [[6, 10, 25, 50, -1], [6, 10, 25, 50, "Todos"]],
        pageLength: 6,
        
    });

    $('.dataTables_filter input[type=search]').css({ 'width': '300px' });
});
