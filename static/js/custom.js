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
        order: [[0, 'asc']], // define a primeira coluna (índices) como coluna de ordenação padrão
//        order: false, // Desativa a ordenação padrão
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


// =============  Data Table - (Start) ================= //

$(document).ready(function () {
    $('#tabelaitensConsumo').DataTable({
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
                title: 'Lista de Itens de Consumo', // aqui você define o título desejado
                filename: 'Itens Consumo',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'excelHtml5',
                text: 'Exportar Excel',
                title: 'Lista de Itens de Consumo', // aqui você define o título desejado
                filename: 'Itens Consumo',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'print',
                text: 'Imprimir',
                title: 'Lista de Itens de Consumo', // aqui você define o título desejado
                exportOptions: {
                    columns: ':visible'
                }
            }
        ],
        lengthMenu: [[6, 10, 25, 50, -1], [6, 10, 25, 50, "Todos"]],
        pageLength: 6,
        order: [[0, 'asc']], // define a primeira coluna (índices) como coluna de ordenação padrão
    });

    $('.dataTables_filter input[type=search]').css({ 'width': '300px' });
});


// =============  Data Table - (End) ================= //

// =======  Função para mudar de campo com a tecla ENTER ========== //

function enableFormTabbing() {
  document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');

      var fields = form.querySelectorAll('input[type="text"], input[type="email"], input[type="number"], select');
    for (var i = 0; i < fields.length; i++) {
      fields[i].addEventListener('keydown', function(e) {
        if (e.keyCode === 13) {
          e.preventDefault();
          var nextField = getNextVisibleField(this);
          if (nextField) {
            nextField.focus();
          }
        }
      });
    }

    function getNextVisibleField(currentField) {
        var fields = Array.from(form.querySelectorAll('input[type="text"], input[type="email"], input[type="number"], select'));
      var currentIndex = fields.indexOf(currentField);
      for (var i = currentIndex + 1; i < fields.length; i++) {
        if (isElementVisible(fields[i])) {
          return fields[i];
        }
      }
      return null;
    }

    function isElementVisible(el) {
      return (el.offsetWidth > 0 || el.offsetHeight > 0);
    }
  });
}

// =======  Função para mudar de campo com a tecla ENTER - (End) ================= //
 